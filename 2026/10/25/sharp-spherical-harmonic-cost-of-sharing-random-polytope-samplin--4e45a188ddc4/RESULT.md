# Sharp spherical-harmonic cost of sharing random-polytope sampling laws

## Finding

Fix an integer \(d\ge3\), a nonempty index set \(J\subseteq\{1,\ldots,d\}\) with at least two members, and a fixed real \(f\in C^4(S^{d-1})\). For all sufficiently small real \(\varepsilon\), let \(K_\varepsilon\subset\mathbb R^d\) be the strictly convex body with boundary
\[
\partial K_\varepsilon=\{(1+\varepsilon f(u))u:u\in S^{d-1}\}.
\]
Let \(\kappa\) be its Gauss curvature, \(H_m\) the normalized \(m\)-th elementary symmetric function of its principal curvatures (\(H_0=1\)), and \(dS_\varepsilon\) its surface-area element. Define, for a strictly positive continuous probability density \(\rho\) relative to \(dS_\varepsilon\),
\[
\mathcal I_j(K_\varepsilon,\rho)
=\int_{\partial K_\varepsilon}
\kappa^{1/(d-1)}H_{d-j}\rho^{-2/(d-1)}\,dS_\varepsilon,
\quad
M_j(K_\varepsilon)=\min_\rho\mathcal I_j(K_\varepsilon,\rho).
\]
These are the leading coefficients, apart from index-dependent positive constants, of the expected intrinsic-volume losses of random polytopes sampled from the boundary. Define the best single-sampler worst relative loss
\[
T_J(\varepsilon)=\inf_\rho\max_{j\in J}
\frac{\mathcal I_j(K_\varepsilon,\rho)}{M_j(K_\varepsilon)}.
\]
Use the spherical Laplacian convention \(\Delta_S Y_\ell=-\ell(\ell+d-2)Y_\ell\). Let \(\sigma\) be probability surface measure on \(S^{d-1}\), and put
\[
g=(\Delta_S+d-1)f,
\qquad
V_f=\int_{S^{d-1}}\left(g-\int g\,d\sigma\right)^2d\sigma.
\]
**Theorem (sharp minimax expansion).** With \(j_-=\min J\) and \(j_+=\max J\),
\[
\boxed{
T_J(\varepsilon)=1+
\frac{(j_+-j_-)^2}{4(d-1)^2(d+1)}
V_f\,\varepsilon^2+O_{d,J,f}(|\varepsilon|^3).
}
\]
Thus, to second order, *only the two extreme intrinsic-volume indices matter*, however many intermediate indices are included. The quadratic form vanishes precisely for perturbations consisting only of a constant and a degree-one spherical harmonic.

Write \(f=\sum_{\ell\ge0}f_\ell\) for the orthogonal spherical-harmonic decomposition. The quadratic form has the exact spectral representation
\[
V_f=\sum_{\ell\ge2}
\left[\ell(\ell+d-2)-(d-1)\right]^2
\|f_\ell\|_{L^2(\sigma)}^2.
\]
In particular, the sharp, dimension-dependent stability constant is
\[
\boxed{
\lim_{\varepsilon\to0}
\frac{T_J(\varepsilon)-1}{\varepsilon^2}
\ge
\frac{(j_+-j_-)^2(d+1)}{4(d-1)^2}
\|\Pi_{\ge2}f\|_{L^2(\sigma)}^2.
}
\]
Equality holds in this coefficient bound for every nonzero pure degree-two harmonic, possibly with added constant and degree-one harmonics; the constant cannot be improved.

A fully explicit example is \(d=3\), \(J=\{1,2,3\}\), and \(f(u)=\tfrac12(3u_3^2-1)\). Then \(V_f=16/5\) and
\[
\boxed{T_{\{1,2,3\}}(\varepsilon)
=1+\tfrac15\varepsilon^2+O(|\varepsilon|^3).}
\]

## Assumptions and scope

The perturbation \(f\) is fixed while \(\varepsilon\to0\); all implied constants may depend on \(d,J,f\). Smallness of \(|\varepsilon|\) guarantees a positive radial function and positive principal curvatures. The boundary sampling density is fixed as the number of sampled points tends to infinity; the assertion is a theorem about their *separately normalized leading expected intrinsic-volume coefficients*, not about minimizing finite-sample expectations or uniform-in-density asymptotic remainders. All surface integrals over the perturbed body use Euclidean \((d-1)\)-dimensional area.

The primary MSC2020 classification is 52A27; random-polytope intrinsic-volume asymptotics are the motivating geometric setting. Dimensions \(d\ge3\) are stated explicitly: the planar ellipse minimax case is already present in published work and is not a novelty claim here.

## Proof

**Step 1: source-supported normalized functionals.** The boundary-sampling asymptotic formula gives the curvature weight
\[
w_j=\kappa^{1/(d-1)}H_{d-j},\qquad
\beta=\frac{d+1}{d-1}>1,
\]
so \(\mathcal I_j=\int w_j\rho^{1-\beta}dS_\varepsilon\). Hölder's inequality uniquely minimizes this at
\[
\rho_j=\frac{w_j^{1/\beta}}{\int w_j^{1/\beta}\,dS_\varepsilon}.
\]
Put \(L_\varepsilon=\int dS_\varepsilon\), \(d\mu_\varepsilon=dS_\varepsilon/L_\varepsilon\), and \(p_j=L_\varepsilon\rho_j\). Thus \(\int p_j\,d\mu_\varepsilon=1\). Every admissible common density corresponds to \(r=L_\varepsilon\rho>0\) of \(\mu_\varepsilon\)-mean one, with exact normalized loss
\[
R_j(r)=\frac{\mathcal I_j}{M_j}
=\int p_j^\beta r^{1-\beta}\,d\mu_\varepsilon.
\]
In particular \(\min_r R_j(r)=1\), attained at \(r=p_j\).

**Step 2: curvature linearization.** The shape operator of the radial graph satisfies, uniformly on the sphere,
\[
S_\varepsilon=I-\varepsilon(\nabla_S^2f+fI)+O_f(\varepsilon^2).
\]
Taking normalized elementary symmetric polynomials gives
\[
H_m=1-\varepsilon\frac{m}{d-1}g+O_f(\varepsilon^2),
\quad\kappa=1-\varepsilon g+O_f(\varepsilon^2),
\]
with \(g=(\Delta_S+d-1)f\). Therefore
\[
\log w_j=-\varepsilon\frac{d-j+1}{d-1}g+O_f(\varepsilon^2).
\]
On normalizing the optimal density against \(\mu_\varepsilon\),
\[
p_j=1+\varepsilon u_j+O_f(\varepsilon^2),\qquad
u_j=-\frac{d-j+1}{d+1}(g-\overline g),
\quad\overline g=\int g\,d\sigma.
\]
Here and below remainder bounds are uniform in the spherical direction; \(\mu_\varepsilon\) converges smoothly to \(\sigma\). The coefficient functions \(u_j\) are collinear and affine in \(j\).

**Step 3: a universal sharp endpoint lower bound.** Denote \(p_-=p_{j_-}\) and \(p_+=p_{j_+}\). Every common \(r\) obeys
\[
\max_{j\in J}R_j(r)\ge\tfrac12\bigl(R_{j_-}(r)+R_{j_+}(r)\bigr).
\]
The equality case of Hölder's inequality gives the exact average-risk infimum
\[
Z_\varepsilon^\beta,
\quad
Z_\varepsilon=\int
\left(\frac{p_-^\beta+p_+^\beta}{2}\right)^{1/\beta}
\,d\mu_\varepsilon.
\]
Set \(\delta_\pm=p_\pm-1\), which have \(\mu_\varepsilon\)-mean zero. Taylor expansion under the integral gives
\[
Z_\varepsilon
=1+\frac{\beta-1}{8}
\int(\delta_+-\delta_-)^2\,d\mu_\varepsilon
+O_f(|\varepsilon|^3).
\]
Consequently
\[
T_J(\varepsilon)\ge
1+\frac{\beta(\beta-1)}8
\frac{(j_+-j_-)^2}{(d+1)^2}
V_f\varepsilon^2+O_f(|\varepsilon|^3).
\]

**Step 4: the matching one-density construction.** Choose
\[
r_{\rm mid}=
\frac{\sqrt{p_-p_+}}{\int\sqrt{p_-p_+}\,d\mu_\varepsilon}.
\]
Its first variation is \(r_{\rm mid}=1+\varepsilon(u_-+u_+)/2+O_f(\varepsilon^2)\). Direct Taylor expansion, using the exact mean-one constraints on \(p_j\) and \(r_{\rm mid}\), shows for each \(j\in J\)
\[
R_j(r_{\rm mid})
=1+\frac{\beta(\beta-1)}2\varepsilon^2
\left\|u_j-\frac{u_-+u_+}{2}\right\|_{L^2(\sigma)}^2
+O_f(|\varepsilon|^3).
\]
Since \(u_j\) lies on the line segment joining \(u_-\) and \(u_+\), the maximal quadratic term occurs at an endpoint. Thus the upper bound equals the lower bound from Step 3. Substituting \(\beta=(d+1)/(d-1)\) yields exactly \((j_+-j_-)^2/[4(d-1)^2(d+1)]\), proving the expansion.

**Step 5: spectrum and sharpness.** Spherical harmonics diagonalize \(\Delta_S\), with eigenvalues \(-\ell(\ell+d-2)\). Subtracting the mean removes degree zero, while the multiplier at degree one is exactly zero. The smallest nonzero absolute multiplier is \(d+1\), occurring at degree two; all degrees \(\ell\ge3\) have larger multipliers. Orthogonality proves the spectral formula and optimal coercivity constant. For \(d=3\), the normalized degree-two zonal harmonic \(P_2(u_3)\) has squared norm \(1/5\), and \((\Delta_S+2)P_2=-4P_2\), giving \(V_f=16/5\) and the claimed coefficient \(1/5\).

## Verification

The bundled standalone `verify_spherical_minimax.py` computes the two principal curvatures of the explicitly specified three-dimensional quadrupole radial graph from its meridional parametrization. It separately constructs each curvature-optimal density, computes the exact dual endpoint average-cost lower bound by a one-dimensional scalar bisection, and evaluates the three-objective loss of the constructive geometric-mean density. Both bounds converge to the analytic coefficient \(1/5\). It also checks the degree-two spherical eigenvalue and norm. Run `python verify_spherical_minimax.py`; expected marker `CURVATURE_MINIMAX_QUADRATURE_OK`.

The symbolic all-dimension argument above establishes the theorem; quadrature is only a reproducibility check on one nontrivial family. It does not certify infinitely many dimensions, shapes, or all densities by sampling.

## Relationship to prior work

The motivating 2026 paper by Hoehner establishes the leading curvature-weighted intrinsic-volume errors, their unique separate optimal sampling densities, and rigidity: two individual optima coincide only on balls. Its Theorem 3.1 gives the curvature-weighted sampling functional, Lemma 3.3 determines each individually minimizing density, and Theorem 3.4 proves qualitative rigidity. It does not derive the universal near-sphere worst-risk coefficient, its harmonic spectrum, or the all-index endpoint law; the two-endpoint average-risk lower bound used here is derived in Step 3.

A published planar-ellipse result identifies a unique exact minimax area/perimeter sampler and its \(3/8\) small-eccentricity coefficient. That result is restricted to \(d=2\), two objectives, and ellipses, and does not imply the stated \(d\ge3\) all-intrinsic-volume quadratic spectral law. A separate published Hellinger calculation measures the distance between volume-optimal and mean-width-optimal sampling laws; its probability-distance identity is not a minimax expected-deficit calculation and has no spherical-harmonic endpoint formula. The 2011 random-boundary-polytope theorem provides the source asymptotic weights, not this optimization and stability result.

## Limitations

The result is local in a fixed \(C^4\) radial deformation and concerns only the leading random-polytope expected intrinsic-volume asymptotics. It gives no global geometric-distance stability inequality, no uniform error in an unrestricted family of deformations, and no finite-sample optimal sampler. Terms beyond order \(\varepsilon^2\) are not determined. The known planar ellipse theorem covers that restricted special case; no novelty is asserted for it. Search-based priority cannot exclude unindexed perturbation-theoretic work, and an independent scientific audit has not been performed.

## References

1. S. Hoehner, *One polytope fits all: Characterization of the Euclidean ball via simultaneous intrinsic volume approximation*, first submitted 20 February 2026, arXiv:2602.18547v1, especially §3.1, Theorem 3.1, Lemma 3.3 and Theorem 3.4. https://arxiv.org/abs/2602.18547
2. K. J. Böröczky, F. Fodor and D. Hug, *Intrinsic volumes of random polytopes with vertices on the boundary of a convex body*, Trans. Amer. Math. Soc. 365 (2013), 785–809; arXiv:1103.4978v1, Theorem 1.1. https://arxiv.org/html/1103.4978v1
3. F. Besau, S. Hoehner and G. Kur, *Intrinsic and Dual Volume Deviations of Convex Bodies and Polytopes*, IMRN 2021 (22), 17456–17513; arXiv:1905.08862. https://arxiv.org/abs/1905.08862
4. *Unique minimax area–perimeter sampling law for random polygons in ellipses*, published mathematical research record (11 October 2026), identifier 179adc1046b6.
5. *Exact Hellinger curvature gap for optimal polytope vertex laws*, published mathematical research record (11 October 2026), identifier 6c90b94614f1.
