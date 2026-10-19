# Exact degree-three positivity-loss constant for first-harmonic Fourier reproduction

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let \(C_{\mathbb R}(\mathbb T)\) have the uniform norm, and let \(\mathcal P_j\) be the real trigonometric polynomials of degree at most \(j\). Consider all bounded real-linear operators \(A:C_{\mathbb R}(\mathbb T)\to\mathcal P_3\) that reproduce \(\mathcal P_1\) pointwise. Their least possible operator norm is a uniquely specified exact constant \(\Lambda_{1,3}\), approximately \(1.16139544326947142872\). The associated least worst-case positivity loss is exactly \((\Lambda_{1,3}-1)/2\), approximately \(0.08069772163473571436\).

Here is a finite, exact characterization of the constant and of its unique even convolution-kernel minimizer. Put
\[
K_{a,b}(t)=1+2\cos t+2a\cos(2t)+2b\cos(3t), \qquad a,b\in\mathbb R.
\]
There is exactly one real quintuple \((a,b,\alpha,\beta,\gamma)\) satisfying \(0<\alpha<\beta<\gamma<\pi\), the three equations
\[
K_{a,b}(\alpha)=K_{a,b}(\beta)=K_{a,b}(\gamma)=0,
\]
and the two equations
\[
\sin(2\alpha)-\sin(2\beta)+\sin(2\gamma)=0,\qquad
\sin(3\alpha)-\sin(3\beta)+\sin(3\gamma)=0.
\]
With
\[
F_{a,b}(t)=t+2\sin t+a\sin(2t)+\frac{2b}{3}\sin(3t),
\]
the exact optimal norm is
\[
\boxed{\displaystyle
\Lambda_{1,3}=\frac1\pi\left|2F_{a,b}(\alpha)-2F_{a,b}(\beta)+2F_{a,b}(\gamma)-\pi\right|.}
\]
The unique minimizing even convolution kernel is \(K_{a,b}\), whose only zeros in \((0,\pi)\) are the three simple points \(\alpha,\beta,\gamma\). Numerical values (not definitions of the exact constant) are
\[
\begin{aligned}
a&\approx0.53974621269702685056, & b&\approx0.28162143596785042513,\\
\alpha&\approx1.44277583775848871384, &\beta&\approx1.99007264651936166881,\\
\gamma&\approx2.31699816241351683603.
\end{aligned}
\]
Moreover \(1<\Lambda_{1,3}<4/\pi\). Thus allowing the third harmonic strictly improves on the optimal degree-two reproduction norm \(4/\pi\), and the canonical degree-three delayed de la Vallée–Poussin kernel is strictly suboptimal.

## Assumptions and scope
All operators act on real-valued continuous functions; the Fourier normalization is \(\widehat f(k)=(2\pi)^{-1}\int_0^{2\pi}f(t)e^{-ikt}\,dt\). Convolution uses normalized Haar measure. The norm is the operator norm induced by \(\|f\|_\infty\). No translation-invariance or reflection symmetry is assumed of the original operators. The claimed uniqueness is for the even translation-invariant minimizing kernel, not for all possible non-equivariant minimizing operators. The harmonic degrees \(1\) and \(3\) are fixed; no formula is claimed for higher output bands.

## Proof
**1. Reduction to two free Fourier multipliers.** Average an admissible operator over circle rotations, then average it with its conjugate by reflection \(t\mapsto-t\). Each averaging preserves its reproduction property and range \(\mathcal P_3\), and cannot increase its norm. The averaged operator commutes with rotations and reflection, so is convolution with a real even trigonometric kernel. Reproduction of \(\mathcal P_1\) forces Fourier multipliers \(\widehat K(0)=\widehat K(1)=\widehat K(-1)=1\); the remaining multipliers are two arbitrary real numbers \(a,b\), giving exactly \(K_{a,b}\). The uniform norm of convolution with a continuous kernel equals its normalized \(L^1\)-norm: approximate its sign at a point by continuous test functions to obtain the lower bound. Thus
\[
\Lambda_{1,3}=\min_{a,b\in\mathbb R}J(a,b),\qquad
J(a,b)=\frac1\pi\int_0^\pi|K_{a,b}(t)|\,dt.
\]
The minimum exists: \(J\) is continuous and convex; also \(J(a,b)\ge\max\{|a|,|b|\}\) by Fourier coefficient bounds, so it is coercive.

**2. Every minimizer has exactly three simple sign changes.** The nonzero trigonometric polynomial \(K_{a,b}\) has finitely many zeros, so differentiation under the integral is valid:
\[
\partial_aJ=\frac2\pi\int_0^\pi\cos(2t)\operatorname{sgn}K_{a,b}(t)\,dt,\qquad
\partial_bJ=\frac2\pi\int_0^\pi\cos(3t)\operatorname{sgn}K_{a,b}(t)\,dt.
\]
Both derivatives vanish at a minimizer. Because \(\pi^{-1}\int_0^\pi K\,dt=1\) and \(\pi^{-1}\int_0^\pi K\cos t\,dt=1\), \(K\) cannot be nonnegative throughout \((0,\pi)\): otherwise \(\int_0^\pi K(t)(1-\cos t)\,dt=0\) forces the nonzero continuous \(K\) to vanish identically. Nor can \(K\) be nonpositive. It therefore changes sign at least once.

The change of variable \(u=\cos t\) expresses \(K\) as
\[
8bu^3+4au^2+(2-6b)u+(1-2a),
\]
so there are at most three sign-changing zeros in \((0,\pi)\). Exactly one sign change at \(\alpha\) would force \(\sin(2\alpha)=\sin(3\alpha)=0\), which is impossible for \(0<\alpha<\pi\). Exactly two at \(\alpha<\beta\) would force \(\sin(2\alpha)=\sin(2\beta)\) and \(\sin(3\alpha)=\sin(3\beta)\). The first equality forces \(\alpha+\beta\) to equal \(\pi/2\) or \(3\pi/2\); in either case \(0<\beta-\alpha<\pi/2\). The second equality would then force \(\sin(3(\beta-\alpha)/2)=0\), since \(\cos(3(\alpha+\beta)/2)\ne0\); this is impossible because \(0<3(\beta-\alpha)/2<3\pi/4\). Hence exactly three sign changes occur. Since the polynomial in \(u\) has degree at most three, all three zeros are simple.

**3. Exact determining system and uniqueness.** Denote these three simple zeros by \(\alpha<\beta<\gamma\). Their alternating sign intervals and the vanishing derivatives above give precisely the two sine equations in the Finding section. Together with the three zero equations, this proves existence of a quintuple satisfying the stated system.

Conversely, any quintuple satisfying the system has three distinct interior roots of the cubic and therefore exactly three alternating sign intervals. Its two sine equations give \(\nabla J(a,b)=0\); convexity makes it a global minimizer. To prove uniqueness, suppose two distinct kernels \(K_1,K_2\) minimized \(J\). Equality in the triangle inequality for their midpoint forces \(K_1(t)K_2(t)\ge0\) almost everywhere. Since each has exactly three simple sign changes, their three crossing locations coincide. Their cubic polynomials in \(\cos t\) therefore have the same three distinct roots and are proportional; their common constant Fourier coefficient \(1\) forces the proportionality factor to be \(1\). Consequently both kernels, and hence both quintuples, coincide.

**4. Exact value, strict improvement, and positivity loss.** The primitive of \(K_{a,b}\) is \(F_{a,b}\) and its sign alternates across the three simple zeros. Integrating separately over the four intervals gives the displayed exact formula for \(\Lambda_{1,3}\). The inequality \(\Lambda_{1,3}>1\) follows from \(\int K=1\) and the impossibility of a nonnegative admissible kernel. Taking \(a=1/2,b=0\) yields \(K(t)=2\cos t(1+\cos t)\) and \(J=4/\pi\). This trial kernel has only one interior sign change and hence cannot minimize \(J\), proving the strict upper bound. The canonical delayed de la Vallée–Poussin degree-three kernel has \((a,b)=(2/3,1/3)\), so uniqueness and the different optimal coefficients (equivalently its failure of the stationary equations) show it too is strictly suboptimal.

Every admissible operator reproduces \(1\), so its representing signed measures have mass one. The worst excess above \(1\) and worst undershoot below \(0\) for \(0\le f\le1\) both equal half the excess operator norm \((\|A\|-1)/2\). Taking the infimum therefore gives exactly \((\Lambda_{1,3}-1)/2\).

## Verification
The adjacent standalone file `check_projection.py` numerically solves the five defining equations at 60-digit precision, checks residuals below \(10^{-50}\), verifies the three ordered simple roots and Fourier moments, evaluates the exact primitive formula against independent interval-split quadrature, and compares with the degree-two and canonical degree-three kernels. It also carries out 10,752 finite-mesh integrand checks and tests positivity of the local Hessian. Run it with `python check_projection.py` in an environment with `mpmath` installed. The existence, uniqueness, all-operator lower bound, and exact-value identities are analytic consequences of the proof above, not numerical extrapolations.

## Relationship to prior work
Hao-Ning Wu, *Positivity loss in bandlimited spectral reproduction on spheres*, arXiv:2609.02695 (first posted September 2, 2026), proves sharp-order estimates for a general two-scale projection constant and reduces the circle case to bandlimited Fourier kernels. It does not provide this degree-three exact constant or three-crossing extremizer. Deregowska, Foucart, Lewandowska, and Skrzypek, *On the Norms and Minimal Properties of de la Vallée Poussin's type Operators*, proves precise norms and minimality/nonminimality of specified averaging kernels; in particular, its nonminimality theorem applies to the canonical wide-transition averaging scheme, but does not determine its best replacement. Defant and collaborators, *Projection Constants of Polynomial Spaces via Representation Theory*, arXiv:2609.22050, gives exact norms for accessible invariant *range* projections, rather than optimizing a non-projection transition band between two different spaces. The present statement concerns the sharp two-free-multiplier minimization, not those already-established principles.

## Limitations
The exact value is specified by a unique finite trigonometric system, not by a radical closed form. Printed decimals are numerical approximations. Uniqueness is established for the even convolution optimizer, not arbitrary non-translation-invariant optimizers. The result neither solves arbitrary reproduction/output degrees nor implies positivity (the optimum necessarily changes sign). A full historical-priority certification and an independent scientific audit have not been performed.

## References
1. H.-N. Wu, *Positivity loss in bandlimited spectral reproduction on spheres*, arXiv:2609.02695 (September 2, 2026), https://arxiv.org/abs/2609.02695.
2. B. Deregowska, S. Foucart, B. Lewandowska, L. Skrzypek, *On the Norms and Minimal Properties of de la Vallée Poussin's type Operators*, Monatshefte für Mathematik (2018), https://doi.org/10.1007/s00605-018-1159-x.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, P. Zadunaisky, *Projection Constants of Polynomial Spaces via Representation Theory*, arXiv:2609.22050 (September 18, 2026), https://arxiv.org/abs/2609.22050.
