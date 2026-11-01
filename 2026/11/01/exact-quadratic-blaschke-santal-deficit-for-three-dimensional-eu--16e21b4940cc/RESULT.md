# Exact quadratic Blaschke–Santaló deficit for three-dimensional Euclidean capsules

## Finding
Let \(B_2^3\) be the Euclidean unit ball in \(\mathbb R^3\), and let \(e_1=(1,0,0)\). For every \(r>0\) and \(a\ge0\), set
\[
K_{r,a}=rB_2^3+[-a,a]e_1,\qquad s=a/r,\qquad \delta=s/(1+s).
\]
The Santaló point of \(K_{r,a}\) is the origin, and its volume product satisfies the exact identity
\[
\boxed{\operatorname{vol}_3(K_{r,a})\operatorname{vol}_3(K_{r,a}^{\circ})
=\frac{16\pi^2}{9}\left(1-\frac{\delta^2}{4}\right).}
\]
Equivalently, its normalized deficit from the three-dimensional Euclidean ball is exactly \(\delta^2/4\). Consequently, for fixed \(r>0\), the product is strictly decreasing in \(a>0\), with
\[
\frac{4\pi^2}{3}<\operatorname{vol}_3(K_{r,a})\operatorname{vol}_3(K_{r,a}^{\circ})\le\frac{16\pi^2}{9}.
\]
The upper equality occurs exactly for \(a=0\); the lower constant is sharp but not attained at finite \(a/r\). The lower endpoint is the volume product of a circular cylinder \([-1,1]\times B_2^2\).

## Assumptions and scope
All volumes are ordinary three-dimensional Lebesgue measures. The polar is taken about the origin, \(K^{\circ}=\{y:\langle x,y\rangle\le1\ \forall x\in K\}\). The sum above is a Minkowski sum of a radius-\(r\) Euclidean ball with a centered segment of length \(2a\). No assertion is made for unequal end caps, higher dimensions, or general convex bodies.

The capsule is centrally symmetric and has interior, hence its unique Santaló point is \(0\). By uniform homothety the volume product depends only on \(s=a/r\). It suffices to take \(r=1\).

## Proof
Write \(K_s=B_2^3+[-s,s]e_1\). Its cross-section is a radius-one circular disk for \(|x_1|\le s\), and a spherical cap outside this central cylinder. Thus its volume is exactly
\[
V_s=\operatorname{vol}_3(K_s)=\frac{4\pi}{3}+2\pi s=\frac{2\pi}{3}(2+3s).
\]
The support function of the Minkowski sum is \(h_{K_s}(y)=\|y\|_2+s|y_1|\). Consequently,
\[
K_s^{\circ}=\{(x,z)\in\mathbb R\times\mathbb R^2:\sqrt{x^2+\|z\|_2^2}+s|x|\le1\}.
\]
For \(x\ge0\), the polar cross-section is a disk with squared radius \((1-sx)^2-x^2\), and the admissible range is precisely \(0\le x\le(1+s)^{-1}\). Fubini's theorem therefore gives
\[
\begin{aligned}
V_s^{\circ}
&=2\pi\int_0^{1/(1+s)}\big((1-sx)^2-x^2\big)\,dx\\
&=2\pi\left[\frac1{1+s}-\frac{s}{(1+s)^2}+\frac{s^2-1}{3(1+s)^3}\right]\\
&=\frac{2\pi(s+2)}{3(1+s)^2}.
\end{aligned}
\]
Hence
\[
V_sV_s^{\circ}=\frac{4\pi^2}{9}\frac{(2+3s)(2+s)}{(1+s)^2}.
\]
The polynomial identity
\[
4(1+s)^2-(2+3s)(2+s)=s^2
\]
reduces this to the announced exact quadratic deficit.

For \(s>0\), differentiation gives
\[
\frac{d}{ds}(V_sV_s^{\circ})=-\frac{8\pi^2s}{9(1+s)^3}<0.
\]
Its value at \(s=0\) is \(16\pi^2/9\), and its limit as \(s\to\infty\) is \(4\pi^2/3\). This proves the claimed bounds and equality cases.

For the geometric identification of the limiting product, apply the linear map \(T_s=\operatorname{diag}((1+s)^{-1},1,1)\) to \(K_s\). Its support function is
\[
h_{T_sK_s}(u)=\sqrt{u_1^2/(1+s)^2+\|u_\perp\|_2^2}+\frac{s}{1+s}|u_1|.
\]
The inequality \(0\le\sqrt{v^2+\varepsilon^2w^2}-v\le\varepsilon|w|\) implies uniform convergence of these support functions to \(\|u_\perp\|_2+|u_1|\), the support of \(C=[-1,1]\times B_2^2\). Thus the rescaled capsules converge to \(C\) in Hausdorff distance. The cylinder has volume \(2\pi\), and its polar is \(\{(x,z):|x|+\|z\|_2\le1\}\), of volume \(2\pi\int_0^1(1-x)^2dx=2\pi/3\). Its product is \(4\pi^2/3\), as asserted.

## Verification
`verify.py` uses standard-library exact fractions to check the polar integral and the polynomial identity at multiple rational parameters, verifies the polynomial identity coefficient-by-coefficient, and independently compares the polar volume with numerical spherical-support integration. It additionally checks the strict sign of the rational derivative at positive rational test points. The proof above is valid for all real \(s\ge0\); the finite checks are corroborative, not an exhaustive proof.

## Relationship to prior work
The Blaschke–Santaló inequality, and the quantitative stability theorem of Böröczky (2009), give global upper bounds and qualitative or quantitative proximity to an ellipsoid. Neither establishes the precise capsule-family identity \(1-\delta^2/4\). Meyer and Reisner (2006) establish convexity of reciprocal polar volume along shadow systems, rather than the displayed three-dimensional Minkowski-capsule volume computation. Iriyeh and Shibata (2017 preprint; 2019 revision) prove the sharp three-dimensional symmetric lower bound and its equality cases, which do not determine this capsule profile. The present result is an explicit family-specific, sharp quantitative model, not a new general Santaló inequality.

## Limitations
This does not determine a universal stability coefficient for all convex bodies, nor the exact Banach–Mazur distance of a capsule from the Euclidean ball. The normalized axial elongation \(\delta\) is a parameter specific to capsules, not an affine-invariant distance on arbitrary bodies. The lower cylinder limit is not a minimizer among all three-dimensional symmetric bodies. The historical literature search was bounded and cannot exclude an older, unindexed explicit capsule formula.

## References
1. M. Meyer and S. Reisner, *Shadow Systems and Volumes of Polar Convex Bodies*, Mathematika 53 (2006), 129–148, arXiv:math/0606305 (initial public version 2006-06-13), DOI:10.1112/S0025579300000061.
2. K. J. Böröczky, *Stability of the Blaschke–Santaló and the affine isoperimetric inequality*, Adv. Math. 225 (2010), 1914–1928, arXiv:0901.3340 (first posted 2009-01-21), DOI:10.1016/j.aim.2010.04.014.
3. H. Iriyeh and M. Shibata, *Symmetric Mahler's conjecture for the volume product in the three dimensional case*, Duke Math. J. 169 (2020), arXiv:1706.01749 (first posted 2017-06-06).
