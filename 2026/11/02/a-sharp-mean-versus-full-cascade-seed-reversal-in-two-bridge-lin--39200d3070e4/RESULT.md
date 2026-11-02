# A sharp mean-versus-full-cascade seed reversal in two bridge-linked triangles

## Finding

In an irreversible social-adoption process on two triangles joined by one bridge, let exactly two vertices be permanently seeded and independently assign every other vertex a contact threshold of one with probability \(p\) and two with probability \(1-p\). For every \(0<p<1\), the seed pair that maximizes the probability of eventual adoption by all six vertices is **one nonbridge vertex in each triangle**. In contrast, the seed pair maximizing the expected final number of adopters undergoes one sharp transition:

\[
p_\star=1-\frac{1}{\sqrt{2}}.
\]

For \(0<p<p_\star\), seed a bridge endpoint and a nonbridge vertex in the *opposite* triangle. For \(p_\star<p<1\), seed one nonbridge vertex in each triangle. At \(p=p_\star\), precisely these two seed-pair orbits tie for the maximal mean. Up to graph automorphism, these are the complete optimizer classifications; no other two-vertex seed set attains either optimum for \(0<p<1\).

Thus, throughout the entire open regime \(0<p<p_\star\), maximizing average spread and maximizing the probability of full adoption select **different initial interventions**. The transition is exact and is not a numerical crossover.

## Assumptions and scope

The undirected simple graph has vertex set \(V=\{0,1,2,3,4,5\}\) and edges

\[
E=\{\{0,1\},\{1,2\},\{0,2\},\{3,4\},\{4,5\},\{3,5\},\{2,3\}\}.
\]

The distinguished bridge endpoints are \(2\) and \(3\). The two initially active seed vertices are never required to satisfy a threshold. For each of the four other vertices \(v\), independently choose \(\tau_v=1\) with probability \(p\), or \(\tau_v=2\) with probability \(1-p\). The threshold is sampled once and remains fixed. At every synchronous step an inactive vertex joins permanently if it has at least \(\tau_v\) active neighbors. Let \(Z_S\) be the size of the eventual stable active set starting from the two-element seed set \(S\). The optimization criteria are \(\mathbb E Z_S\) and \(\Pr(Z_S=6)\); there is no empirical calibration, recovery, stochastic transmission, weighted edges, or additional intervention.

Graph automorphisms divide the \(\binom62=15\) seed pairs into the following four types. Here \(A\) denotes two vertices in the same triangle, \(B\) a bridge endpoint and a nonbridge vertex in the opposite triangle, \(C\) a nonbridge vertex in each triangle, and \(D\) the two bridge endpoints. Representatives \(S_A=\{0,1\}\), \(S_B=\{0,3\}\), \(S_C=\{0,4\}\), and \(S_D=\{2,3\}\) have orbit sizes \(6,4,4,1\), respectively.

## Proof

**Finite configuration identity.** Fix a seed-pair type \(T\in\{A,B,C,D\}\). Given an assignment of the four nonseed thresholds, let \(k\) be the number of threshold-one vertices, let \(z\) be the final number adopted, and let \(h=1\) if \(z=6\) (otherwise \(h=0\)). Define \(H_{T,k}\) as the sum of \(z\), and \(J_{T,k}\) as the sum of \(h\), over all \(\binom4k\) threshold assignments with that \(k\). Enumerating the sixteen assignments in each of the four graph-automorphism classes gives the exact integer table:

| Type | \((H_{T,0},H_{T,1},H_{T,2},H_{T,3},H_{T,4})\) | \((J_{T,0},J_{T,1},J_{T,2},J_{T,3},J_{T,4})\) |
|:--|:--|:--|
| \(A\) | \((3,13,25,21,6)\) | \((0,0,2,3,1)\) |
| \(B\) | \((4,20,34,24,6)\) | \((0,2,5,4,1)\) |
| \(C\) | \((2,24,36,24,6)\) | \((0,4,6,4,1)\) |
| \(D\) | \((2,16,32,24,6)\) | \((0,0,4,4,1)\) |

This is an **exhaustive finite proof** of the table, not a sample: a complete independent specification for its reproduction is the standalone `verify.py` included with this result. For each seed pair and each of the sixteen threshold vectors, the checker both iterates activation and independently intersects every stable superset of the seeds. Equality of the two characterizations also checks the cascade's eventual closure. Every other seed pair is assigned to and checked against exactly one orbit type, thereby covering all fifteen seed pairs. No unenumerated configuration enters the model.

Independence of the four threshold draws now yields two polynomial identities for every \(0\le p\le1\):

\[
M_T(p):=\mathbb E Z_{S_T}=\sum_{k=0}^4 H_{T,k}p^k(1-p)^{4-k},\qquad
Q_T(p):=\Pr(Z_{S_T}=6)=\sum_{k=0}^4 J_{T,k}p^k(1-p)^{4-k}.
\]

Substitution and expansion give

\[
\begin{aligned}
M_A&=3+p+4p^2-2p^3, & Q_A&=p^2(2-p),\\
M_B&=4+4p-2p^2, & Q_B&=p(2-p),\\
M_C&=6-4(1-p)^4, & Q_C&=p(2-p)(1+(1-p)^2),\\
M_D&=2+8p-4p^2, & Q_D&=p^2(2-p)^2.
\end{aligned}
\]

**Mean-optimal pair.** For every \(0<p<1\), exact factorization gives

\[
M_B-M_A=(1-p)(1+4p-2p^2)>0,
\qquad M_B-M_D=2(1-p)^2>0.
\]

(The first parenthesis is at least one for \(0\le p\le1\).) Hence neither \(A\) nor \(D\) can maximize the mean; only \(B\) and \(C\) remain. Their signed difference is

\[
M_B-M_C=2(1-p)^2(2p^2-4p+1).
\]

The quadratic has roots \(1\pm1/\sqrt2\), and exactly one lies in \((0,1)\). Its sign is positive before \(p_\star=1-1/\sqrt2\), vanishes at that point, and is negative thereafter. This proves the unique crossover and all equality cases among the fifteen seed sets.

**Complete-adoption optimum.** The full-adoption polynomials satisfy, throughout \(0<p<1\),

\[
\begin{aligned}
Q_C-Q_A&=p(1-p)(2-p)^2>0,\\
Q_C-Q_B&=p(2-p)(1-p)^2>0,\\
Q_C-Q_D&=2p(2-p)(1-p)^2>0.
\end{aligned}
\]

Therefore only type \(C\) maximizes the probability of full adoption, and it does so strictly across graph-automorphism orbits. Combining the two criteria proves the assertion.

As a concrete exact witness inside the conflict regime, at \(p=1/4\) type \(B\) has \(M_B=39/8\) and \(Q_B=7/16\), while type \(C\) has \(M_C=303/64\) and \(Q_C=175/256\). Thus \(B\) gives greater mean spread but lower full-adoption probability.

## Verification

Run `python verify.py` with Python 3 and SymPy from the supplied files. The verifier independently reconstructs the seven edges; enumerates the entire set of \(15\) seed pairs and all \(16\) independent nonseed-threshold assignments for each pair; compares synchronous closure with the intersection of all stable supersets; checks orbit sizes, each integer coefficient of the displayed table, polynomial expansions and factorizations, as well as rational test points and endpoint degeneracies. The final packaged verifier completed **348 exact assertions** and checked **240 threshold assignments twice**, without simulation or floating-point reliance for mathematical decisions. The sign arguments above, rather than finite numerical samples, establish the all-\(p\) result.

## Relationship to prior work

Watts (2002) supplies an influential heterogeneous-threshold cascade framework on random graphs. Kempe, Kleinberg and Tardos (2003; expanded 2015) formulate network influence maximization and a general random-threshold model that encompasses these independent discrete thresholds. Their theorems concern general equivalence, computational hardness and approximation; they do not imply the exact four-orbit two-objective comparison for this particular graph. O'Sullivan and colleagues (2015) address complex contagion on clustered, clique-based networks through approximate large-network dynamics and social reinforcement; those results do not give this finite exact seed-pair optimizer. Published results about deterministic conversion sets on complete multipartite graphs and zero-forcing of bridge-linked cliques use different local rules and do not imply either signed comparison above. The searched accessible sources did not supply an equivalent exact two-criterion threshold; that observation does not establish comprehensive historical priority.

## Limitations

This theorem addresses only the specified six-vertex graph, one-time independent Bernoulli thresholds taking values one or two, exactly two permanent seeds, and the eventual binary adoption state. It does not imply the same optimizer structure for larger cliques, asymmetric probabilities, network dynamics, finite-time objectives, independent-cascade per-edge transmission or empirical social interventions. The scientific proof is finite and exhaustive for this exact system, but no independent external audit or claim of established historical priority is made. A full-text comparison with the original Watts article was unavailable, and equivalent old calculations in other terminology cannot be ruled out by searched titles and abstracts alone.

## References

1. D. J. Watts, “A simple model of global cascades on random networks,” *Proceedings of the National Academy of Sciences* **99** (2002), 5766–5771; publicly dated 2002-04-30. DOI: https://doi.org/10.1073/pnas.082090499.
2. D. Kempe, J. Kleinberg and É. Tardos, “Maximizing the Spread of Influence through a Social Network,” *KDD* (2003), 137–146, DOI: https://doi.org/10.1145/956750.956769. Expanded open-access article, *Theory of Computing* **11** (2015), 105–147, DOI: https://doi.org/10.4086/toc.2015.v011a004.
3. D. J. P. O'Sullivan, G. J. O'Keeffe, P. G. Fennell and J. P. Gleeson, “Mathematical modeling of complex contagion on clustered networks,” *Frontiers in Physics* **3** (2015), article 71, publicly dated 2015-09-15. DOI: https://doi.org/10.3389/fphy.2015.00071.
