# Tight-component formula for faces of finite bounded-Lipschitz balls

## Finding
Let \(S\) be a nonempty finite metric space and equip the real vector space of functions \(f:S\to\mathbb R\) with the bounded-Lipschitz norm
\[
N(f)=\max_{i\in S}|f_i|+\max_{i\ne j}\frac{|f_i-f_j|}{d(i,j)},
\]
with the second maximum defined as zero when \(|S|=1\). Let \(B=\{f:N(f)\le1\}\).

For any nonconstant boundary point \(f\) of \(B\), put \(a=\max_i|f_i|>0\), \(L=\max_{i\ne j}|f_i-f_j|/d(i,j)>0\), so \(a+L=1\). Mark as *anchors* the vertices \(i\) with \(|f_i|=a\), giving each its sign \(\operatorname{sgn}(f_i)\). Define the *tight-edge graph* \(G_f\) on all of \(S\), with edge \(\{i,j\}\) exactly when \(|f_i-f_j|=L\,d(i,j)\). Let \(u\) be the number of components of \(G_f\) that contain no anchor. Let \(\varepsilon=0\) if one component contains both a positive and a negative anchor, and \(\varepsilon=1\) otherwise.

**Theorem.** The smallest face of \(B\) containing \(f\) has affine dimension
\[
\boxed{\dim F_B(f)=u+\varepsilon.}
\]
Consequently, a nonconstant unit vector \(f\) is an extreme point **if and only if** every connected component of its tight-edge graph contains an anchor and at least one component contains anchors of both signs. The remaining extreme points are exactly the two constant functions \(f\equiv1\) and \(f\equiv-1\). A point with \(N(f)<1\) is not extreme.

Given the input metric and a boundary function, the graph criterion and face dimension are computed with \(O(|S|^2)\) arithmetic comparisons and a graph traversal. This holds without geodesicity, graph-metric assumptions, or rationality of distances.

## Assumptions and scope
The scalars are real, and \(d\) is a genuine metric on a nonempty **finite** set. Every distinct-point distance is positive; no assertion is made for pseudometrics with unidentified zero-distance points, infinite spaces, or the separate Fortet–Mourier maximum norm. The formula applies to every nonconstant point of the norm-one sphere. For \(|S|=1\), the unit ball is an interval and only its two endpoints are extreme.

## Proof
Write \(n=|S|\). The one-point case follows immediately. Suppose \(n\ge2\). For every function \(g\), since maxima in its two norm components are independently attained,
\[
N(g)=\max_{i,\sigma\in\{-1,1\},\,p\ne q}\left[\sigma g_i+\frac{g_p-g_q}{d(p,q)}\right].
\]
Thus \(B\) is a full-dimensional polytope described by those finitely many linear inequalities, each with right side \(1\). At a boundary point the affine hull of its smallest face is the simultaneous equality set of precisely the active inequalities: inactive inequalities have strict slack at the point, so sufficiently small positive and negative displacements in the nullspace remain feasible.

Assume \(N(f)=1\) and \(L>0\). The active inequalities at \(f\) are *exactly* the products of a signed anchor \((i,\sigma)\), where \(\sigma f_i=a\), and an oriented tight edge \((p,q)\), where \(f_p-f_q=Ld(p,q)\). Therefore, a displacement \(h\) is tangent to the minimal face precisely when
\[
\sigma h_i+\frac{h_p-h_q}{d(p,q)}=0
\quad\text{for all such anchors and oriented edges.}
\]
There is at least one anchor and one tight edge. Fix one oriented tight edge and compare its equations for all anchors, and then fix one anchor and compare its equations for all oriented tight edges. This yields a common scalar \(r\) with
\[
\sigma h_i=r\ \text{at every anchor},\qquad
h_p-h_q=-r\,d(p,q)=-\frac{r}{L}(f_p-f_q)
\ \text{on every tight edge}.
\]
For every tight-graph component \(C\), including isolated vertices, the edge relations are equivalent to
\[
h_j=-\frac rL f_j+c_C\qquad(j\in C)
\]
for a component-specific constant \(c_C\). If \(C\) contains a positive anchor, substituting \(f_i=a\), \(h_i=r\) gives \(c_C=r(1+a/L)=r/L\) because \(a+L=1\). A negative anchor similarly imposes \(c_C=-r/L\). An anchorless component has one free \(c_C\). If any component contains both anchor signs, its two requirements force \(r=0\); otherwise \(r\) is free. All these relations are also sufficient for every active equality. Hence the nullity of the active-inequality matrix equals \(u+\varepsilon\). This is precisely the affine dimension of the smallest face.

A point of a polytope is extreme exactly when its smallest face is zero-dimensional, proving the equivalence. If \(L=0\) and \(N(f)=1\), the function is identically \(1\) or \(-1\). Each is extreme: all feasible functions satisfy \(|g_i|\le1\), so a convex average attaining the value \(1\) (or \(-1\)) at every coordinate forces both summands to be the same constant function. Finally, if \(N(f)<1\), a small line segment through \(f\) lies in \(B\), so \(f\) is not extreme. \(\square\)

## Verification
The accompanying standalone `verify_bl_graph.py` uses exact rational arithmetic to recompute the rank of the complete family of active inequality normals and compares its nullity with the tight-component expression. It passed 46,000 normalized boundary configurations on random weighted shortest-path metrics and interval metrics, including the two opposing four-point examples in Hille–Theewis (2023, Section 6). The first is correctly classified extreme, the second non-extreme. These tests corroborate the algebraic proof but are not a substitute for its universal argument.

A concrete boundary case illustrating the criterion's nuance has three vertices, values \((1/3,-1/3,1/3)\), and distances \(d(1,2)=1\), \(d(1,3)=d(2,3)=5\). Its tight graph has one edge and an isolated vertex, yet the point is extreme because both graph components are anchored and the edge component has opposite-sign anchors.

## Relationship to prior work
Hille and Theewis (2023, Section 6) give necessary finite-space conditions and show by explicit four-point examples that a proposed local edge-saturation condition is insufficient. Their stated problem concerns precisely the sum norm treated here. Hille and Theewis (2022, Lemma 6.1) supply a finite half-space description and a linear-programming route for the dual norm but no connected-component formula for the dimension of *every* face. Bredies, Chirinos Rodriguez and Naldi (2023, Section 2) characterize extreme points for the *pure* Lipschitz seminorm with a pinned base point (and strict-convexity hypotheses on the range); the supremum-norm term and its opposing-anchor coupling are absent. The new criterion is not the assertion that the entire tight graph is connected and does not follow from the other norm's connectedness criterion.

## Limitations
The theorem is finite-dimensional and real. Although elementary polyhedral linear algebra gives an active-constraint rank test in principle, the specific graph-component formula and complete necessary-and-sufficient extreme-point criterion are the claimed contribution. An equivalent characterization in earlier or unindexed work remains a bibliographic risk. The checker samples finitely many rational metrics/functions and does not certify the infinite family of inputs or establish novelty. No independent audit has been performed.

## References
1. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500v1 (first public 2023-05-15), Section 6. https://arxiv.org/html/2305.08500v1
2. S. C. Hille and E. S. Theewis, *Explicit expressions and computational methods for the Fortet–Mourier distance to finite weighted sums of Dirac measures*, arXiv:2206.12234v2, Section 6 and Lemma 6.1. https://arxiv.org/html/2206.12234v2
3. K. Bredies, M. Chirinos Rodriguez, and G. Naldi, *On extreme points and representer theorems for the Lipschitz unit ball on finite metric spaces*, arXiv:2304.14039v1 (2023), Section 2. https://arxiv.org/html/2304.14039v1
