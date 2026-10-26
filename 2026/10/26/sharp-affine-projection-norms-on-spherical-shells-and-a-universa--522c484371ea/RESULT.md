# Sharp affine-projection norms on spherical shells and a universal hole-contact singularity

## Finding

For every integer \(d\ge 2\) and every \(0\le r<1\), let
\[A_{d,r}=\{x\in\mathbb R^d:r\le\|x\|_2\le1\}\]
carry normalized Lebesgue measure \(\mu_{d,r}\), and let \(P_{d,r}\) be the \(L^2(\mu_{d,r})\)-orthogonal projection onto the real affine functions \(\operatorname{span}\{1,x_1,\ldots,x_d\}\). Write \(\omega_j=\pi^{j/2}/\Gamma(1+j/2)\) for the volume of the unit \(j\)-ball and put
\[q_d(r)=\frac{1-r^{d+2}}{(d+2)(1-r^d)}.\]
For \(R,q>0\), define the explicit cap moment
\[
F_d(R,q)=\begin{cases}
\displaystyle \omega_{d-1}\int_q^R\left(\frac{t}{q}-1\right)(R^2-t^2)^{(d-1)/2}\,dt,&R>q,\\
0,&R\le q.
\end{cases}
\]
The **exact sharp endpoint norms** are
\[
\boxed{\|P_{d,r}\|_{L^1\to L^1}=\|P_{d,r}\|_{L^\infty\to L^\infty}
=\Lambda_d(r):=1+\frac{2\bigl(F_d(1,q_d(r))-F_d(r,q_d(r))\bigr)}{\omega_d(1-r^d)}.}
\]
The maximum is realized by outer-boundary evaluation in every radial direction. At a chosen boundary unit vector \(u\), the sign-valued datum \(f(y)=\operatorname{sgn}(1+u\cdot y/q_d(r))\) is an endpoint extremizer (boundary evaluation is understood by continuous extension).

There is a **unique geometric contact radius** \(r_d\in(1/(d+2),1/d)\) satisfying
\[r_d=q_d(r_d).\]
For \(r\le r_d\), the inner hole misses the negative cap of the sharp projection kernel, so \(F_d(r,q_d(r))=0\); for \(r>r_d\), it has strictly positive contribution. This contact produces a universal one-sided nonanalyticity. Define the analytic outer-cap continuation
\[H_d(r)=1+\frac{2F_d(1,q_d(r))}{\omega_d(1-r^d)}\]
near \(r_d\), and set \(\alpha_d=(d+3)/2\). Then
\[
\boxed{H_d(r)-\Lambda_d(r)=C_d(r-r_d)_+^{\alpha_d}
+O\bigl((r-r_d)_+^{\alpha_d+1}\bigr),}
\]
with the **strictly positive and explicit** coefficient
\[
\boxed{C_d=
\frac{8\omega_{d-1}2^{(d-1)/2}r_d^{(d-3)/2}}
{\omega_d(1-r_d^d)(d+1)(d+3)}
\bigl(1-q_d'(r_d)\bigr)^{(d+3)/2}.}
\]
Consequently \(\Lambda_d\) is smooth on either side of \(r_d\), is of class \(C^{\lceil\alpha_d\rceil-1}\) at \(r_d\), and is **not** of class \(C^{\lceil\alpha_d\rceil}\) there. The first unsmooth derivative therefore depends only on dimension, although the contact radius and coefficient vary with dimension.

In the planar case \(d=2\), the contact radius is exactly
\[r_2=2-\sqrt3.\]
The cap moment has the fully elementary expression
\[
F_2(R,q)=
-R^2\arccos(q/R)+q\sqrt{R^2-q^2}
+\frac{2}{3q}(R^2-q^2)^{3/2}
\quad(R>q),
\]
with value zero for \(R\le q\), and \(q_2(r)=(1+r^2)/4\). Hence the planar norm is a piecewise elementary function, twice continuously differentiable but not three times differentiable at \(2-\sqrt3\). Its previously known full-disk and limiting circular-boundary benchmarks are, respectively,
\[
\Lambda_2(0)=1-\frac2\pi\arccos\frac14+\frac{11\sqrt{15}}{8\pi},
\qquad
\lim_{r\uparrow1}\Lambda_2(r)=\frac13+\frac{2\sqrt3}{\pi}.
\]

## Assumptions and scope

The dimension \(d\) is an integer at least two; all balls and shells use Euclidean distance and Lebesgue volume, and \(r\) is the ratio of inner to outer radius. The outer radius is one by dilation invariance. The projection is the real or complex-linear extension of the same real-kernel orthogonal projection. The endpoint \(L^1\) operator is the canonical finite-rank extension of the \(L^2\) projector. The theorem specifies the sharp induced norms, not the \(L^2\) norm (which is one). The contact regularity is local at the unique \(r_d\), not a claim that the norm is monotone for every \(r\).

## Proof

1. **Reproducing kernel.** Rotational symmetry gives \(\mathbb E_\mu y_i=0\) and \(\mathbb E_\mu y_i y_j=\delta_{ij}q_d(r)\), because
\[\mathbb E_\mu\|y\|_2^2=\frac{d(1-r^{d+2})}{(d+2)(1-r^d)}.\]
Thus the exact projector is
\[(P_{d,r}f)(x)=\int_{A_{d,r}}K(x,y)f(y)\,d\mu(y),\quad K(x,y)=1+\frac{x\cdot y}{q_d(r)}.\]

2. **Endpoint localization and sharpness.** The induced \(L^\infty\) norm is the supremum over \(x\in A_{d,r}\) of \(\int|K(x,y)|\,d\mu(y)\). For fixed \(y\)-law this expression, as a function of \(x\), is convex and rotationally invariant, hence its radial profile is nondecreasing; its maximum is at \(\|x\|_2=1\). At \(x=u\) the sign of \(K(u,y)\) yields equality. Although the boundary has zero volume, the projected output is affine and continuous up to the boundary, so its essential supremum equals the boundary supremum. Symmetry \(K(x,y)=K(y,x)\) and equality of the underlying measures give the identical sharp \(L^1\) norm.

3. **Negative-cap formula.** The kernel has integral one in \(y\). Therefore its absolute integral equals one plus twice the normalized mass of its negative part. Choosing \(u=e_1\), that negative part is \((-1-y_1/q)_+\). For any ball of radius \(R\), slicing perpendicular to the first coordinate at \(y_1=-t\) gives cross-sectional volume \(\omega_{d-1}(R^2-t^2)^{(d-1)/2}\). Its negative mass is exactly \(F_d(R,q)\). Subtracting the inner ball from the outer ball proves the displayed sharp norm formula for every \(d,r\).

4. **Unique contact.** If \(U\) is uniform on \([0,1]\), the radius of a uniform point in the shell has the same law as \(\rho_r=(r^d+(1-r^d)U)^{1/d}\). Thus \(q_d(r)=\mathbb E(\rho_r^2)/d\). For \(0<r<1\), differentiation under the integral and the inequality \(\rho_r\ge r\) give
\[
0\le q_d'(r)
=\frac1d\mathbb E\left[2r^{d-1}(1-U)\rho_r^{2-d}\right]
\le\frac rd<1.
\]
The function \(r-q_d(r)\) is therefore strictly increasing, negative at \(r=0\) and positive as \(r\uparrow1\) since \(q_d(1)=1/d\). Its unique root lies strictly between \(1/(d+2)\) and \(1/d\) because \(q_d(0)=1/(d+2)\) and \(q_d(r)<1/d\) for \(r<1\). Consequently the inner-ball cap vanishes exactly up to the contact radius.

5. **Universal contact singularity.** Put \(h=R-q>0\). Substitute \(t=R-v\) into the cap integral and use \(R^2-t^2=v(2R-v)\). Uniformly near any fixed positive contact radius,
\[
F_d(R,q)=\frac{4\omega_{d-1}2^{(d-1)/2}R^{(d-3)/2}}
{(d+1)(d+3)}h^{(d+3)/2}
\bigl(1+O(h)\bigr).
\]
Indeed the leading integral is \(\int_0^h(h-v)v^{(d-1)/2}\,dv=4h^{(d+3)/2}/((d+1)(d+3))\). At \(R=r\) and \(q=q_d(r)\), the gap satisfies \(h=(1-q_d'(r_d))(r-r_d)+O((r-r_d)^2)\), with positive slope. Inserting this asymptotic into the exact endpoint norm gives \(C_d\) and the stated remainder. The outer-cap term \(H_d\) is real analytic near contact since \(q_d(r_d)<1\). Therefore the one-sided term cannot be canceled by the smooth part, and the differentiability classification follows. For \(d=2\), integration of the circular slice yields the elementary formula and solving \(4r=1+r^2\) gives \(2-\sqrt3\). The two endpoint benchmarks follow by substitution and the thin-annulus limit, respectively.

## Verification

The accompanying standalone `CHECK.py` recomputes the exact cap formula by numerical integration in dimensions two through nine, independently integrates the planar angular kernel, checks the elementary circular-cap expression, and evaluates the contact exponents with high-precision integration. It completed 205 formula/quadrature assertions and eight asymptotic-scaling assertions. These calculations are stress tests, not substitutes for the preceding proof, and the finite set of dimensions is not used to infer the general theorem.

Run from a directory containing the supplied file: `python3 CHECK.py`. The checker uses Python, SciPy and mpmath; no network or source file downloads are required.

## Relationship to prior work

Hansen, Atkinson and Chien formulate \(L^2\) polynomial projection and study norms of discrete hyperinterpolation operators on a **filled disk**, with a different large-degree objective. Wade develops Lebesgue-constant estimates for hyperinterpolation on **weighted balls**; Li and Xu develop polynomial and Sobolev spectral approximation on a **filled ball**. These works supply the classical approximation-theoretic motivation and kernel setting, but their stated theorems do not provide the present hole-contact threshold or dimension-dependent loss of smoothness under shell perforation. Classical full-disk and spherical-boundary degree-one constants are benchmark cases, not claimed as new.

The new claim is the complete sharp shell norm in every dimension together with the unique contact and its exact leading one-sided singularity. The general covariance kernel identity itself is elementary and is not asserted to be novel.

## Limitations

No optimality claim is made for higher polynomial degree, nonconcentric holes, nonuniform shell weights or other shapes. The result does not establish global monotonicity of the norm with the hole radius. The cross-dimensional contact law is analytically proven, but available finite computations are consistency checks only. Priority relative to unindexed or inaccessible literature remains subject to independent bibliographic verification.

## References

- O. Hansen, K. Atkinson, D. Chien, *On the norm of the hyperinterpolation operator on the unit disc and its use for the solution of the nonlinear Poisson equation*, IMA Journal of Numerical Analysis, advance-access publication 20 March 2008, doi:10.1093/imanum/drm052; author-hosted full text: https://homepage.divms.uiowa.edu/~atkinson/papers/Hansen_KEA_Chien2008.pdf.
- J. Wade, *On hyperinterpolation on the unit ball*, arXiv:1209.4328, first posted 19 September 2012, https://arxiv.org/abs/1209.4328.
- H. Li, Y. Xu, *Spectral approximation on the unit ball*, arXiv:1310.2283, first posted 8 October 2013, https://arxiv.org/abs/1310.2283.
