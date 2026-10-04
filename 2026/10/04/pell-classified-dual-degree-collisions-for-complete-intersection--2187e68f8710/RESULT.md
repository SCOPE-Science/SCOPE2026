# Pell-classified dual-degree collisions for complete-intersection space curves
## Finding
Let \(C_{d,e}\subset\mathbb P^3_{\mathbb C}\) be a smooth complete intersection of surfaces of degrees \(d,e\ge2\), and write \(\Delta(d,e)=\deg(C_{d,e}^{\vee})\) for the degree of its projective-dual surface. Then
\[
\Delta(d,e)=de(d+e-2).
\]
Among the two one-parameter families \(C_{2,m}\) and \(C_{3,n}\), all equal-dual-degree pairs are classified by one Pell equation. If
\[
x_k+u_k\sqrt{24}=(5+\sqrt{24})^k,\qquad k\ge1,
\]
then
\[
m_k=3u_k,\qquad n_k=\frac{x_k-1}{2}
\]
gives \(\Delta(2,m_k)=\Delta(3,n_k)\), and every solution with \(m,n\ge2\) occurs uniquely this way. The first Pell solution, \((m_1,n_1)=(3,2)\), merely reverses the same unordered bidegree \(\{2,3\}\). Every \(k\ge2\) gives genuinely distinct complete-intersection types. The first two nontrivial collisions are
\[
(2,30)\ \text{versus}\ (3,24),\qquad \Delta=1800,
\]
and
\[
(2,297)\ \text{versus}\ (3,242),\qquad \Delta=176418.
\]
Thus the degree of the projective dual does not determine the bidegree of a smooth complete-intersection space curve, even after restricting to these two basic families; in fact there are infinitely many such collisions. Along them,
\[
\frac{m_k}{n_k}\longrightarrow\sqrt{\frac32}.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). Curves are smooth complete intersections in \(\mathbb P^3\), so they are nondegenerate and their dual varieties are surfaces. The statement classifies only collisions between types \((2,m)\) and \((3,n)\); it does not claim a classification of all pairs of complete-intersection bidegrees having equal dual degree.

## Proof
Let \(C\subset\mathbb P^3\) be a smooth nondegenerate curve of degree \(\delta\) and genus \(g\). Choose a general line \(L\) disjoint from \(C\). The pencil of planes through \(L\) induces a morphism \(f:C\to\mathbb P^1\) of degree \(\delta\). A member of the pencil is tangent to \(C\) exactly when the corresponding point of \(C\) is a ramification point of \(f\). For a general pencil, intersection with the dual surface counts this ramification divisor with its natural multiplicities. Riemann--Hurwitz therefore gives
\[
\deg(C^{\vee})=\deg R_f=2g-2+2\delta.
\]
For a complete intersection \(C_{d,e}\), adjunction gives
\[
\delta=de,\qquad 2g-2=de(d+e-4).
\]
Hence
\[
\Delta(d,e)=de(d+e-2).
\]
In particular,
\[
\Delta(2,m)=2m^2,\qquad \Delta(3,n)=3n(n+1).
\]
Suppose these are equal. Then
\[
2m^2=3n(n+1).
\]
Reducing modulo \(3\) shows \(3\mid m\); write \(m=3u\). The equality becomes \(n(n+1)=6u^2\). Setting \(x=2n+1\) gives
\[
x^2-24u^2=1.
\]
Conversely, every positive integral solution of this Pell equation has odd \(x\), so \(n=(x-1)/2\) and \(m=3u\) are positive integers satisfying the original equality. The fundamental positive solution of \(x^2-24u^2=1\) is \((x,u)=(5,1)\), and the classical Pell theorem gives all positive solutions uniquely as
\[
x_k+u_k\sqrt{24}=(5+\sqrt{24})^k,\qquad k\ge1.
\]
This proves the classification. The first solution has \((m,n)=(3,2)\), hence the same unordered type. Since the sequences are strictly increasing, every later solution gives distinct types. Finally \(x_k/u_k\to\sqrt{24}\), so
\[
\frac{m_k}{n_k}=\frac{6u_k}{x_k-1}\longrightarrow\frac6{\sqrt{24}}=\sqrt{\frac32}.
\]

## Verification
The accompanying exact-integer checker generates Pell solutions, evaluates the dual-degree formula, verifies the recurrences, and independently brute-forces all \(2\le m,n\le5000\). The only collisions in that box are \((m,n)=(3,2),(30,24),(297,242),(2940,2400)\), exactly those produced by the Pell parametrization. This finite computation is regression evidence only; the infinite classification follows from the proof above.

## Relationship to prior work
Projective duality and tangency are classical; Wallace's 1956 paper is an early systematic source. Ilten and Len study tangential and dual varieties of complete-intersection curves and explicitly develop methods for computing their degrees. Their article treats the dual-degree problem itself but does not state the cross-bidegree Pell collision classification above. Searches for the exact equality \(2m^2=3n(n+1)\), its Pell form \(x^2-24u^2=1\), the first nontrivial collision \((2,30)\) versus \((3,24)\), and semantic aliases of complete-intersection dual-degree collisions did not locate a prior algebraic-geometric statement of this classification.

## Limitations
The result concerns equality of the numerical degree of the dual surfaces, not equality or projective equivalence of the dual surfaces themselves. The colliding curves have different ordinary degrees and, from the second Pell solution onward, different genera as well. No assertion is made about collisions involving two arbitrary bidegrees outside the two families considered here. Historical literature on projective duality is extensive, so an unindexed older arithmetic observation remains a residual literature risk.

## References
1. A. H. Wallace, *Tangency and Duality Over Arbitrary Fields*, Proceedings of the London Mathematical Society, s3-6 (1956), 321--342. DOI: 10.1112/plms/s3-6.3.321.
2. N. Ilten and Y. Len, *Tropical tangents for complete intersection curves*, arXiv:2104.15059, first posted 2021-04-30.
