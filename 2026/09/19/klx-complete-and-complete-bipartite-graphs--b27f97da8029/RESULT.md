# Exact KLX numbers of complete and complete bipartite graphs

## Result

Let \(\operatorname{KLX}(G)\) be the kissing-loop crossing number introduced by Bourotte, Ducloz, Orponen, and Seki: the minimum, over ordered depth-first-search trees, of the maximum number of simultaneously open back edges. Let \(\operatorname{DTC}(G)\) denote their DFS-tree congestion, which counts only back edges crossing a tree edge.

For complete graphs, for every \(n\ge 2\),
\[
\boxed{\operatorname{KLX}(K_n)=\operatorname{DTC}(K_n)=\left\lfloor\frac{n^2}{4}\right\rfloor-1.}
\]

For complete bipartite graphs, write \(1\le a\le b\). If \(a=1\), then \(K_{a,b}\) is a tree and
\[
\operatorname{KLX}(K_{1,b})=\operatorname{DTC}(K_{1,b})=0.
\]
If \(a\ge2\), put
\[
\varepsilon_{a,b}=
\begin{cases}
1,&a=b\text{ and }a\text{ is odd},\\
0,&\text{otherwise}.
\end{cases}
\]
Then
\[
\boxed{
\operatorname{KLX}(K_{a,b})=\operatorname{DTC}(K_{a,b})=
\begin{cases}
\left\lfloor\dfrac{(a+b)^2}{8}\right\rfloor-1+\varepsilon_{a,b},& b\le 3a-2,\\[2mm]
(a-1)(b-a+2)-1,& b\ge 3a-1.
\end{cases}}
\]

In particular,
\[
\boxed{\operatorname{KLX}(K_{t,t})=\left\lfloor\frac{t^2-1}{2}\right\rfloor}
\]
and
\[
\boxed{\operatorname{KLX}(K_{2,b})=b-1.}
\]

The formula exhibits a genuine shape transition. When the two parts are not too imbalanced, the bottleneck is an approximately central cut of an alternating DFS spine. Once \(b\ge3a-1\), the maximizing cut is forced to the end of that spine.

## DFS-tree structure for a biclique

Let the bipartition be \(A\cup B\), with \(|A|=a\le b=|B|\). In every DFS tree of \(K_{a,b}\), any two incomparable vertices must lie in the same bipartition class, because every cross-part pair is adjacent.

Suppose a vertex \(x\in A\) has two children. They both lie in \(B\). If the subtree of one child contained another vertex of \(A\), that vertex would be adjacent to the other child, contradicting incomparability of distinct child subtrees in a DFS tree. Thus every child subtree of a branch vertex is a singleton. The same incomparability argument forces every vertex of \(A\) onto the root-to-branch path and every remaining vertex of \(B\) to be a leaf at the terminal \(A\)-vertex. Consequently, up to relabeling and reversal, every DFS tree has one of two forms.

A canonical optimal form roots in the larger part \(B\):
\[
b_1,a_1,b_2,a_2,\ldots,b_a,a_a
\]
is an alternating spine, and the remaining \(q=b-a\) vertices of \(B\) are leaf children of \(a_a\).

For the spine edge \(b_i a_i\), deleting it leaves a prefix with \(i\) vertices of \(B\) and \(i-1\) vertices of \(A\). Hence the number of crossing back edges is
\[
h_i=i(a-i+1)+(i-1)(b-i)-1
   =i(a+b+2-2i)-b-1,
\qquad 1\le i\le a.
\]
For the spine edge \(a_i b_{i+1}\),
\[
g_i=i(a+b-2i)-1,
\qquad 1\le i\le a-1.
\]
If the extra leaves are visited as \(c_1,\ldots,c_q\), then at the return edge \(c_j\to a_a\) exactly \(j(a-1)\) back edges from the first \(j\) leaves are open. The maximum leaf contribution is \((b-a)(a-1)\), and this is strictly dominated by the spine value
\[
h_a=(a-1)(b-a+1)
\]
when \(a>1\). Thus this ordered DFS tree has
\[
\operatorname{KLX}(T)=\max\left\{\max_{1\le i\le a}h_i,\ \max_{1\le i\le a-1}g_i\right\},
\]
and its maximum is already attained by crossing back edges, so \(\operatorname{DTC}(T)=\operatorname{KLX}(T)\).

If instead the root lies in \(A\), the analogous spine contains one fewer \(B\)-vertex and the remaining \(b-a+1\) vertices of \(B\) are leaves at its final \(A\)-vertex. Its corresponding first family of spine cuts is
\[
f_i=i(a+b+2-2i)-a-1=h_i+(b-a),
\qquad 1\le i\le a-1,
\]
while the \(g_i\) cuts are unchanged. Moreover, its last relevant spine cut dominates \(h_a\). Therefore rooting in \(B\) is never worse, and the displayed canonical tree is optimal for both KLX and DTC.

## Reduction to one concave quadratic

Let
\[
G(a,b)=\max_{1\le i\le a-1}g_i.
\]
For \(1\le i\le a-1\),
\[
h_i-g_i=2i-b,
\qquad
h_i-g_{i-1}=a-2i+2
\]
whenever the second comparison is defined, while
\[
h_a-g_{a-1}=2-a\le0.
\]
These comparisons imply that every \(h_i\) is dominated by one of the neighboring \(g\)-values, except in the unique parity case
\[
a=b\text{ odd},\qquad i=\frac{a+1}{2},
\]
where \(h_i=G(a,b)+1\). Hence
\[
\operatorname{KLX}(K_{a,b})=G(a,b)+\varepsilon_{a,b}.
\]

Now
\[
g_i=i(a+b-2i)-1
\]
is a concave quadratic. If \(b\le3a-2\), an unrestricted integer maximizer lies in \(1\le i\le a-1\), and
\[
G(a,b)=\left\lfloor\frac{(a+b)^2}{8}\right\rfloor-1.
\]
If \(b\ge3a-1\), the sequence is increasing throughout the allowed interval, so the maximum occurs at \(i=a-1\), giving
\[
G(a,b)=(a-1)(b-a+2)-1.
\]
This proves the biclique formula.

## Complete graphs

Every DFS tree of \(K_n\) is a Hamilton path: two vertices in different child subtrees would be incomparable but adjacent. Root the path as \(v_1,\ldots,v_n\). For the tree edge \(v_i v_{i+1}\), every graph edge crossing the cut
\[
\{v_1,\ldots,v_i\}\mid\{v_{i+1},\ldots,v_n\}
\]
is open on the return traversal, except the tree edge itself. Therefore
\[
|\mathcal O(v_iv_{i+1})|=i(n-i)-1.
\]
Maximizing over \(i\) yields
\[
\operatorname{KLX}(K_n)=\left\lfloor\frac{n^2}{4}\right\rfloor-1.
\]
Again the maximum consists entirely of crossing back edges, so \(\operatorname{DTC}(K_n)=\operatorname{KLX}(K_n)\).

## Separation from ordinary spanning-tree congestion

Classical spanning-tree congestion minimizes over all spanning trees and counts the tree edge itself in each cut. Bourotte et al. note that DTC is the same cut quantity restricted to DFS trees, adjusted by \(-1\). Since DTC equals KLX on the families above, the DFS-restricted classical congestion is exactly \(\operatorname{KLX}+1\).

Known formulas give
\[
\operatorname{stc}(K_n)=n-1,
\qquad
\operatorname{stc}(K_{a,b})=a+b-2\quad(a,b\ge2).
\]
Thus
\[
\operatorname{stc}_{\rm DFS}(K_n)=\left\lfloor\frac{n^2}{4}\right\rfloor,
\]
and, for balanced bicliques,
\[
\operatorname{stc}_{\rm DFS}(K_{t,t})
=\left\lceil\frac{t^2}{2}\right\rceil,
\qquad
\operatorname{stc}(K_{t,t})=2t-2.
\]
Hence imposing the DFS constraint can increase optimal spanning-tree congestion by a factor of order \(t\), even on the highly symmetric families \(K_n\) and \(K_{t,t}\).

## Verification

A standalone verifier enumerates spanning trees, roots, and child orders directly from the KLX definition for small complete bipartite graphs, rejecting rooted trees that are not DFS trees. It independently evaluates the arc intervals of every non-tree edge and minimizes the resulting maximum number of open back edges. It also checks all rooted Hamilton-path orders for \(K_2,\ldots,K_8\). The checked instances agree with the formulas.

Finite verification is supporting evidence only; the result is proved above for all parameters.

## Literature position

Bourotte, Ducloz, Orponen, and Seki introduced and developed KLX in 2026, defining open back edges and proving structural characterizations for \(\operatorname{KLX}\le1\) and \(\operatorname{KLX}\le2\), together with \(\operatorname{TW}(G)\le\operatorname{KLX}(G)+1\) and fixed-parameter recognition results. The accessible current full text was inspected; no exact formula for complete graphs or complete bipartite graphs was found.

The older spanning-tree-congestion literature does determine ordinary congestion for complete and complete multipartite graphs, but that optimization ranges over arbitrary spanning trees. It therefore does not determine KLX, whose feasible trees are DFS trees and whose objective also accounts for ordered enveloping back edges. The exact formulas above resolve this distinction explicitly and show an unbounded asymptotic penalty for the DFS restriction.

To the best of our knowledge, searches for KLX/kissing-loop crossing, DFS-tree congestion, Trémaux-tree congestion, normal-spanning-tree congestion, open-back-edge congestion, and complete/complete-bipartite specializations found no equivalent formulas or stronger result. Because KLX is a recent parameter, very recent unindexed parallel work remains a residual originality risk.

### References

- C. Bourotte, G. Ducloz, P. Orponen, and S. Seki, *A Congestion Parameter for Depth-First Graph Traversals*, MFCS 2026, DOI: https://doi.org/10.4230/LIPIcs.MFCS.2026.7 ; arXiv: https://arxiv.org/abs/2606.24675
- K. Kozawa, Y. Otachi, and K. Yamazaki, *On spanning tree congestion of graphs*, Discrete Mathematics 309 (2009), 4215--4224, DOI: https://doi.org/10.1016/j.disc.2008.12.021
- Y. Otachi, survey material summarizing exact complete and complete-bipartite spanning-tree congestion formulas: https://www.jstage.jst.go.jp/article/iis/17/3/17_3_197/_pdf
