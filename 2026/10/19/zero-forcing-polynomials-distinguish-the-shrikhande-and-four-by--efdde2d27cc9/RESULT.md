# Zero-forcing polynomials distinguish the Shrikhande and four-by-four rook graphs

## Finding

Let \(S\) be the Shrikhande graph and \(R=K_4\square K_4\) the four-by-four rook graph, with the explicit common vertex labeling given below. Under the **ordinary** zero-forcing rule, the exact polynomials of initial forcing sets are

\[
\begin{aligned}
\mathcal Z(S;z)&=3616z^{10}+3600z^{11}+1760z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16},\\
\mathcal Z(R;z)&=3456z^{10}+3504z^{11}+1760z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\end{aligned}
\]

In particular,
\[\mathcal Z(S;z)-\mathcal Z(R;z)=160z^{10}+96z^{11}.\]
Both graphs have the same strongly regular parameters \((16,6,2,2)\), hence the same adjacency spectrum \(\{6^1,2^6,(-2)^9\}\), and the same ordinary zero-forcing number \(10\). Nonetheless their complete forcing polynomials differ. Every inclusion-minimal ordinary zero-forcing set in either graph has size \(10\). There are \(3616\) such sets for \(S\) and \(3456\) for \(R\). Consequently the two graphs have respectively \(9673\) and \(9417\) forcing sets in total.

The \(3616\) minimum forcing sets of \(S\) form exactly \(23\) orbits under its full automorphism group of order \(192\), with orbit-size multiset \(192\) repeated \(15\) times, \(96\) repeated \(7\) times, and \(64\) once. Of these sets, \(1312\) finish in two synchronous forcing rounds and \(2304\) in three rounds; for \(R\), the respective counts are \(864\) and \(2592\).

The following obstruction hierarchy gives an exact structural accounting. A *fort* is a nonempty vertex subset \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). In \(S\), the numbers of inclusion-minimal forts of orders \(4,5,6\) are \(60,48,336\); in \(R\), they are \(60,144,112\). There are no inclusion-minimal forts of other orders. Among six-vertex white sets, the counts classified by the **least order of a contained fort** are:

| Least fort order | Shrikhande | Rook |
| :-- | --: | --: |
| \(4\) | \(3720\) | \(3720\) |
| \(5\) | \(336\) | \(720\) |
| \(6\) | \(336\) | \(112\) |
| No fort (forcing complement) | \(3616\) | \(3456\) |

Thus the polynomial distinction is supported by a difference in the minimum-obstruction geometry, not just by unrelated set totals.

## Assumptions and scope

All graphs here are finite, simple and undirected. The vertex set of both graphs is \(V=(\mathbb Z/4\mathbb Z)^2\), ordered by the vertex index \(4a+b\), for \(a,b\in\{0,1,2,3\}\).

For \(S\), vertices \(u,v\) are adjacent exactly when their coordinate difference modulo \(4\) is in
\[
D=\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}.
\]
For \(R\), distinct vertices are adjacent exactly when they agree in one coordinate. This explicitly fixes all edges and avoids any appeal to a graph database or particular drawing.

Initially the vertices of \(B\subseteq V\) are blue; all others are white. A blue vertex having exactly one white neighbor may color that neighbor blue. A set is *zero forcing* if repeated applications color all vertices. The polynomial \(\mathcal Z(G;z)=\sum_{k=0}^{16}z(G;k)z^k\) counts each labeled blue subset once. A synchronous round applies all currently available forces before the next round. Synchronous forcing determines the same final closure as any fair sequential order; the number of rounds reported is for this explicit synchronous convention. The invariant is ordinary zero forcing, **not** positive-semidefinite or skew zero forcing.

## Proof

**Graph normalization and cospectrality.** For both explicit adjacency rules, every vertex has exactly six neighbors and every distinct pair has exactly two common neighbors. Directly: the former follows from the six listed Cayley differences or the three other row and three other column positions; the latter is checked by fixed coordinate differences in \(S\) and the row/column cases in \(R\). Consequently each adjacency matrix \(A\) satisfies \(A^2=4I+2J\). On the all-ones vector \(A\) has eigenvalue \(6\), and on its perpendicular complement eigenvalues are \(\pm2\). Trace zero yields multiplicities \(6\) and \(9\) for \(2\) and \(-2\). The graphs are not isomorphic: the neighbors of each vertex induce one six-cycle in \(S\) but two disjoint triangles in \(R\).

**Fort duality.** Write \(W=V\setminus B\) for the initially white set. Then \(B\) is zero forcing **if and only if** \(W\) contains no nonempty fort. Indeed, if \(F\subseteq W\) is a fort, there cannot be a first vertex of \(F\) forced: every blue vertex outside \(F\) has zero or at least two neighbors still in \(F\), so none has a unique white neighbor there. Conversely, if forcing stops with a nonempty white set \(F\), every outside (blue) vertex has zero or at least two neighbors in \(F\), making \(F\) a fort. This establishes the equivalence for every initial set, without assuming that a particular sequence of color choices succeeds.

**Finite exact computation.** Since \(|V|=16\), the preceding lemma reduces the complete classification to a proof by exhaustive, fixed-bound enumeration. Identify each set \(W\) with the unique integer mask \(0\le w<2^{16}\) whose bits are its vertex indicators. For each nonempty mask \(f\), test the literal fort condition
\[
\forall v\in V\setminus F:\quad |N(v)\cap F|\ne 1.
\]
Call this truth value \(q[f]\); put \(q[0]=0\). A Boolean subset-zeta transform computes
\[
Q[w]=\bigvee_{f\subseteq w}q[f]
\]
by the sixteen updates \(Q[w]\gets Q[w]\lor Q[w\setminus\{i\}]\), over each bit \(i\) present in \(w\). Hence the coefficient of \(z^{16-|w|}\) is incremented precisely when \(Q[w]=0\). These are **all** possible subsets, not a sample. To test inclusion-minimality of a forcing blue set with white mask \(w\), check that each single-bit addition to \(w\) creates a nonforcing state; the monotonicity of the forcing property makes this necessary and sufficient. For minimal forts, the same subset-zeta array tests whether a fort has any proper nonempty fort subset.

The standalone C++ verifier implements this finite set-theoretic proof directly and checks the complete coefficients, minimal forcing sets and minimal fort spectrum. It enumerates exactly \(2^{16}\) masks for each graph; no heuristic termination or interpolation is used. A second standalone Python verifier independently runs synchronous force-closure on every possible initial blue subset, without calling the fort algorithm. The two methods reproduce every coefficient, the total numbers and the inclusion-minimal counts, and agree **bit for bit** on both complete forcing truth tables. Their 16,384-byte common certificate stores one bit per possible blue mask per graph. In particular, for five white vertices the fort classes (none, minimum contained fort of size four, minimum contained fort of size five) are \((3600,720,48)\) for \(S\), and \((3504,720,144)\) for \(R\). For six white vertices they give the table in the finding. For at most four white vertices, the only obstructions are exactly the \(60\) size-four forts; for at least seven white vertices, every set contains some fort. These verified statements yield the two displayed polynomials and all listed forcing and fort counts. The independent closure census supplies the synchronous-round distributions.

**Full symmetry and orbit computation.** The translations of \((\mathbb Z/4\mathbb Z)^2\) together with the twelve invertible linear maps that preserve \(D\) give \(16\cdot12=192\) distinct automorphisms of \(S\). This is the **full** automorphism group: fixing a root, an automorphism acts on its six neighbors, which induce a six-cycle, in at most \(12\) ways; each of the other nine vertices is uniquely determined by its distinct pair of neighbors among that six-cycle. Thus an automorphism is determined by the root image and its action on this cycle, giving the upper bound \(16\cdot12=192\). The orbit verifier independently reconstructs these \(192\) maps, checks they preserve adjacency, enumerates the \(3616\) successful six-white masks, and partitions them by the group action. The \(23\) explicit orbit representatives and their sizes are in `certificates/shrikhande_minimum_orbits.csv`. Orbit sizes add to \(3616\); the verifier also checks the two- and three-round classifications.

## Verification

From the package root, with Python 3.10 or newer and a C++17 compiler, run:

```sh
python3 scripts/verify_simulation.py
g++ -std=c++17 -O2 -Wall -Wextra scripts/verify_forts.cpp -o verify_forts
./verify_forts certificates/forcing_truth_tables.bin
python3 scripts/verify_orbits.py
```

The two independent classifications compare all \(131072\) graph/initial-set decisions against the binary certificate; its first \(8192\) bytes encode \(S\), and its second \(8192\) bytes encode \(R\). Within each block, bit \(j\) of byte \(i\) gives the zero-forcing truth value for blue mask \(8i+j\). The separate orbit certificate records a white six-set as four lowercase hexadecimal digits, its orbit size, the number of edges it induces, its induced component sizes, and its synchronous propagation time. Both verifiers generate their own graph adjacency lists from the definitions above; the fort verifier does not invoke the force-closure algorithm. The orbit verifier requires `scripts/verify_simulation.py`, which is supplied.

## Relationship to prior work

The ordinary zero-forcing rule and its use in minimum-rank questions predate this computation; see Barioli et al. (2010) and the foundational references therein. Boyer et al. (2018) introduce the full zero-forcing polynomial and discuss its general properties and fort obstructions. The present result does not claim either concept as new. Rook-graph zero forcing has been characterized more broadly; the rook polynomial here is a controlled benchmark rather than a priority claim for that graph alone.

Abiad et al. (2022), Proposition 3.6, explicitly consider the Shrikhande/rook cospectral pair and compare **positive-semidefinite** zero-forcing numbers, reporting values \(9\) and \(10\). Their comparison uses a different color-change rule and does not determine the ordinary zero-forcing polynomials or the Shrikhande minimum-set orbits. In the ordinary rule addressed here, both graphs instead have minimum number \(10\), while their complete generating polynomials and minimal-fort spectra distinguish them. The contribution is this explicit ordinary-forcing classification and symmetry description; a prior unindexed enumeration remains possible.

## Limitations

These statements are exact only for the two explicitly defined sixteen-vertex graphs. They do **not** imply a formula for all strongly regular graphs or that zero-forcing polynomials distinguish all cospectral graphs. The finite proof depends on complete execution of the supplied, auditable enumerators; a numerical transcript alone is not a proof. The same algorithms give finite exact certificates but do not establish historical priority or substitute for independent mathematical review. The known positive-semidefinite comparison should not be confused with the ordinary-forcing statement.

## References

1. F. Barioli et al., *Zero forcing parameters and minimum rank problems*, arXiv:1003.2028v1 (first public arXiv version 2010-03-10), https://arxiv.org/abs/1003.2028.
2. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018-01-26), https://arxiv.org/abs/1801.08910.
3. A. Abiad, B. Brimkov, J. Breen, T. R. Cameron, H. Gupta and R. R. Villagrán, *Constructions of cospectral graphs with different zero forcing numbers*, Electronic Journal of Linear Algebra **38** (2022), 280–294, DOI:10.13001/ela.2022.6737, https://pure.tue.nl/ws/portalfiles/portal/206533710/vol38_pp280_294.pdf.
