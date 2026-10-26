# Exact low-failure total Roman bondage polynomial of complete prisms

## Finding

Let \(G_n=K_n\square K_2\) for every integer \(n\ge3\), with vertices \(a_i,b_i\) for \(1\le i\le n\), each of \(\{a_i\}\) and \(\{b_i\}\) spanning a clique, and additional matching edges \(a_ib_i\). A total Roman dominating function on an isolate-free graph assigns \(0,1,2\) to vertices, requires each zero to have a neighbor labelled \(2\), and requires the positive-labelled vertices to induce a graph with no isolated vertices. Write \(\gamma_{tR}\) for its least weight.

For every integer \(0\le k\le n-1\), let \(F_{n,k}\) be the number of distinct \(k\)-edge subsets \(B\subseteq E(G_n)\) such that \(G_n-B\) has no isolated vertices and \(\gamma_{tR}(G_n-B)>\gamma_{tR}(G_n)\). Then \(\gamma_{tR}(G_n)=4\), and

\[
\boxed{F_{n,k}=[t^k]\sum_{j=0}^{n}(-1)^j\binom nj(1+t)^{(n-j)^2},\qquad 0\le k<n.}
\]

In particular, the total Roman bondage number is \(b_{tR}(G_n)=\lceil n/2\rceil\). The exact number \(M_n\) of distinct minimum-cardinality damaging deletion sets is

\[
\boxed{M_n=\begin{cases}\dfrac{n!}{(n/2)!},&n\ge4\ \text{even},\\[5pt]\dfrac{n^2(n-1)!}{((n-1)/2)!},&n\ge3\ \text{odd}.\end{cases}}
\]

For instance, the lists \((F_{n,0},\ldots,F_{n,n-1})\) for \(n=3,4,5,6\) are, respectively, \((0,0,18)\), \((0,0,12,248)\), \((0,0,0,300,4800)\), and \((0,0,0,120,7800,121212)\). The formula also supplies the exact conditional failure probability \(F_{n,k}/\binom{n^2}{k}\) under uniformly chosen \(k<n\) distinct edge deletions.

## Assumptions and scope

All graphs are finite, simple, undirected, and labelled. The clique prism has \(2n\) vertices, \(n^2\) edges and minimum degree \(n\). Distinct edge subsets are counted, without quotienting by graph automorphisms. Here the edge-failure enumeration only claims \(0\le k<n\), the largest deletion window in which the isolate-free requirement holds automatically. The degenerate prism \(G_2\cong C_4\) is excluded; its total Roman domination number equals its order and its total Roman bondage number is infinite.

## Proof

**Step 1: a weight-four characterization.** In any isolate-free graph \(H\) on at least six vertices with no universal vertex, \(\gamma_{tR}(H)\ge4\). Indeed, a feasible function of weight at most three must have a label \(2\) and, because positive support cannot be isolated, at least one neighboring positive vertex. If the weight is three, the positive labels must be \(2,1\), and every remaining vertex is zero and adjacent to the label-\(2\) vertex, making that vertex universal. Assignments without a label \(2\) would leave zeros undefended.

Furthermore, \(\gamma_{tR}(H)=4\) if and only if \(H\) contains an **adjacent dominating pair** \(uv\) with \(N_H[u]\cup N_H[v]=V(H)\). Such a pair supplies a weight-four function by giving both endpoints label \(2\) and all other vertices label \(0\). Conversely, consider a weight-four feasible function. Four labels \(1\) are impossible on at least six vertices, because there are zeros and no label \(2\). For two labels \(2\), those vertices must be adjacent and their closed neighborhoods cover all vertices. In the remaining case the positive labels are \(2,1,1\). The vertex \(v\) bearing \(2\) has a positive neighbor \(u\) bearing \(1\); every zero is adjacent to \(v\). The other label-\(1\) vertex is adjacent either to \(v\) or to \(u\), because positive support has no isolates. Thus \(vu\) is an adjacent dominating pair. This proves the characterization, including disconnected isolate-free graphs.

**Step 2: all surviving minimum defenders.** Every vertex of \(G_n\) has degree \(n<2n-1\), so no universal vertex exists. For \(n\ge3\), its adjacent dominating pairs are exactly the \(n\) rungs \(a_ib_i\). Every rung dominates both entire clique layers; an edge within the \(a\)-layer fails to dominate \(b_h\) for any third index \(h\), and similarly in the other layer. Removing edges cannot create an adjacent dominating pair. The pair \(a_ib_i\) remains adjacent and dominating in \(G_n-B\) precisely when \(B\) contains no edge incident with index \(i\), meaning neither a deleted rung \(a_ib_i\) nor a deleted clique edge incident with \(a_i\) or with \(b_i\). Since every vertex of \(G_n\) has degree \(n\), deleting fewer than \(n\) edges cannot isolate a vertex. Step 1 therefore gives an exact equivalence for \(k<n\): \(\gamma_{tR}(G_n-B)>4\) if and only if every index \(1,\ldots,n\) is touched by some deleted edge.

**Step 3: the complete low-deletion enumeration.** Regard a rung as covering one index and a clique edge as covering its two endpoint indices. For a fixed subset \(J\) of \(j\) indices required to be *untouched*, the permitted deleted edges lie entirely in the two cliques on the other \(n-j\) indices together with the corresponding rungs. There are \(2\binom{n-j}{2}+(n-j)=(n-j)^2\) such edges. Consequently the generating polynomial for those subsets is \((1+t)^{(n-j)^2}\). Inclusion-exclusion over untouched indices counts exactly those deletion sets touching every index, and coefficient extraction gives the displayed formula. The degree restriction from Step 2 makes every such deletion set admissible in the original isolate-free definition.

**Step 4: the sharp minimum and its multiplicity.** Each deleted edge covers at most two indices. Hence any damaging set has at least \(\lceil n/2\rceil\) edges, attainable by a matching of deleted clique edges and, for odd \(n\), one additional deleted rung. For \(n=2r\), a minimum damaging set consists of a perfect matching of the \(2r\) index labels, with each pair's edge deleted in either clique layer. Thus \(M_{2r}=2^r(2r)!/(2^r r!)=(2r)!/r!\).

For \(n=2r+1\), a minimum set has \(r+1\) edges. If it contains a rung, it contains exactly one rung, and the remaining \(r\) deletions are a perfect matching of the other indices: \((2r+1)(2r)!/r!\) choices. If it has no rung, the graph formed on the index labels by its \(r+1\) deleted clique edges has all degrees positive and degree sum \(2r+2\); it must be a three-vertex path plus \(r-1\) isolated matching edges. Choosing the triple, its middle vertex, a matching of the rest, and one of the two clique layers for each deleted edge yields \(3\binom{2r+1}{3}\cdot(2r-2)!/[2^{r-1}(r-1)!]\cdot2^{r+1}\) choices. This is \(2r\) times the number in the rung case. Adding both cases gives \(M_{2r+1}=(2r+1)^2(2r)!/r!\). No other minimum patterns are possible.

## Verification

The attached standalone \(\texttt{verify.py}\) independently enumerates all deleted edge sets of cardinality below \(n\) for \(n=3,4,5,6\): \(459723\) cases total. It compares their index-cover counts against the inclusion-exclusion coefficients and the closed minimum counts. Separately, for every deletion set of size below \(n\) when \(n=3,4\), it enumerates all \(\{0,1,2\}\)-valued vertex assignments and directly checks feasibility, confirming the adjacent-dominating-pair criterion on \(743\) graph instances. Running \(\texttt{python3 verify.py}\) produces the recorded \(\texttt{verify_output.txt}\). These checks are finite corroboration; Steps 1–4 prove all parameter values.

## Relationship to prior work

Khosh-Ahang Ghasr and Nazari-Moghaddam (2026) introduce and study total Roman bondage, prove that weight four coincides with the presence of an adjacent dominating pair under suitable hypotheses, and show equality with ordinary total bondage at that weight. This is the principal conceptual source. Its classes of exact results are complete graphs, complete bipartite graphs, wheels, brooms and wounded spiders. The present theorem does not claim those foundational criteria as new; its contribution is the complete *edge-deletion size distribution below minimum degree* for the different class of matched complete-clique prisms, with a parity-dependent count of minimum damaging sets.

Appel, Fischberg, Kelley, Shank and Sosis (2025) study \(k\)-total bondage and related edge failure constructions. The inspected path/cycle, wheel, clique and biclique theorems and construction section do not determine this total Roman edge-failure profile. A published record about Roman \(\{3\}\)-domination on the same prism graphs uses a different feasibility rule and does not imply the stated total Roman bond profile. Inclusion-exclusion and the perfect-matching counts are classical enumeration tools, not claimed as new independent facts.

## Limitations

The polynomial includes only deletion sizes \(k<n\). At \(k\ge n\), some deletions can isolate vertices, so the coefficient formula can overcount admissible total Roman bondage sets. No claim is made about the post-deletion value of \(\gamma_{tR}\) beyond its strict increase, or about unlabeled counts. Earlier literature under alternative total-bondage terminology or a dedicated clique-prism treatment could conceivably contain an equivalent count; no exhaustive bibliographic uniqueness claim or independent validation is made.

## References

1. F. Khosh-Ahang Ghasr and S. Nazari-Moghaddam, *Total Roman bondage number of a graph*, first public preprint 2026-02-09, arXiv:2602.08758, https://arxiv.org/abs/2602.08758.
2. J.-P. Appel, G. Fischberg, K. Kelley, N. Shank and E. Sosis, *The \(k\)-Total Bondage Number of a Graph*, first public preprint 2025-06-08, arXiv:2506.07000, https://arxiv.org/html/2506.07000v1.
3. J.-M. Xu, *On Bondage Numbers of Graphs: A Survey with Some Comments*, International Journal of Combinatorics 2013, DOI:10.1155/2013/595210.
