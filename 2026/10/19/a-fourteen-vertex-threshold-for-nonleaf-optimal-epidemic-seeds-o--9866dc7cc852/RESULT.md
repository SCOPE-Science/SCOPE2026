# A fourteen-vertex threshold for nonleaf optimal epidemic seeds on trees

## Finding

Consider a finite, connected, undirected, simple tree \(T\) with at least two vertices. Starting with just one infected vertex \(v\), each infected vertex makes exactly one contact, selecting uniformly among all its neighbors, and then recovers permanently. A previously uninfected contact becomes the next infected vertex; a contact with a previously infected vertex terminates the spread. Thus the infected set is a simple path; let \(E_T(v)\) be its expected number of vertices.

**Sharp leaf-optimality boundary.** Every tree on \(2\) through \(13\) vertices has at least one leaf \(v\) maximizing \(E_T(v)\) over all starting vertices. There exists a tree on \(14\) vertices whose unique maximizing vertex is not a leaf. The following labelled tree exhibits this:

```text
(1,0) (1,2) (0,7) (2,3) (3,4) (4,5) (4,6)
(7,8) (7,11) (8,9) (9,10) (11,12) (12,13)
```

For that tree, vertex \(0\) has \(E_T(0)=49/16\), whereas the greatest score of any leaf is \(1763/576\), attained at vertices \(10\) and \(13\). The exact strict advantage is \(1/576\). All other vertices have score below that of vertex \(0\).

## Assumptions and scope

The graph is unweighted, finite, connected, undirected, loop-free and acyclic. There is one deterministic seed, selected before the process. Contacts are independent and uniformly distributed over the *full* neighbor set, including already infected neighbors. Transmission succeeds with probability one if the contact is susceptible. Every infected vertex makes one attempt total, with no reinfection or recovery delay. The objective is to **maximize** cumulative infections, not to minimize them and not to average over a random seed. Both the attempt leading to an already infected neighbor and the final recovery introduce no additional infected vertex. The statement holds for **every** tree of the given sizes; no population or asymptotic random-network assumptions are made.

A vertex of degree \(1\) is a leaf. For the two-vertex tree both vertices are leaves. Only trees with at least two vertices are quantified in the claim.

## Proof

**1. Exact expectation recurrence.** For adjacent vertices \(u,p\) of a tree, define \(F(u,p)\) to be the expected number of *newly counted* infected vertices starting with \(u\) when \(p\) is already infected and the previous transmission came from \(p\) to \(u\). Then

\[
F(u,p)=1+\frac{1}{\deg_T(u)}\sum_{w\in N_T(u)\setminus\{p\}}F(w,u).
\]

Indeed, contact with \(p\) terminates without infection, whereas choosing any other neighbor \(w\) (probability \(1/\deg_T(u)\)) initiates infection of \(w\). On a tree no other previously infected vertex can be adjacent to \(u\); otherwise the traversed path plus that edge would be a cycle. The recursion is well-founded on the component of \(T-up\) containing \(u\). Hence

\[
E_T(v)=1+\frac{1}{\deg_T(v)}\sum_{u\in N_T(v)}F(u,v).
\]

These formulas give exact rational values on any tree.

**2. Complete enumeration up to \(13\) vertices.** `verify.py` starts from the unique one-vertex tree. For each representative tree of order \(n\), it attaches a newly labelled leaf at each of the \(n\) vertices; it then retains one tree per canonical unlabelled isomorphism class. A finite tree of order at least \(2\) has a leaf; deleting it gives a tree on one fewer vertex, so by induction every isomorphism type occurs in this generation. The canonical code is the lexicographically smaller sorted recursive rooted-parenthesis string at the tree center(s), as obtained by repeatedly stripping leaves. The standard center argument shows that any isomorphism maps the center(s) to the center(s), and recursively sorted rooted strings are equal exactly for isomorphic rooted trees. Consequently deduplication neither loses an isomorphism type nor keeps duplicate types. The generated counts for orders \(1,\ldots,13\) are

```text
1 1 1 2 3 6 11 23 47 106 235 551 1301
```

For **every** generated tree of order \(2\) through \(13\), the program computes \(E_T(v)\) exactly at every vertex using rational arithmetic and checks the equality

\[
\max_{v\in V(T)}E_T(v)=\max_{v\text{ a leaf}}E_T(v).
\]

The source and the finite complete-enumeration argument jointly prove the lower bound: no tree with at most \(13\) vertices forces all maximizing seeds to be internal.

**3. Explicit order-\(14\) witness.** Apply the recurrence to the displayed tree, in vertex order \(0,\ldots,13\), obtaining

\[
\left(\frac{49}{16},3,\frac{47}{16},\frac{91}{32},\frac{673}{288},\frac{865}{288},\frac{865}{288},\frac{407}{144},\frac{827}{288},\frac{1475}{576},\frac{1763}{576},\frac{827}{288},\frac{1475}{576},\frac{1763}{576}\right).
\]

Vertex \(0\) has degree \(2\), so is internal. Inspection of the exact vector shows it is the **unique** maximizer, and every leaf is strictly worse. Indeed \(49/16-1763/576=1/576>0\). This closes the bound sharply.

## Verification

Both programs use Python 3 standard-library rational arithmetic, with no data downloads or dependencies: run `python3 verify.py` and `python3 crosscheck.py` from their containing directory. `verify.py` checks all unlabelled trees up to order \(13\), the displayed edges, and the rational optimum gap. Independently, `crosscheck.py` sums probabilities of all simple path prefixes from each witness root; the resulting \(14\) expectations agree with the directed-edge recursion. The certificates are finite and self-contained; an unrestricted order claim is neither stated nor inferred.

## Relationship to prior work

Kenah and Robins (publicly available in 2006) analyze finite-population SIR epidemic networks and outbreak-size representations, but do not give the one-contact *fixed-tree, seed-vertex* extremum or a sharp order cutoff. Gómez and coauthors (2009) analyze individual one-neighbor contacts in a discrete-time model with possible reinfections, focusing on stationary infection prevalence and thresholds, not cumulative infections in this irreversible single-contact model. Tishby, Biham and Katzav (2016) consider **the same first-repetition stopping rule for a random walk** on Erdős–Rényi graph ensembles and a random initial vertex; the present work instead optimizes the deterministic starting vertex on *every* finite tree and identifies the least-order exception to leaf optimality. Enright and Kao (2016) give exact expected outbreak-size algorithms on directed acyclic time-expanded networks, rather than this seed-location classification.

The first-repetition random-walk equivalence on a tree is mathematically exact: until its first attempted return to a visited vertex, the infection chain and ordinary simple random walk visit the same distinct vertices. This equivalence is **used for overlap checking** and is not claimed as new.

## Limitations

The edge weights, contact counts and seed objective are fixed as defined. The small gap in the \(14\)-vertex witness should not be interpreted as epidemiologically large. An unindexed equivalent tree-seed extremum remains a possibility; the novelty assessment compares the most relevant accessible sources, not every possible historical document. No independent external validation is asserted. The result does not apply to recurrent SIS models, independent bond percolation, general graphs with cycles, or non-backtracking walks without reanalysis.

## References

1. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057v1 (30 October 2006), https://arxiv.org/abs/q-bio/0610057.
2. S. Gómez et al., *Discrete-time Markov chain approach to contact-based disease spreading in complex networks*, arXiv:0907.1313v1 (7 July 2009), https://arxiv.org/abs/0907.1313.
3. I. Tishby, O. Biham and E. Katzav, *The distribution of first hitting times of random walks on Erdős–Rényi networks*, arXiv:1606.01560v1 (5 June 2016), https://arxiv.org/abs/1606.01560.
4. J. Enright and R. R. Kao, *A fast algorithm for calculating an expected outbreak size on dynamic contagion networks*, *Epidemics* 16 (2016), 56–62, https://doi.org/10.1016/j.epidem.2016.05.002.
5. I. Tishby, O. Biham and E. Katzav, *The distribution of first hitting times of non-backtracking random walks on Erdős–Rényi networks*, arXiv:1609.08375v1 (27 September 2016), https://arxiv.org/abs/1609.08375; the non-backtracking process differs because it forbids immediate returns.
