# Component obstructions and the sharp random resolving window of two-subset Kneser graphs

## Finding

**Theorem.** Fix an integer \(n\ge5\). Let \(G=\mathrm{KG}(n,2)\), whose vertices are the two-element subsets of \([n]\), with two vertices adjacent when they are disjoint. Identify a subset \(S\subseteq V(G)\) with the edge set of a simple spanning graph \(H_S=([n],S)\).

The set \(S\) is a metric resolving set of \(G\) **if and only if** all four of the following conditions hold:

1. \(H_S\) has at most one isolated vertex.
2. No connected component of \(H_S\) is \(K_2\).
3. It is not the case that \(H_S\) has both an isolated vertex and a connected component \(P_3\).
4. No connected component of \(H_S\) is \(P_4\) or \(C_4\).

In particular, membership in the family of resolving sets can be decided from the connected components of \(H_S\), in time \(O(n+|S|)\) when its edge list is supplied.

Now independently include each vertex of \(G\) in \(S_p\) with probability \(p\). For every fixed real \(c\), put \(p_n=(\log n+c)/n\), with \(n\) sufficiently large that \(0<p_n<1\). Then

\[
\lim_{n\to\infty}\Pr\bigl(S_{p_n}\text{ resolves }\mathrm{KG}(n,2)\bigr)
=\exp(-e^{-c})(1+e^{-c}).
\]

Thus random resolving sets have a sharp threshold at \(p=(\log n)/n\): if \(p_n=(\log n+c_n)/n\) is a valid probability with \(c_n\to+\infty\), the success probability tends to one; if \(c_n\to-\infty\), it tends to zero. At the critical window, the limiting success probability differs from the classical random-graph connectivity limit by allowing **one**, rather than zero, isolated ground vertices.

## Assumptions and scope

Graphs are finite, undirected, simple, and labeled on the indicated vertex sets. A metric resolving set \(S\) of a connected graph is a set of distance probes such that for every two distinct vertices \(u,v\), some \(s\in S\) satisfies \(d(s,u)\ne d(s,v)\). The notation \(P_j\) means the path on \(j\) vertices; \(C_4\) is the four-cycle. A *component* is maximal connected: the prohibitions above do not exclude non-induced copies inside larger components. A *spanning graph* includes all \(n\) ground vertices, including isolates. Natural logarithms are used in the random threshold.

For the random statement the independent probe model corresponds exactly to the binomial random ground graph \(H_{S_p}\sim G(n,p)\). The first assertion is deterministic for every \(n\ge5\), with no asymptotic or probabilistic assumption.

## Proof

### Distance reduction

For distinct two-subsets \(e,f\) of \([n]\),
\[
d_G(e,f)=\begin{cases}1,&e\cap f=\varnothing,\\2,&e\cap f\ne\varnothing.\end{cases}
\]
Indeed disjoint two-subsets are adjacent, while two intersecting distinct two-subsets have a common disjoint two-subset because their union has three points and \(n\ge5\).

Suppose \(e=\{a,b\}\) and \(f=\{a,c\}\) intersect. A probe \(w\) distinguishes them exactly when the corresponding ground edge has one endpoint in \(\{b,c\}\) and the other outside \(\{b,c\}\). This remains true when \(w=e\) or \(w=f\), since the zero distance distinguishes the target. The edge \(\{b,c\}\) itself does not distinguish them. Consequently, the pair is unresolved precisely if no selected ground edge leaves \(\{b,c\}\). This happens precisely when \(b,c\) are both isolated in \(H_S\), or when they form a two-vertex connected component \(K_2\). Because \(n\ge5\), every two selected ground vertices \(b,c\) can be accompanied by a distinct \(a\), so both obstructions genuinely produce an unresolved intersecting target pair.

Next take disjoint target edges \(e=\{a,b\}\) and \(f=\{c,d\}\) and put \(U=\{a,b,c,d\}\). The probes distinguishing \(e\) and \(f\) are exactly: the two target edges \(e,f\) themselves, and ground edges with precisely one endpoint in \(U\). Other ground edges either meet both targets or neither. Hence \(e,f\) are unresolved precisely if \(H_S\) has no selected edge leaving \(U\) and the induced graph \(H_S[U]\) has no edge inside either \(\{a,b\}\) or \(\{c,d\}\). Equivalently, \(U\) is a union of connected components and \(H_S[U]\) is a subgraph of a balanced complete bipartite graph with these two sides of order two.

Assume that the intersecting-pair obstructions are absent: there are at most one isolate and no \(K_2\) component. Any such four-vertex union of components must then be either one component on four vertices or a three-vertex component together with one isolated vertex. In the connected four-vertex case, a bipartite graph admitting part sizes two and two must be \(P_4\) or \(C_4\): its connected spanning subgraph has at least three of the four edges of \(K_{2,2}\). In the three-plus-one case, the three-vertex component must be \(P_3\), with the isolated vertex placed on the smaller bipartition side. Conversely, \(P_4\), \(C_4\), and \(P_3\) together with an isolate each supply a balanced bipartition of an edge-closed four-vertex set, and hence a pair of unresolved disjoint target edges. This proves the exact four-obstruction characterization.

### Random critical window

With independent vertex probes at rate \(p_n\), the ground graph is exactly the binomial random graph \(G(n,p_n)\). Let \(X_n\) be its number of isolated vertices. For every fixed positive integer \(r\), the falling factorial moment is
\[
\mathbb E (X_n)_r=(n)_r(1-p_n)^{r(n-r)+\binom r2}\longrightarrow e^{-rc}.
\]
These are the factorial moments of a Poisson random variable with mean \(\lambda=e^{-c}\). The standard factorial-moment criterion therefore gives \(X_n\Rightarrow\mathrm{Poisson}(\lambda)\).

Let \(Y_{n,k}\) count connected components with exactly \(k\) vertices for \(k\in\{2,3,4\}\). Every such component contains a spanning tree on its \(k\) vertices and has no edge to its complement. Cayley's tree count and a union bound imply
\[
\mathbb E Y_{n,k}\le \binom nk k^{k-2}p_n^{k-1}(1-p_n)^{k(n-k)}
=O\!\left(\frac{(\log n)^{k-1}}{n^{k-1}}\right)=o(1).
\]
Thus with probability tending to one the ground graph has no component of order two, three, or four. On this event, the deterministic characterization reduces exactly to \(X_n\le1\). It follows that the difference between the resolving probability and \(\Pr(X_n\le1)\) tends to zero. Poisson convergence gives
\[
\Pr(X_n\le1)\longrightarrow\Pr(\mathrm{Poisson}(\lambda)\le1)
=e^{-\lambda}(1+\lambda),
\]
which is the asserted limiting law.

Finally, the resolving property is increasing when probes are added. Sandwiching any \(c_n\to+\infty\) (respectively \(c_n\to-\infty\)) between fixed large positive (respectively fixed large negative) window shifts, and then letting the fixed shift tend to infinity in magnitude, proves both sharp-threshold statements.

## Verification

The standalone C++17 program `verify.cpp` constructs the complete distance-distinguishing masks for \(\mathrm{KG}(n,2)\) directly from disjointness. Its first implementation tests metric resolution by comparing every pair of Kneser vertices. Its second implementation checks only the four connected-component obstructions, independently through a disjoint-set data structure. The two tests agree on **every** ground edge subset for \(n=5,6,7\): respectively \(1024\), \(32768\), and \(2097152\) inputs. They additionally agree on \(150000\) seeded random samples with \(n\in\{8,9,10\}\) and five different edge densities. The recorded run output is in `verification_output.txt`.

Reproduce with `g++ -O3 -std=c++17 -Wall -Wextra -Werror verify.cpp -o verify && ./verify`. The random limiting law is proved analytically and is not inferred from finite simulation.

## Relationship to prior work

Bailey and Cameron (2011), Theorem 3.32 and Corollary 3.33, determine the minimum metric dimension of \(\mathrm{KG}(n,2)\) (equivalently \(J(n,2)\)) as a function of \(n\) modulo three. That scalar extremal result neither classifies all resolving probe subsets nor evaluates their random success probability.

Bailey et al. (2013), Lemma 2 and Lemma 5, explain the relation between Johnson and Kneser resolving sets and give a general intersection-test formulation; their treatment offers resolving-set constructions and metric-dimension bounds, not the four explicit component obstructions or a binomial random-probe limit. Our structural criterion is a nontrivial simplification of the general resolution test for \(k=2\), not a claim to have first formulated that test.

Bonato, Huggan and Marbach (2020), Section 2, connect metric resolving sets of diameter-two Kneser graphs with hypergraph detectability. Their general estimates principally concern uniformity at least three. The exact component criterion and its sharp window are not stated in the inspected material. The elementary isolated-vertex Poisson limit for \(G(n,p)\) is standard; the new assertion is its specific two-isolate-tail role in Kneser resolution, which follows from the component classification.

## Limitations

The component characterization is restricted to two-element Kneser graphs, and the probability limit is for independent uniformly sampled vertex probes. The theorem makes no claim about larger-subset Kneser graphs, nonuniform sensor sampling, optimal deterministic sensor layouts, or distributions outside the specified window. The cited prior results include general intersection-based tests, so the novelty claimed here is the precise structural obstruction theorem and the resulting non-connectivity Poisson law, not the underlying distance formula or the classical Poisson theorem. Exhaustive tests stop at the stated finite orders and do not certify the infinite-family proof. No independent scientific validation or exhaustive proof of bibliographic priority has been performed.

## References

1. R. F. Bailey and P. J. Cameron, *Base size, metric dimension and other invariants of groups and graphs*, Bulletin of the London Mathematical Society **43** (2011), 209–242, Theorem 3.32 and Corollary 3.33. Author-hosted manuscript: https://maths.qmul.ac.uk/~pjc/preprints/bsod.pdf ; DOI: 10.1112/blms/bdq096.
2. R. F. Bailey, J. Cáceres, D. Garijo, A. González, A. Márquez, K. Meagher and M. L. Puertas, *Resolving sets for Johnson and Kneser graphs*, European Journal of Combinatorics **34** (2013), 736–751, Lemmas 2 and 5. arXiv:1203.2660, https://arxiv.org/pdf/1203.2660 .
3. A. Bonato, M. A. Huggan and T. Marbach, *The localization number and metric dimension of graphs of diameter 2*, first publicly posted 11 August 2020, arXiv:2008.04896v1 [math.CO], Section 2, https://arxiv.org/html/2008.04896v1 .
