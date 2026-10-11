# Sharp scalar-defect thresholds on \(\ell_p\)-sums

## Finding

Let \(\mathbb K\in\{\mathbb R,\mathbb C\}\), let \(Y\ne\{0\}\) be a Banach space over \(\mathbb K\), and let \(1\le p\le\infty\). On the absolute \(\ell_p\)-sum \(X=\mathbb K\oplus_pY\), define, for \(0\le\lambda<1\),
\[
T_\lambda(a,y)=(\lambda a,0),\qquad
D_{p,\lambda}(a,y)=\bigl(\|(a,y)\|_X^2-\|T_\lambda(a,y)\|_X^2\bigr)^{1/2}.
\]
Then \(D_{p,\lambda}\) is a norm if and only if
\[
\boxed{\quad\lambda=0\quad\text{or}\quad p=2\quad\text{or}\quad
1<p<2\ \text{and}\ \lambda^2\le c_p:=\frac{p-1}{p}2^{2/p}.\quad}
\]
The strict endpoint \(\lambda^2=c_p\) is included. For \(1<p<2\), the positive threshold \(\sqrt{c_p}\) rises to \(1\) as \(p\uparrow2\); for every \(p>2\), however, no positive \(\lambda\) works. These statements hold for **every nonzero Banach space** \(Y\), without a dimension, smoothness, or reflexivity assumption.

For \(\mathbb K=\mathbb C\), Theorem 7.13 of Jana–Pal–Roy, with their Definition 1.2 of Banach-space isometric dilation, additionally makes the same condition necessary and sufficient for \(T_\lambda\) to admit such a dilation. This last equivalence uses their theorem; the new assertion is the exact coefficient threshold for these operators.

## Assumptions and scope

For finite \(p\), \(\|(a,y)\|_X=(|a|^p+\|y\|_Y^p)^{1/p}\); for \(p=\infty\) it is \(\max\{|a|,\|y\|_Y\}\). The scalar-coordinate operator \(T_\lambda\) has norm exactly \(\lambda<1\). Consequently \(D_{p,\lambda}(a,y)>0\) for each nonzero \((a,y)\), and \(D_{p,\lambda}\) is absolutely homogeneous. The sole issue is the triangle inequality. The parameter \(\lambda=1\) is deliberately excluded: it is not a strict contraction, and the defect vanishes on the scalar axis.

## Proof

**1. Reduction to an absolute plane.** Put \(t=\lambda^2\) and let
\[
N_{p,t}(u,v)=\Bigl((|u|^p+|v|^p)^{2/p}-t|u|^2\Bigr)^{1/2}
\quad(1\le p<\infty),
\]
with the analogous maximum-norm expression for \(p=\infty\). Since \(Y\ne\{0\}\), fixing any \(y_0\in Y\) with \(\|y_0\|=1\) restricts \(D_{p,\lambda}\) on \(\mathbb R\oplus\mathbb R y_0\) to \(N_{p,t}\). Thus the necessity of every condition may be checked on this real plane.

Conversely, whenever \(N_{p,t}\) is a norm on \(\mathbb R^2\), it is **absolute**, hence coordinatewise nondecreasing on the nonnegative quadrant (by convexity and invariance under coordinate sign changes). Therefore for \(a,b\in\mathbb K\) and \(y,z\in Y\),
\[
\begin{aligned}
D_{p,\lambda}(a+b,y+z)
&=N_{p,t}(|a+b|,\|y+z\|)\\
&\le N_{p,t}(|a|+|b|,\|y\|+\|z\|)\\
&\le N_{p,t}(|a|,\|y\|)+N_{p,t}(|b|,\|z\|).
\end{aligned}
\]
This proves the triangle inequality for real and complex \(Y\) simultaneously. It remains to classify the absolute plane norms.

**2. Exact interior curvature when \(1<p<2\).** For \(x,y>0\), write
\[
S=x^p+y^p,\qquad G(x,y)=N_{p,t}(x,y)^2=S^{2/p}-t x^2,
\]
and let \(B=\tfrac12\nabla^2(S^{2/p})\). Direct differentiation gives
\[
B=(p-1)S^{2/p-1}\begin{pmatrix}x^{p-2}&0\\0&y^{p-2}\end{pmatrix}
 +(2-p)S^{2/p-2}
\begin{pmatrix}x^{2p-2}&x^{p-1}y^{p-1}\\x^{p-1}y^{p-1}&y^{2p-2}\end{pmatrix}.
\]
In particular,
\[
\det B=(p-1)S^{4/p-2}x^{p-2}y^{p-2},\qquad
B_{22}=S^{2/p-2}y^{p-2}\bigl((p-1)x^p+y^p\bigr)>0.
\]
Since \(\tfrac12\nabla^2G=B-\mathrm{diag}(t,0)\), its positive semidefiniteness is equivalent, by the Schur complement, to \(t\le\det B/B_{22}\). With \(r=x/y>0\), this becomes
\[
t\le q_p(r):=\frac{(p-1)(1+r^p)^{2/p}r^{p-2}}{1+(p-1)r^p}.
\]
A logarithmic differentiation yields the exact identity
\[
\frac{d\log q_p(r)}{d\log r}
=\frac{(2-p)(r^p-1)}{(1+r^p)(1+(p-1)r^p)}.
\]
For \(1<p<2\) the derivative is negative below \(r=1\) and positive above \(r=1\). Hence
\[
\inf_{r>0}q_p(r)=q_p(1)=\frac{p-1}{p}2^{2/p}=c_p.
\]
The coefficient satisfies \(0<c_p<1\) in this range and is strictly increasing: indeed \(rac{d}{dp}\log c_p=\frac{p-2(p-1)\log2}{p^2(p-1)}>0\) for \(1<p<2\). It follows that \(G\) has positive semidefinite Hessian throughout the four open quadrants exactly when \(t\le c_p\). As \(p>1\), \(G\) is continuously differentiable away from the origin and its first derivatives agree across both coordinate axes; along either axis its restriction is a convex quadratic (since \(t<1\)). Integrating directional derivatives across the finitely many axis crossings of any line gives global convexity of \(G\). Its sublevel set \(\{G\le1\}\) is then convex, balanced, and absorbing; the positive homogeneous function \(N_{p,t}=\sqrt G\) is its Minkowski gauge, so it is a norm.

Conversely, when \(t>c_p\), at \((x,y)=(1,1)\) take the direction
\[
v=\bigl(1,-(2-p)/p\bigr).
\]
The above Schur-complement calculation gives
\[
\tfrac12\,v^{\mathsf T}(\nabla^2G(1,1))v=c_p-t<0.
\]
Thus \(G\) is not convex. Because the square of any norm is convex, \(N_{p,t}\) cannot be a norm. This also verifies sharpness exactly at the critical balanced point.

**3. Hilbert and endpoint cases.** When \(p=2\),
\[
N_{2,t}(u,v)^2=(1-t)|u|^2+|v|^2,
\]
so every \(0\le t<1\) works. When \(p=1\) and \(t>0\), the two vectors \((1,0)\) and \((0,1)\) violate the triangle inequality because
\[
N_{1,t}(1,1)=\sqrt{4-t}>1+\sqrt{1-t}=N_{1,t}(0,1)+N_{1,t}(1,0).
\]
If \(2<p<\infty\) and \(t>0\), choose a sufficiently small \(h>0\). As \(h\downarrow0\),
\[
N_{p,t}(h,1)^2=(1+h^p)^{2/p}-t h^2
=1+\frac2p h^p-t h^2+o(h^p)<1.
\]
But the midpoint of \((h,1)\) and \((-h,1)\) is \((0,1)\) of norm \(1\). The triangle inequality therefore fails. For \(p=\infty\) the same pair gives \(N_{\infty,t}(h,1)=\sqrt{1-th^2}<1\) whenever \(0<h<1\). Finally \(t=0\) recovers the original \(\ell_p\)-sum norm for all \(p\).

**4. Dilation interpretation.** For complex spaces, Jana–Pal–Roy prove that a strict contraction \(T\) possesses their \(\ell_2\)-complemented isometric dilation if and only if \(x\mapsto(\|x\|^2-\|Tx\|^2)^{1/2}\) is a norm. Apply this published equivalence to the just-classified \(T_\lambda\). No independent dilation construction or claim about broader, inequivalent notions of dilation is needed.

## Verification

The proof above is analytic and covers all real exponents and arbitrary nonzero Banach summands. The standalone standard-library program `verify.py` checks the Schur-complement minimum numerically for six sub-Hilbert exponents; checks the balanced-point negative-curvature witness above the threshold; performs deterministic triangle tests with complex scalars and two distinct Banach-summand norms; and checks explicit failure pairs in the remaining regimes. Running `python verify.py` produced `PASS 19890 numeric, complex-triangle, curvature, and failure-witness tests`. These finite tests corroborate the analytic identities and do not replace proofs for all parameters.

## Relationship to prior work

Jana, Pal and Roy (arXiv:2407.15112; first public version July 21, 2024) formulate the defect function, prove the norm/isometric-dilation equivalence for strict contractions (Definition 1.2 and Theorem 7.13 in the revised full text), and exhibit other failures on non-Hilbert \(L_p\)-spaces (Example 7.20). The theorem here **uses** that equivalence but identifies the previously uncomputed sharp threshold for the scalar-coordinate contraction on every \(\mathbb K\oplus_pY\).

Ricard and Xu (arXiv:1405.0431, Theorems 1–2) prove sharp global \(L_p\) convexity inequalities with coefficient \(p-1\) for \(1<p\le2\). Their universal bound does not decide the **fixed-coordinate** defect-norm threshold: throughout \(1<p<2\), the threshold here is strictly greater than \(p-1\), since \(2^{2/p}>p\). Their inequalities and the present classification address different quantifiers and different optimal constants.

## Limitations

The statement is restricted to scalar-coordinate contractions \(T_\lambda\), not general rank-one maps or all contractions. It assumes a nonzero Banach summand \(Y\) and \(\lambda<1\). Only the complex dilation implication in the precise sense of Jana–Pal–Roy is asserted. An equivalent coordinate-curvature calculation could exist in less directly indexed renorming literature; the present proof is self-contained notwithstanding that originality risk.

## References

1. S. Jana, S. Pal, S. Roy, *A dilation theoretic approach to Banach spaces*, arXiv:2407.15112, first submitted 2024-07-21; revised full text 2025-04-30, https://arxiv.org/html/2407.15112v2 (Definition 1.2, Theorem 7.13, Example 7.20).
2. É. Ricard, Q. Xu, *A noncommutative martingale convexity inequality*, arXiv:1405.0431, first submitted 2014-05-02, https://arxiv.org/html/1405.0431v4 (Theorems 1–2 and their proofs).
