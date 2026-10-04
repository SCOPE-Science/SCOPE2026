# Uniqueness of the centered distance ellipsoid for the Gaussian zonoid
## Finding
For every integer \(n\ge 3\), let \(Z_n\subset\mathbb R^{n-1}\times\mathbb R\) be the Gaussian zonoid of Ryabogin and Zvavitch, with support function
\[
h_{Z_n}(x,t)=\mathbb E\left|\langle x,\Gamma_{n-1}\rangle+t\right|,
\]
where \(\Gamma_{n-1}\) is centered Gaussian with covariance \((\pi/2)I_{n-1}\). Let
\[
F_1(s)=\frac{\phi(s)}{\sqrt{1+s^2}},\qquad \phi(s)=\mathbb E|\gamma+s|,
\]
with \(\gamma\sim N(0,\pi/2)\), and let \(b_\infty=\min_{s\ge0}F_1(s)\). The minimum occurs at a unique \(s_0>0\), and \(0<b_\infty<1\).

If an origin-centered ellipsoid \(E\) satisfies
\[
E\subset Z_n\subset b_\infty^{-1}E,
\]
then necessarily
\[
E=b_\infty B_2^n.
\]
Thus the Euclidean homothety class is the unique origin-centered distance-ellipsoid class attaining
\[
d_{BM}(Z_n,B_2^n)=b_\infty^{-1}.
\]

## Assumptions and scope
The statement concerns the centrally symmetric Banach--Mazur problem in its linear, origin-centered form. No assertion is made about translated ellipsoid pairs in a nonsymmetric formulation. The restriction \(n\ge3\) isolates the genuinely higher-dimensional case; planar symmetric distance ellipsoids are already known to be unique by general theory.

The proof uses two facts established for \(Z_n\) in arXiv:2609.10852v1: the symmetry group \(G=O(n-1)\times\{\pm1\}\) may be used to average the quadratic form of any competing ellipsoid without worsening its sandwich factor, and among \(G\)-invariant ellipsoid shapes the Euclidean shape is the unique optimizer. The latter follows from the strict inequalities in the two cases \(\alpha>1\) and \(0<\alpha<1\) in the proof of Theorem 5.3.

## Proof
Write the support-square of \(E\) as
\[
q(u)=h_E(u)^2=u^{\mathsf T}Qu,
\]
where \(Q\) is positive definite. The assumed sharp sandwich is equivalent to
\[
b_\infty^2 h_{Z_n}(u)^2\le q(u)\le h_{Z_n}(u)^2
\]
for every \(u\in\mathbb R^n\).

Average \(q\) over \(G\) with normalized Haar measure:
\[
\bar q(u)=\int_G q(gu)\,d\mu(g).
\]
Because \(h_{Z_n}(gu)=h_{Z_n}(u)\), the same two inequalities hold with \(q\) replaced by \(\bar q\). Hence \(\bar q\) is the support-square of a \(G\)-invariant ellipsoid attaining the sharp factor \(b_\infty^{-1}\).

Every \(G\)-invariant ellipsoid, after removing an irrelevant common scale, has support-square
\[
|x|^2+\alpha t^2,
\]
with \(\alpha>0\). In the proof of Theorem 5.3 of arXiv:2609.10852v1, if \(\alpha>1\), the corresponding comparison ratio is strictly larger than \(b_\infty^{-1}\), because its minimum is strictly below \(b_\infty\). If \(0<\alpha<1\), the displayed lower bound for the comparison ratio is again strictly larger than \(b_\infty^{-1}\). Therefore sharpness forces \(\alpha=1\), so
\[
\bar q(u)=c^2\|u\|^2
\]
for some \(c>0\).

For every horizontal unit vector \(u=(\theta,0)\), one has \(h_{Z_n}(u)=1\). The lower sandwich inequality therefore gives \(c^2=\bar q(u)\ge b_\infty^2\). On the other hand, for
\[
u_0=\frac{(\theta,s_0)}{\sqrt{1+s_0^2}},
\]
one has \(h_{Z_n}(u_0)=F_1(s_0)=b_\infty\). The upper sandwich inequality gives \(c^2=\bar q(u_0)\le b_\infty^2\). Thus
\[
\bar q(u)=b_\infty^2\|u\|^2.
\]

It remains to recover the original, possibly non-invariant quadratic form from equality in the averaging step. Fix a horizontal unit vector \(u=(\theta,0)\). For every \(g\in G\), the pointwise lower bound gives \(q(gu)\ge b_\infty^2\), while
\[
\int_G q(gu)\,d\mu(g)=\bar q(u)=b_\infty^2.
\]
The continuous nonnegative function \(g\mapsto q(gu)-b_\infty^2\) therefore vanishes identically. Consequently \(q(\theta,0)=b_\infty^2\) for every \(\theta\in S^{n-2}\), so the horizontal block of \(Q\) is \(b_\infty^2I_{n-1}\). At the axial unit vector \(e_n\), invariance of its \(G\)-orbit and the same equality give \(q(e_n)=b_\infty^2\). Hence
\[
Q=\begin{pmatrix}
b_\infty^2I_{n-1}&w\\
w^{\mathsf T}&b_\infty^2
\end{pmatrix}
\]
for some \(w\in\mathbb R^{n-1}\).

Now fix \(\theta\in S^{n-2}\) and put
\[
u_\theta=\frac{(\theta,s_0)}{\sqrt{1+s_0^2}}.
\]
Every vector in the \(G\)-orbit of \(u_\theta\) is a minimizing-slope direction, so its \(Z_n\)-support is \(b_\infty\). Thus the pointwise upper bound gives \(q(gu_\theta)\le b_\infty^2\) for every \(g\in G\), while its average equals \(b_\infty^2\). Equality follows throughout the orbit. In particular,
\[
q(u_\theta)=b_\infty^2+\frac{2s_0}{1+s_0^2}\langle w,\theta\rangle=b_\infty^2
\]
for every \(\theta\in S^{n-2}\). Since \(s_0>0\), this forces \(w=0\). Therefore \(Q=b_\infty^2I_n\), and hence \(E=b_\infty B_2^n\).

## Verification
The argument is analytic and uses no finite sampling. The normalization \(h_{Z_n}(\theta,0)=1\), \(h_{Z_n}(0,1)=1\), and the minimizing-slope identity \(h_{Z_n}(u_\theta)=b_\infty\) follow directly from the source's definitions of \(\phi\), \(F_1\), and \(s_0\). The strict exclusion of \(\alpha\ne1\) is read from the two cases in the source proof of Theorem 5.3. The final rigidity step is an equality-in-average argument for continuous nonnegative functions on the compact group \(G\).

## Relationship to prior work
Ryabogin and Zvavitch prove in arXiv:2609.10852v1 that
\[
d_{BM}(Z_n,B_2^n)=b_\infty^{-1}
\]
and state that the Euclidean ball is, up to scaling, an optimal Banach--Mazur ellipsoid. Their symmetry-averaging lemma shows that a nonsymmetric ellipsoid cannot improve the optimum, but it does not by itself show that every nonsymmetric optimizer must already be Euclidean. The result above extracts equality information from the same averaging mechanism and proves that stronger uniqueness statement.

Grundbacher and Kobos, arXiv:2407.08829v2 and Mathematika 71 (2025), study uniqueness of Banach--Mazur distance ellipsoids in general. Their Corollary 2.11 gives uniqueness for a symmetric \(n\)-dimensional body when its distance to the Euclidean ball is greater than \(\sqrt{n-1}\). That criterion does not imply the present result for \(n\ge3\): from \(\phi(s)\ge1\) and \(\phi(s)\ge s\), one gets \(F_1(s)\ge1/\sqrt2\), hence \(b_\infty^{-1}\le\sqrt2\le\sqrt{n-1}\).

## Limitations
Only origin-centered ellipsoids in the symmetric Banach--Mazur problem are treated. The statement does not assert uniqueness for translated ellipsoid pairs in a more general affine formulation. It also does not alter the value of \(b_\infty\), prove that \(Z_n\) is extremal among a broader class of convex bodies, or provide a classification of distance ellipsoids for arbitrary zonoids.

## References
D. Ryabogin and A. Zvavitch, *Zonoids whose polars are zonoids: the Banach--Mazur distance need not tend to one*, arXiv:2609.10852v1 (first public 2026-09-09), especially Lemmas 5.1--5.2 and Theorem 5.3.

F. Grundbacher and T. Kobos, *On Certain Extremal Banach-Mazur Distances and Ader's Characterization of Distance Ellipsoids*, arXiv:2407.08829v2; Mathematika 71 (2025), DOI 10.1112/mtk.70062, especially Theorem 2.6 and Corollary 2.11.
