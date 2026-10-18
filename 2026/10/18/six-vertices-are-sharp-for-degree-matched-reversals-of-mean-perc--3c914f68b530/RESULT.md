# Six vertices are sharp for degree-matched reversals of mean percolation outbreak size

## Finding

For a finite connected simple undirected graph \(G\) with \(n\) vertices, independently retain every edge with probability \(p\), select a seed vertex uniformly, and let \(X_G(p)\) be the number of vertices in its retained connected component. Put \(M_G(p)=\mathbb E[X_G(p)]\).

**Sharp threshold.** If connected graphs \(G,H\) each have at most five vertices and have the same degree multiset, then \(M_G(p)-M_H(p)\) has a constant sign for every \(0<p<1\) (the zero function is allowed). Six vertices suffice for a strict reversal.

In particular, take \(G\) to be a four-cycle with a two-edge pendant path attached at one cycle vertex, and \(H\) to be a five-cycle with one pendant leaf. Both have degree multiset \((1,2,2,2,2,3)\), six edges, and no triangles. For all \(0\le p\le1\),

\[
M_G(p)-M_H(p)=\frac{p^3(1-p)}3\bigl(1-8p-p^2\bigr).
\]

Therefore the mean outbreak is strictly larger on \(G\) when \(0<p<\sqrt{17}-4\), but strictly larger on \(H\) when \(\sqrt{17}-4<p<1\). The two curves agree at \(p=0\), \(p=\sqrt{17}-4\), and \(p=1\). The interior crossing is unique. The threshold of six vertices is exact for connected simple contact graphs.

## Assumptions and scope

Edges are independently open with common probability \(p\); a single uniformly random initial vertex reaches precisely its open component. This is a bond-percolation transmission model, not a claim that all continuous-time stochastic SIR models have independent undirected per-edge transmissions. Graphs are finite, simple, undirected, and connected; degree equivalence is equality of multisets, not equality of labeled degrees. The expectation counts the seed itself. For the sharpness statement, both graphs have equal order at most five; connectedness is required. Endpoints \(p=0,1\) are not treated as interior reversals.

## Proof

For a retained edge subset \(F\subseteq E(G)\), write \(\mathcal C(F)\) for the connected components of the spanning subgraph \((V(G),F)\). Conditional on \(F\), a uniform seed lands in a component of size \(|C|\) with probability \(|C|/n\), so

\[
M_G(p)=\frac1n\sum_{F\subseteq E(G)}\left(\sum_{C\in\mathcal C(F)}|C|^2\right)
 p^{|F|}(1-p)^{|E(G)|-|F|}.
\]

This exact finite polynomial requires no independence assumption beyond the open-edge indicators. It is also equal to \(1+(2/n)\sum_{u<v}\Pr_p(u\leftrightarrow v)\).

**Lower bound by complete classification.** For each \(1\le n\le5\), list every subset of the \(\binom n2\) possible undirected edges, retain only connected graphs, and identify graphs up to each of the \(n!\) vertex permutations. There are respectively \(1,1,2,6,21\) connected isomorphism classes. All degree multisets are uniquely realized in these classes, except exactly two degree multisets, both at order five:

\[
(1,2,2,2,3),\qquad (2,2,2,3,3).
\]

Each has exactly two connected isomorphism classes. For their respective pairs, the absolute differences in \(M\) are

\[
\frac25p^3(1-p)(p+5),\qquad
\frac25p^3(1-p)^2(p+5).
\]

Each is strictly positive on \(0<p<1\). Thus no pair of connected graphs of order at most five with the same degrees can exhibit a strict ranking reversal. This classification is exhaustive because every labeled graph is included, every permutation is considered, and the exact sums above are evaluated over every edge state. The finite classification is reproduced by the standalone verifier.

**Six-vertex witness.** With vertices labeled \(0,\ldots,5\), use the edge sets

\[
E(G)=\{(0,4),(0,5),(1,3),(1,4),(2,3),(2,4)\},
\]
\[
E(H)=\{(0,1),(0,4),(1,2),(1,5),(2,3),(3,4)\}.
\]

For \(k=0,\ldots,6\), let \(a_k(G)\) be the sum of \(\sum_C|C|^2\) over all open-edge subsets of size \(k\). Direct disjoint-set enumeration gives

\[
(a_0(G),\ldots,a_6(G))=(6,48,164,312,338,190,36),
\]
\[
(a_0(H),\ldots,a_6(H))=(6,48,164,310,350,206,36).
\]

Substituting these integer lists in the displayed expectation and expanding gives

\[
6M_G(p)=6+12p+14p^2+16p^3-4p^4-2p^5-6p^6,
\]
\[
6M_H(p)=6+12p+14p^2+14p^3+14p^4-16p^5-8p^6.
\]

Their difference factors as claimed. A separate derivation checks the polynomials using two-terminal connectivity: in a unicyclic graph with cycle length \(c\), if distinct vertices attach to cycle sites at clockwise arc distances \(d\) and \(c-d\), and their respective branch-to-cycle paths have lengths \(s,t\), then

\[
\Pr_p(u\leftrightarrow v)=p^{s+t}(p^d+p^{c-d}-p^c).
\]

The two arcs have disjoint edge sets, and the shared branch paths must all be open. Vertices in one pendant path are connected exactly when their unique tree path is open. Summing these probabilities over the fifteen vertex pairs gives the same two polynomials. Finally, \(1-8p-p^2\) decreases strictly from \(1\) to \(-8\) on \([0,1]\), with unique zero \(\sqrt{17}-4\) in \((0,1)\).

## Verification

Run `python3 verify.py` from this folder. The script requires only Python's standard library, enumerates **all** labeled simple graphs up to five vertices, computes graph isomorphism canonically by exhaustive permutations, checks the two exceptional degree profiles and their fixed-sign differences, and independently calculates the six-vertex witness through edge-state enumeration and the unicyclic pair-path identity. Standard output must match the included `certificate.json` after stripping its final newline. The labeled connected graph counts are \(1,1,4,38,728\) for orders one through five.

## Relationship to prior work

Moore and Newman (2000) use bond-percolation clusters as an explicit model of outbreak sizes; no claim of introducing that model is made here. Kenah and Robins (2007) establish why generic SIR models with nondegenerate infectious periods do **not** share a full undirected bond-percolation outbreak law; hence this finding is strictly scoped to independent retained edges. Miller (2009) and Stegehuis–Peron (2021) analyze effects of clustering and fixed degree information in epidemic/percolation networks, largely through asymptotic or large-network techniques. The precise finite six-vertex minimality, the pair of triangle-free degree-matched witnesses, and their unique exact interior crossing are not consequences of those reported results. Earlier unpublished tables or differently named reliability-polynomial results remain a bibliographic uncertainty.

## Limitations

No conclusion is drawn about nonuniform edge transmissibility, heterogeneous infectious periods, multiple seeds, directed transmission, adaptive contact changes, disconnected graphs, or networks constrained by a fixed labeled degree sequence. This exact finite cutoff is not a universal asymptotic law or a claim about all epidemiological mechanisms. Graph-polynomial and reliability literature may contain equivalent finite examples under another name; independent priority review is not performed.

## References

- Moore, C., and Newman, M. E. J. (2000). *Exact solution of site and bond percolation on small-world networks*. arXiv:cond-mat/0001393v1 (first posted January 26, 2000). https://arxiv.org/html/cond-mat/0001393v1
- Kenah, E., and Robins, J. M. (2007). *Second look at the spread of epidemics on networks*. Physical Review E 76, 036113. https://pmc.ncbi.nlm.nih.gov/articles/PMC2215389/
- Miller, J. C. (2009). *Spread of infectious diseases through clustered populations*. Journal of the Royal Society Interface. https://pmc.ncbi.nlm.nih.gov/articles/PMC2817154/
- Stegehuis, C., and Peron, T. (2021). *Network processes on clique-networks with high average degree: the limited effect of higher-order structure*. arXiv:2104.14776v1. https://arxiv.org/html/2104.14776v1
