# Sharp affine least-squares stability on the uniform hemisphere

## Finding
Let \(H=\{y\in\mathbb R^3:\|y\|_2=1,\ y_3\ge0\}\), with probability measure \(d\mu=d\sigma/(2\pi)\) obtained from surface area on the upper hemisphere. Let \(P\) be the \(L^2(H,\mu)\)-orthogonal projector onto the restrictions to \(H\) of affine functions on \(\mathbb R^3\), namely \(\operatorname{span}\{1,y_1,y_2,y_3\}\). The projector extends to bounded maps on \(L^1\) and \(L^\infty\), and its sharp endpoint norms are
\[
\boxed{\|P\|_{L^1\to L^1}=\|P\|_{L^\infty\to L^\infty}=\frac{61\sqrt5}{15}-7=2.093343108499\ldots .}
\]
Its row-kernel absolute integral attains this maximum *exactly* at points of the equatorial circle \(\{x\in H:x_3=0\}\). Every nonzero \(L^\infty\) extremizer, modulo scalar multiplication, is the sign of the kernel at one of those evaluation points; no nonzero \(L^1\) extremizer exists. For \(0\le f\le1\), the exact maximal negative overshoot is \((61\sqrt5-120)/30=0.546671554249\ldots\), attained by the indicator of an explicitly described spherical cap.

## Assumptions and scope
The surface is the **curved hemisphere only**: the equatorial disk carries no measure. All functions are measurable and real- or complex-valued; endpoint norms are essential supremum and integral norms with respect to \(\mu\). The projection is fixed to the indicated four-dimensional affine space, not optimized over all projections onto that space. The result is for the ordinary unweighted surface measure on the *unit two-sphere* truncated by one equatorial plane, not for arbitrary spherical caps, higher degrees, or general dimensions.

For \(x\in H\), write \(\lambda(x)=\int_H |K(x,y)|\,d\mu(y)\), where \(K\) is the reproducing kernel of the projected space. The statement about maximizing evaluations refers to \(\lambda\), and a scalar multiple of \(\operatorname{sgn}(K(x,\cdot))\) is understood up to \(\mu\)-null sets. The sharp undershoot is \(\sup_{0\le f\le1}\|(-Pf)_+\|_{L^\infty}\); there is no nonnegativity-preservation claim for \(P\).

## Proof
**1. Exact reproducing kernel.** For a uniformly distributed \(Y\in H\), the height \(Y_3\) is uniform on \([0,1]\) and the azimuth is independent and uniform. Consequently
\[
\mathbb E Y_1=\mathbb E Y_2=0,\quad \mathbb E Y_3=\tfrac12,\quad
\mathbb E Y_i^2=\tfrac13\ (i=1,2,3),\quad
\operatorname{Var}(Y_3)=\tfrac1{12},
\]
with vanishing centered off-diagonal covariances. The four functions \(1\), \(\sqrt3y_1\), \(\sqrt3y_2\), and \(\sqrt{12}(y_3-1/2)\) form an orthonormal basis. Thus
\[
K(x,y)=1+3(x_1y_1+x_2y_2)
 +12(x_3-\tfrac12)(y_3-\tfrac12),\qquad
Pf(x)=\int_H K(x,y)f(y)\,d\mu(y).
\]
In particular, \(\int_H K(x,y)\,d\mu(y)=1\), and for any \(x\in\mathbb R^3\) (including off-surface parameter points) the orthonormal-basis identity gives \(\int_H K(x,y)^2\,d\mu(y)=K(x,x)\).

**2. Boundary localization.** Rotational symmetry allows an evaluation point of height \(z\in[0,1]\) to have horizontal radius \(r=\sqrt{1-z^2}\). Introduce
\[
F(\rho,z)=\int_H\left|1+3\rho Y_1+12(z-\tfrac12)(Y_3-\tfrac12)\right|d\mu,
\qquad\lambda(x)=F(r,z).
\]
Conditioned on \(Y_3=t\), the variable \(Y_1=\sqrt{1-t^2}\cos\phi\) has a symmetric azimuthal distribution. For any fixed real \(a\), the map \(b\mapsto\mathbb E_\phi|a+b\cos\phi|\) is convex and even, hence nondecreasing on \([0,\infty)\). Therefore \(F(r,z)\le F(1,z)\). For fixed \(\rho=1\), the map \(z\mapsto F(1,z)\) is convex, because the expression inside its absolute value depends affinely on \(z\).

At the auxiliary parameter point \((1,0,1/3)\), the orthonormal-basis identity and Cauchy--Schwarz yield
\[
F(1,\tfrac13)\le \left(\int_H K((1,0,\tfrac13),y)^2d\mu(y)\right)^{1/2}
=\sqrt{\tfrac{13}{3}}.
\]
Hence for \(0\le z\le1/3\), convex interpolation gives
\[
\lambda(x)\le F(1,z)\le(1-3z)F(1,0)+3z\sqrt{\tfrac{13}{3}}.
\tag{1}
\]
For \(1/3\le z\le1\), Cauchy--Schwarz directly on the actual spherical evaluation point yields
\[
\lambda(x)\le\sqrt{K(x,x)}=\sqrt{7-12z+9z^2}\le 2.
\tag{2}
\]
The last inequality holds because the convex quadratic \(7-12z+9z^2\) equals \(4\) at both endpoints \(z=1/3\) and \(z=1\).

**3. Exact equatorial row integral.** Set \(x=e_1=(1,0,0)\). Then \(K(e_1,y)=4+3y_1-6y_3=4-3\sqrt5\,v\cdot y\), where \(v=(-1,0,2)/\sqrt5\) is a unit vector. Its negative set is the spherical cap
\[
C_v=\left\{y\in S^2:v\cdot y>\frac4{3\sqrt5}\right\}.
\]
This cap lies entirely inside \(H\): on the lower hemisphere \(y_3\le0\), the kernel satisfies \(4+3y_1-6y_3\ge1\). Under full-sphere surface area \(d\sigma\), the coordinate \(u=v\cdot y\) has area element \(2\pi\,du\). Since \(d\mu=d\sigma/(2\pi)\) on \(H\), the negative mass is exactly
\[
N:=\int_H(-K(e_1,y))_+d\mu(y)
=\int_{4/(3\sqrt5)}^1(3\sqrt5\,u-4)\,du
=\frac{(3\sqrt5-4)^2}{6\sqrt5}.
\]
Because the integral of the kernel is \(1\), its absolute integral is \(1+2N\), giving
\[
F(1,0)=1+\frac{(3\sqrt5-4)^2}{3\sqrt5}
=\frac{61\sqrt5}{15}-7=:L.
\tag{3}
\]
The strict comparison \(L>\sqrt{13/3}>2\) has a rational check: \(\sqrt5>447/200\) implies \(L>2089/1000\), and \(2089/1000>25/12>\sqrt{13/3}\). Combining (1)--(3) shows \(\lambda(x)<L\) for every \(x\in H\) with \(x_3>0\); by rotational symmetry \(\lambda(x)=L\) at every equatorial point. This proves both sharpness and the **complete set of maximizing evaluations**.

**4. Endpoint norms and equality.** The integral representation gives \(\|P\|_{\infty\to\infty}=\sup_{x\in H}\lambda(x)=L\). For any equatorial \(x\), the input \(f_x(y)=\operatorname{sgn}K(x,y)\) has essential supremum one and satisfies \(Pf_x(x)=L\). Conversely, if a nonzero bounded \(f\) attains the norm, the finite-rank output \(Pf\) is continuous and \(\mu\) has full support on \(H\), so the essential supremum of \(|Pf|\) equals its maximum at some \(x\in H\). Equality in the integral triangle inequality forces \(x\) to lie on the equator and \(f(y)=c\operatorname{sgn}K(x,y)\) almost everywhere for some nonzero constant \(c\), because \(K(x,\cdot)\) is nonzero almost everywhere. Kernel symmetry and duality imply \(\|P\|_{1\to1}=L\). No nonzero \(L^1\) input attains that norm: indeed
\[
\|Pf\|_1\le\int_H\lambda(y)|f(y)|d\mu(y)<L\|f\|_1,
\]
since \(\lambda(y)<L\) for \(\mu\)-almost every \(y\) and \(f\not\equiv0\).

**5. Positive inputs.** For each fixed evaluation \(x\), \(\min_{0\le f\le1}Pf(x)=\int_{K(x,y)<0}K(x,y)d\mu(y)=-(\lambda(x)-1)/2\). The largest negative undershoot is therefore \((L-1)/2=(61\sqrt5-120)/30\). At an equatorial point, equality is attained by the indicator of its cap \(C_v\). This is a consequence of the same sharp kernel theorem, not a second independent claim.

## Verification
Run `python3 check.py` using only the Python standard library. The script checks rational Gram-matrix identities and the strict rational comparison used in the proof, evaluates the exact cap formula, and performs both independent-coordinate two-dimensional midpoint quadrature and azimuth-reduced Simpson quadrature. In this instance it passed **96 assertions**, gave \(2.093343108499145\) for the exact constant, and gave \(2.093341942229042\) in direct two-dimensional numerical quadrature. Those finite numerical calculations do **not** prove the global bound or equality classification; the arguments above do.

## Relationship to prior work
Hangelbroek--Narcowich--Sun--Ward (arXiv:1005.2424, Theorem 5.1 and its sphere example) establish general stability estimates for least-squares projections onto kernel-translate subspaces of manifolds. Hangelbroek--Narcowich--Ward (arXiv:1012.4852, Sections 3 and 5) study analogous polyharmonic-kernel spaces on whole manifolds. Neither inspected source concerns the exact norm of the fixed four-dimensional affine projection under **truncated spherical surface measure**. Defant--Galicer--Mansilla--Mastyło--Muro (arXiv:2405.12123, Section 4 and Corollary 4.12) obtain exact full-sphere polynomial projection constants using rotational symmetry; the full-sphere degree-one instance has norm \(5/3\). The hemisphere breaks that symmetry, with a different covariance kernel and a strictly larger norm. Published simplex projection constants and first-harmonic semicircle constants concern different sample spaces and do not imply the hemispherical result. These comparisons support an original contribution within the inspected evidence but do not establish absolute historical priority.

## Limitations
There is no statement for a general spherical cap, weighted surface area, higher-degree polynomials, higher-dimensional hemispheres, or an optimal projection among all projectors onto the same range. Search coverage is incomplete; unindexed early literature and terminology differences may conceal antecedents. The result has a complete analytic proof, but no independent mathematical or bibliographic audit has been performed.

## References
1. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424 (first submitted 2010-05-13), https://arxiv.org/abs/1005.2424.
2. T. Hangelbroek, F. J. Narcowich, J. D. Ward, *Polyharmonic and Related Kernels on Manifolds: Interpolation and Approximation*, arXiv:1012.4852 (2010), https://arxiv.org/abs/1012.4852.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Minimal projections onto spaces of polynomials on real Euclidean spheres*, arXiv:2405.12123 (first submitted 2024-05-20), https://arxiv.org/abs/2405.12123.
