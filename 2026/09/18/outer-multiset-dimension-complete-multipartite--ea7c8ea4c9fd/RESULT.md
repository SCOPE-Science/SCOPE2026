# Outer multiset dimension of arbitrary complete multipartite graphs

## Statement

Let
\[
G=K_{n_1,\ldots,n_r},\qquad r\ge 2,\quad n_i\ge 1,
\]
be a connected complete multipartite graph, let
\[
n=\sum_{i=1}^r n_i,
\]
and let
\[
d=\bigl|\{n_1,\ldots,n_r\}\bigr|
\]
be the number of distinct part sizes. Then
\[
\boxed{\operatorname{dim}_{\mathrm{ms}}(G)=n-d.}
\]
Here \(\operatorname{dim}_{\mathrm{ms}}\) denotes the outer multiset dimension.

There is also an exact characterization of every outer multiset resolving set. If the multipartite parts are \(V_1,\ldots,V_r\), then a set \(S\subseteq V(G)\) is outer multiset resolving if and only if:

1. \(V_i\setminus S\) has size at most one for every \(i\); and
2. whenever \(V_i\setminus S\) and \(V_j\setminus S\) are both nonempty with \(i\ne j\), one has \(n_i\ne n_j\).

Consequently, if \(M\) is the set of distinct part sizes and \(c_m\) is the number of parts of size \(m\), then the number of outer multiset bases is
\[
\boxed{\prod_{m\in M} c_m m.}
\]
More generally, the number of outer multiset resolving sets whose complement has exactly \(k\) vertices is
\[
e_k\bigl((c_m m)_{m\in M}\bigr),\qquad 0\le k\le d,
\]
where \(e_k\) is the \(k\)-th elementary symmetric polynomial.

Equivalently, since a vertex in a part of size \(m\) has degree \(n-m\), the dimension formula can be written as
\[
\operatorname{dim}_{\mathrm{ms}}(G)=n-|\deg(G)|,
\]
where \(|\deg(G)|\) is the number of distinct vertex degrees occurring in \(G\).

## Proof

Let \(S\subseteq V(G)\), and write
\[
s_i=|S\cap V_i|.
\]
For a vertex \(v\in V_i\setminus S\), every landmark in \(V_i\) is at distance \(2\) from \(v\), while every landmark outside \(V_i\) is at distance \(1\). Hence
\[
m(v\mid S)=\{\!\{1^{|S|-s_i},2^{s_i}\}\!\}.
\]
Thus all vertices of \(V_i\setminus S\) have the same multiset representation. Therefore an outer multiset resolving set must leave at most one vertex outside \(S\) in each part.

Suppose now that exactly one vertex is omitted from each of two distinct parts \(V_i,V_j\). Then
\[
s_i=n_i-1,\qquad s_j=n_j-1.
\]
The two omitted vertices have equal multiset representations if and only if \(s_i=s_j\), which is equivalent to \(n_i=n_j\). This proves the necessity of the two conditions in the characterization.

Conversely, suppose those two conditions hold. Every vertex outside \(S\) lies in a different omitted part, and the omitted parts have pairwise distinct sizes. For omitted vertices from parts \(V_i\) and \(V_j\), the multiplicities of distance \(2\) are \(n_i-1\) and \(n_j-1\), respectively, and hence are distinct. Their multiset representations are therefore distinct. So \(S\) is outer multiset resolving, proving the characterization.

The complement of any outer multiset resolving set can therefore contain at most one vertex from each part-size class, so it has at most \(d\) vertices. Hence
\[
|S|\ge n-d.
\]
For the reverse inequality, choose one multipartite part for each distinct part size and omit one arbitrary vertex from each chosen part. The characterization shows that the remaining \(n-d\) vertices form an outer multiset resolving set. Thus \(\operatorname{dim}_{\mathrm{ms}}(G)=n-d\).

For a basis, equality forces one omitted vertex from exactly one part in every distinct-size class. For each size \(m\), there are \(c_m\) choices of the part and then \(m\) choices of the omitted vertex, giving \(\prod_{m\in M} c_m m\) bases. The same bijection with subsets of distinct size classes gives the elementary-symmetric count for resolving sets with a prescribed complement size.

## Relation to known results

Gil-Pons, Ramírez-Cruz, Trujillo-Rasua, and Yero introduced the outer multiset dimension in 2019 and, among other results, treated balanced complete multipartite graphs. Klavžar, Kuziak, and Yero (2023) explicitly record
\[
\operatorname{dim}_{\mathrm{ms}}(K_{m,\ldots,m})=km-1
\]
for balanced complete \(k\)-partite graphs and also note that when all part sizes satisfy
\[
2\le r_1<r_2<\cdots<r_k,
\]
one has
\[
\operatorname{dim}_{\mathrm{ms}}(K_{r_1,\ldots,r_k})=r_1+\cdots+r_k-k.
\]
The theorem above closes the intermediate regime in which some, but not all, part sizes repeat. It also classifies all outer multiset resolving sets and counts the bases. For example,
\[
\operatorname{dim}_{\mathrm{ms}}(K_{2,2,3,5,5})=17-3=14.
\]
The twin-class lower bound alone gives only \(17-5=12\) here; the extra obstruction comes from equal multiset representations of omitted vertices in different parts of equal size.

The 2025 study of joined graphs computes stars, wheels, generalized wheels, windmills, fans, and generalized fans, but does not state the arbitrary complete-multipartite formula. A 2026 survey of multiset dimension variants lists the balanced complete multipartite value, again leaving the partially repeated part-size regime unstated. A September 2026 paper on toroidal grids provides a recent exact determination for another major graph family, illustrating continuing activity around the parameter.

## Verification

The proof is exact and does not rely on computation. As a finite sanity check from the definitions, every nondecreasing complete-multipartite part-size tuple of total order from 2 through 8 was exhaustively tested over all landmark subsets. The full resolving-set characterization, the dimension formula, and the basis-count formula held for all 58 multipartite types checked.

## Limitations and originality

Originality is asserted only to the best of our knowledge. The closest primary source inspected in detail is Klavžar--Kuziak--Yero (2023), whose complete-multipartite discussion states the balanced case and the pairwise-distinct-size case but not the mixed-multiplicity case. The full 2025 joined-graphs paper was also inspected; its stated families do not include arbitrary complete multipartite graphs. The 2026 survey was inspected for its outer-multiset table and likewise lists only the balanced complete multipartite case.

The accessible full text of the 2019 foundational paper was inspected at its complete multipartite proposition: Proposition 3.4 assumes all part sizes are equal and proves the balanced value. No arbitrary mixed-multiplicity formula or resolving-set classification was found there. The resolving-set characterization and basis enumeration were also not found in the other checked sources. No material inaccessible source was identified among the closest references; very recent or poorly indexed parallel work remains the main residual originality risk.

## References

1. R. Gil-Pons, Y. Ramírez-Cruz, R. Trujillo-Rasua, I. G. Yero, *Distance-based vertex identification in graphs: The outer multiset dimension*, Applied Mathematics and Computation 363 (2019), 124612. https://doi.org/10.1016/j.amc.2019.124612 ; https://arxiv.org/abs/1902.03017
2. S. Klavžar, D. Kuziak, I. G. Yero, *Further Contributions on the Outer Multiset Dimension of Graphs*, Results in Mathematics 78 (2023), 50. https://doi.org/10.1007/s00025-022-01829-8 ; https://arxiv.org/abs/2207.06834
3. H. Pervaiz, R. Simanjuntak, S. W. Saputro, *Outer Multiset Dimension of Joined Graphs*, Indonesian Journal of Combinatorics 9 (2025), 61--68. https://doi.org/10.19184/ijc.2025.9.2.1
4. A. Albejani, Y. Lin, J. Ryan, K. A. Sugeng, *A Survey on Multiset Dimension and Its Variations*, arXiv:2607.08128 (2026). https://arxiv.org/abs/2607.08128
5. B. Peng, *The Outer Multiset Dimension of Toroidal Grids*, arXiv:2609.20073 (2026). https://arxiv.org/abs/2609.20073
