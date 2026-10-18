# Universal thin-cap limits and sharp dimensional growth of affine least-squares projector norms

## Finding

Let \(d\ge2\). For any smooth strictly curved exposed boundary point of a compact convex body, the affine \(L^2\)-projection on a cap of inward height \(h\) has a universal limiting sharp endpoint norm as \(h\downarrow0\). The limit depends on dimension but not curvature or the containing body. For every such cap, its \(L^1\) and \(L^\infty\) operator norms are equal.

Write \(b=(d+1)/2\), \(m=b/(b+1)\), and \(a=(b+1)^2(b+2)/b\). Let \(V\) have density \(bv^{b-1}\) for \(0<v<1\), and independently let \(X\) be the first coordinate of a uniform point in the unit Euclidean ball of \(\mathbb R^{d-1}\). Then the common limiting sharp norm is

\[
C_d=\max_{0\le s\le1}\mathbb E\left|1+(d+3)\sqrt{sV}X+a(s-m)(V-m)\right|.
\]

In particular, \(C_d=d/e+O(\sqrt d)\) as \(d\to\infty\), and the coefficient \(1/e\) is sharp. The boundary-tip value is exactly

\[
T_d=2(b+1)\left(\frac{b+1}{b+2}\right)^b-1.
\]

This is a lower bound \(C_d\ge T_d\). At \(d=2\), the outer-rim value \(69907/43218+300\sqrt{30}/2401\) is another explicit lower bound. We do **not** assert that either witness maximizes for all dimensions.

## Assumptions and scope

Let \(K\subset\mathbb R^d\) be a compact convex body and let \(p\in\partial K\) be an exposed point. Assume that in a neighborhood of \(p\), the boundary is \(C^2\) and its inward second fundamental form is positive definite. Choose Euclidean coordinates with \(p=0\), inward normal coordinate \(y\), and tangential coordinate \(z\in\mathbb R^{d-1}\). Write the local boundary as \(y=g(z)\), where \(g(0)=0\), \(Dg(0)=0\), and \(g(z)=\tfrac12 z^{\mathsf T}Hz+o(\|z\|^2)\) for a positive-definite matrix \(H\). Set

\[
K_h=K\cap\{0\le y\le h\},\qquad \mu_h=\frac{\mathbf1_{K_h}\,dx}{|K_h|},
\]

for all sufficiently small \(h>0\). Let \(P_h\colon L^2(\mu_h)\to\operatorname{span}\{1,z_1,\ldots,z_{d-1},y\}\) be orthogonal projection, extended by its explicit reproducing kernel to bounded functions and integrable functions. Here each endpoint operator norm is taken relative to the normalized measure \(\mu_h\), not unnormalized Lebesgue measure. Let \(\mathcal D_d=\{(u,v):u\in\mathbb R^{d-1},\ \|u\|^2\le v\le1\}\) carry normalized volume measure \(\nu_d\).

## Proof

**1. Cap blow-up and norm continuity.** Since \(p\) is exposed, compactness gives that the set cut off by a sufficiently shallow supporting slab lies inside any prescribed neighborhood of \(p\). Define the invertible affine rescaling \(u=(2h)^{-1/2}H^{1/2}z\) and \(v=y/h\). The rescaled cap is

\[
D_h=\{(u,v):0\le v\le1,\ v\ge g((2h)^{1/2}H^{-1/2}u)/h\}.
\]

The quadratic graph assumption implies uniform convergence of the rescaled lower boundary to \(\|u\|^2\) on every fixed bounded set. Positive curvature and compactness bound all \(D_h\) in one fixed ball for small \(h\). Therefore \(D_h\) converges to \(\mathcal D_d\) both in Hausdorff distance and in volume symmetric difference. Their uniform probability measures converge in polynomial moments through degree two; the affine covariance matrices converge as well, with invertible limit because \(\mathcal D_d\) has nonempty interior.

For any full-dimensional compact region with normalized volume \(\mu\), the affine projector kernel is

\[
k(x,y)=1+(x-\bar x)^{\mathsf T}\Sigma^{-1}(y-\bar x),
\]

where \(\bar x\) and \(\Sigma\) are its mean and covariance. Its \(L^\infty\) norm is \(\sup_{x\in D}\int_D|k(x,y)|\,d\mu(y)\). Symmetry \(k(x,y)=k(y,x)\) makes this also its \(L^1\) norm. Invertible affine changes of coordinates preserve the affine span, its projection and its endpoint norms. Under the cap blow-up, covariance inversion and moment convergence make \(k_h\) converge uniformly to \(k_d\) on a common compact neighborhood. The bounded kernels and symmetric-difference convergence imply uniform convergence of the integral Lebesgue functions; Hausdorff convergence then gives convergence of their suprema. The cap limit is therefore exactly the affine projector norm of \(\mathcal D_d\), independent of \(H\).

**2. Exact paraboloid-model kernel.** Put \(U\in\mathbb R^{d-1}\) and \(V\in[0,1]\) for a \(\nu_d\)-distributed random point. Slicing at height \(v\), the allowed tangential section is a ball of radius \(\sqrt v\); hence \(V\sim\operatorname{Beta}(b,1)\), with \(b=(d+1)/2\), and \(U=\sqrt V\,Z\), where \(Z\) is independent, uniform in the unit \((d-1)\)-ball. Rotational symmetry and beta integration give

\[
\mathbb EU=0,\quad \mathbb EV=m=\frac b{b+1},\quad
\operatorname{Var}(V)=\frac b{(b+1)^2(b+2)},\quad
\operatorname{Cov}(U)=\frac1{d+3}I_{d-1},\quad
\operatorname{Cov}(U,V)=0.
\]

Thus, at query \((u,s)\in\mathcal D_d\),

\[
k_d((u,s),(U,V))=1+(d+3)u\cdot U+a(s-m)(V-m),\qquad
 a=\frac{(b+1)^2(b+2)}b.
\]

For fixed \(s\), the integral of its absolute value is convex in \(u\) and invariant under every rotation in \(\mathbb R^{d-1}\). A convex radial function has maximum over the ball \(\|u\|\le\sqrt{s}\) at radius \(\sqrt{s}\). Rotation sends the dot product to \(\sqrt{sV}X\), yielding the asserted exact scalar maximization. The coordinate density of \(X\) is \(\Gamma((d+1)/2)(1-x^2)^{(d-2)/2}/(\sqrt\pi\Gamma(d/2))\) on \([-1,1]\).

**3. Exact tip witness and sharp high-dimensional growth.** At the tip \((u,s)=(0,0)\), the kernel simplifies to

\[
k_d((0,0),(U,V))=(b+1)\{(b+1)-(b+2)V\}.
\]

It has mean one and becomes negative precisely when \(V>(b+1)/(b+2)\). Direct beta integration of its negative part gives

\[
\mathbb E|k_d((0,0),(U,V))|
=2(b+1)\left(\frac{b+1}{b+2}\right)^b-1=T_d.
\]

For an arbitrary query, remove its tangential term and define \(G_d(s)=\mathbb E|1+a(s-m)(V-m)|\). Cauchy–Schwarz with \(\mathbb E U_1^2=1/(d+3)\) gives a uniform difference bound

\[
\left|\mathbb E|k_d((u,s),(U,V))|-G_d(s)\right|
\le(d+3)\|u\|\mathbb E|U_1|\le\sqrt{d+3}.
\]

The scalar function \(G_d\) is convex on \([0,1]\); hence \(\max_sG_d(s)=\max\{G_d(0),G_d(1)\}\). Its first endpoint equals \(T_d\). At the second endpoint,

\[
G_d(1)\le1+a(1-m)\sqrt{\operatorname{Var}(V)}
=1+\sqrt{\frac{b+2}{b}},
\]

which is uniformly bounded for \(d\ge2\). Therefore

\[
T_d\le C_d\le\max\!\left\{T_d,1+\sqrt{\frac{b+2}b}\right\}+\sqrt{d+3}.
\]

As \(b\to\infty\), \(T_d=2b/e+O(1)=d/e+O(1)\). Consequently \(C_d=d/e+O(\sqrt d)\), establishing the sharp coefficient \(1/e\).

**4. Planar explicit boundary witness.** In dimension two, use \(u=s=1\) at the paraboloid model rim. The kernel is \(5U+(35/6)V-5/2\), and normalized area density is constant \(3/4\) on \(\{(U,V):U^2\le V\le1\}\). Integrating its absolute value first in \(U\) splits at \(\sqrt V=(\sqrt{30}-3)/7\); elementary polynomial integration gives

\[
\mathbb E|5U+(35/6)V-5/2|
=\frac{69907}{43218}+\frac{300\sqrt{30}}{2401}.
\]

This is an exact lower-bound witness and is not used to claim the global planar maximum.

## Verification

The accompanying `CHECK.py` executes 37 independent finite checks of the covariance identities, the tip's integrated kernel, a separately evaluated planar rim witness and the approach of the tip witness to \(1/e\). It uses only Python's standard library. Numerical integration has explicit discretization error and is not a proof of all-dimensional identities or of the cap limit; those follow from the preceding arguments. Execute `python3 CHECK.py` in the directory containing this file.

## Relationship to prior work

Hangelbroek–Narcowich–Sun–Ward (2010 preprint) prove bounds for kernel-generated least-squares projectors on a fixed manifold with quasiuniform centers; these are not projections onto fixed-degree affine polynomials on collapsing convex caps. Kroó–Lubinsky (2012) obtain Christoffel-function universality at high polynomial degree on fixed domains, a different limit and a different norm invariant. Kroó (2015) develops high-degree Christoffel asymptotics on convex and starlike domains, not the present collapsing-domain endpoint projector norm.

Classical affine projector covariance formulas and beta moments underlie the proof; the new claim is the cap-universality theorem together with its explicit dimension-dependent norm and sharp linear large-dimensional coefficient. Unlike the known simplex endpoint formula, the smooth cap approaches a paraboloidal rather than simplicial shape and has coefficient \(1/e\) rather than the simplex's \(2/e\). Similar lower-order projector computations on disks, annuli and polygons do not supply the dimension-uniform cap law.

## Limitations

Strict exposure and positive-definite curvature are essential hypotheses for the stated paraboloid model. No claim is made for flat points, singular boundaries, nonsmooth measures, fixed positive cap height, or polynomial degrees larger than one. No general exact formula for the maximizing height in the scalar expression, beyond the displayed maximization, is asserted. The remainder \(O(\sqrt d)\) concerns the universal limiting constants only; no uniform-in-dimension finite-depth convergence rate is established. No independent proof audit or historical-priority certification has occurred.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-Norm of the \(L_2\)-Projector*, arXiv:1005.2424, publicly posted 13 May 2010, https://arxiv.org/abs/1005.2424.
2. A. Kroó and D. S. Lubinsky, *Christoffel Functions and Universality in the Bulk for Multivariate Orthogonal Polynomials*, Canadian Journal of Mathematics 65 (2013), 600–620, doi:10.4153/CJM-2012-016-x, first available online 25 August 2012.
3. A. Kroó, *Christoffel functions on convex and starlike domains in \(\mathbb R^d\)*, Journal of Mathematical Analysis and Applications 421 (2015), 718–729, doi:10.1016/j.jmaa.2014.07.037.
