# A finite-radius false-attractor transition for three-particle polarized Kalman inversion

## Finding

The deterministic, Gaussian-distance weighted, unbiased-covariance polarized ensemble Kalman inversion step has an exact scalar reduction on the invariant three-particle family \((-a,x,a)\). Its two outside particles already solve the observation equation, but the interior particle has an **unavoidable strictly positive limiting observation residual at every fixed positive polarization radius**. The transition at \(\kappa=a\) is a symmetry-breaking bifurcation, with an explicit critical slowing law.

Write \(\beta=a^2/\kappa^2\). For \(\kappa\ge a\), all interior states converge to 0. For \(0<\kappa<a\), the nonzero interior states converge according to their signs to \(\pm x_*\), the nonzero solutions of

\[
x_*=a\tanh\!\left(\frac{ax_*}{\kappa^2}\right),\qquad0<x_*<a.
\]

The observation residual of the limiting middle particle is \(a^2\) if \(\kappa\ge a\), and \(a^2-x_*^2>0\) if \(\kappa<a\). In the latter regime its residual decreases to zero only in the singular limit \(\kappa\downarrow0\).

At \(\kappa=a\), for every starting point \(x_0\in(-a,a)\setminus\{0\}\),

\[
\lim_{n\to\infty}\sqrt n\,|x_n|=a\sqrt{\frac{3}{2\omega_0}},\qquad
\omega_0=\frac{a^4}{a^4+2R(1+\tfrac12e^{-1/2})}.
\]

The stable branches satisfy the sharp local and strong-polarization asymptotics

\[
\frac{x_*}{a}\sim\sqrt{3\left(\frac{a^2}{\kappa^2}-1\right)}\quad (\kappa\uparrow a),\qquad
 a^2-x_*^2\sim4a^2e^{-2a^2/\kappa^2}\quad(\kappa\downarrow0).
\]

## Assumptions and scope

Fix \(a>0\), \(R>0\), and \(\kappa>0\). Let \(G(\theta)=\theta^2\) and \(y=a^2\), so the two exact solutions are \(-a\) and \(a\). Start the deterministic three-particle scheme at \((-a,x_0,a)\), where \(-a<x_0<a\). The Gaussian localization metric is the ordinary squared Euclidean distance. For the particle currently at \(z_i\), its weights are

\[
w_{ij}=\frac{\exp[-(z_i-z_j)^2/(2\kappa^2)]}{\sum_{\ell=1}^{3}\exp[-(z_i-z_\ell)^2/(2\kappa^2)]},\quad
D_i=1-\sum_{j=1}^{3}w_{ij}^2.
\]

Use weighted means and unbiased local cross- and output covariances,

\[
C_i^{\theta G}=D_i^{-1}\sum_jw_{ij}(z_j-\bar z_i)(G(z_j)-\bar G_i),\qquad
C_i^{GG}=D_i^{-1}\sum_jw_{ij}(G(z_j)-\bar G_i)^2,
\]

and repeat the deterministic fixed-ridge update

\[
z_i^+=z_i+\frac{C_i^{\theta G}}{C_i^{GG}+R}\bigl(y-G(z_i)\bigr).
\]

The analysis concerns this exact finite-ensemble, fixed-\(R\) iteration, without perturbed observations, extra projections, particle resampling, regularization updates, or adaptive polarization. All three particles are updated in parallel at each step. The two endpoints remain stationary because their innovations vanish.

## Proof

**1. Exact covariance reduction.** Fix an interior middle state \(x\in(-a,a)\) and define

\[
u=e^{-(x+a)^2/(2\kappa^2)},\quad v=e^{-(x-a)^2/(2\kappa^2)},\quad S=u+v,\quad P=uv.
\]

The middle particle has weights \((u,1,v)/(1+S)\). Directly evaluating the weighted means and centered sums gives

\[
D=\frac{2(S+P)}{(1+S)^2},\quad
C^{\theta G}=\frac{(x^2-a^2)[Sx-a(v-u)]}{2(S+P)},\quad
C^{GG}=\frac{S(a^2-x^2)^2}{2(S+P)}.
\]

Since \(S>0\), \(P>0\), and \(R>0\), every denominator is nonzero. Furthermore,

\[
\frac{v-u}{v+u}=\tanh\left(\frac{ax}{\kappa^2}\right).
\]

Substitution into the Kalman step and division by its positive denominator gives the **exact**, not asymptotic, map

\[
x^+=F(x)=(1-\omega(x))x+\omega(x)T(x),\qquad
T(x)=a\tanh\left(\frac{ax}{\kappa^2}\right),
\]

where

\[
\omega(x)=\frac{(a^2-x^2)^2}{(a^2-x^2)^2+2R(1+P/S)}.
\]

For all \(-a<x<a\), \(0<\omega(x)<1\) and \(-a<T(x)<a\); thus \(F\) maps the open interval strictly into itself. Also, \(F(x)=x\) if and only if \(T(x)=x\).

**2. Complete fixed-point and basin diagram.** The map \(T\) is odd and strictly increasing. For \(x>0\), \(T\) is strictly concave, satisfies \(T'(0)=a^2/\kappa^2=\beta\), and has \(T(a)<a\). If \(\beta\le1\), strict concavity implies \(0<T(x)<x\) for every \(x\in(0,a)\). Therefore \(F(x)\) lies strictly between \(T(x)\) and \(x\), and every positive orbit decreases to 0. Negative orbits follow by odd symmetry, while 0 is fixed.

If \(\beta>1\), strict concavity gives precisely one root \(x_*\in(0,a)\) of \(T(x)=x\), with \(T(x)>x\) below \(x_*\), and \(T(x)<x\) above \(x_*\). Monotonicity of \(T\), together with \(0<\omega<1\), makes the interval below \(x_*\) invariant with increasing orbits, and the interval above \(x_*\) invariant with decreasing orbits. Their limits must be fixed points and hence equal \(x_*\). By symmetry, negative states converge to \(-x_*\). The center 0 is a fixed point, repelling relative to every nonzero sufficiently close state. Because every possible interior limit has magnitude strictly below \(a\), its observation residual is strictly positive.

**3. Critical rate.** At \(\kappa=a\), \(T(x)=a\tanh(x/a)=x-x^3/(3a^2)+O(x^5)\). The relaxation factor \(\omega\) is smooth and even near 0, so \(\omega(x)=\omega_0+O(x^2)\) with the stated positive \(\omega_0\). Therefore

\[
x_{n+1}=x_n-\frac{\omega_0}{3a^2}x_n^3+O(x_n^5).
\]

Every nonzero orbit preserves its sign and tends to 0, and hence

\[
\frac1{x_{n+1}^2}-\frac1{x_n^2}\longrightarrow\frac{2\omega_0}{3a^2}.
\]

Cesàro averaging of this telescoping difference proves \(n x_n^2\to3a^2/(2\omega_0)\).

**4. Branch asymptotics.** With \(m=x_*/a\in(0,1)\), the fixed-point equation is \(\beta=\operatorname{artanh}(m)/m\). Near 0, \(\operatorname{artanh}(m)/m=1+m^2/3+O(m^4)\), yielding \(m\sim\sqrt{3(\beta-1)}\) as \(\beta\downarrow1\). As \(\beta\to\infty\), the same equation forces \(m\to1\); writing \(\delta=1-m=2/(1+e^{2\beta m})\) gives \(\delta\sim2e^{-2\beta}\) and \(1-m^2\sim4e^{-2\beta}\). This proves both stated asymptotics.

## Verification

The standalone `verify.py` computes the full three-particle weighted means and covariances independently of the closed-form reduction and checks the update against its closed-form formula across a grid of positive radii, ridges, amplitudes, and middle-particle positions. It also tests the attraction basins and the critical asymptotic at a large finite iteration count. The script passes 2,095 finite supplementary checks. Exact symbolic factorization of the weighted covariance numerators and denominator independently confirms the expressions in Step 1. The proof, not the numerical tests, establishes the infinite-time and all-parameter assertions.

For an illustrative choice \(a=1\), \(\kappa=0.7\), the positive attracting position is approximately \(0.9612168299\), with limiting raw observation residual approximately \(0.0760622059\). For \(\kappa\ge1\), the center tends to 0 and its raw residual equals 1.

## Relationship to prior work

Yang and Wu's arXiv:2610.31907v1 defines the Gaussian-distance polarized ensemble, biased-corrected local covariances, and positive-ridge Kalman update used here. Its published theorems bound finite-ensemble cross-cluster interaction and establish contraction for **linear** forward maps, not the exact nonlinear stationary basin or critical slowdown derived here. Its experiments acknowledge possible spurious clusters, but do not classify this three-particle quadratic mechanism.

Wacker's arXiv:2402.00027v3 develops locally weighted covariance EKI and its continuous-time dynamics; this supplies an important earlier local-covariance antecedent, including a framework from which the stationary equation in this symmetric example can be derived. The present result claims neither invention of local weighting nor of the classical Curie–Weiss scalar equation. Its asserted distinction is the **finite-ridge, discrete-time, unbiased-weighted PEKI reduction together with a global basin classification and an exact critical iterate rate**. Tong and Morzfeld's localized EKI, arXiv:2201.10821, concerns another localization mechanism and high-dimensional convergence.

## Limitations

The theorem is confined to one-dimensional quadratic observations, three particles with two exactly data-consistent stationary endpoints, Gaussian particle-distance weights, and deterministic fixed-ridge iteration. It does not assert that a large or noisy ensemble fails to recover either true mode, nor that false middle-particle states constitute distinct posterior clusters after post-processing. The infinite-iteration analysis is of a fixed update map; it is not a uniform-in-horizon guarantee or failure for a prescribed finite number of noisy updates with a horizon-dependent noise matrix. Floating-point weights may underflow for extremely small radii although the mathematical weights stay positive. General prior work on local Kalman dynamics may contain related implied specializations; historical uniqueness is not independently certified.

## References

1. H. Yang and J.-L. Wu, *Polarized Ensemble Kalman Inversion: A Derivative-Free Method for Multimodal Inverse Problems with Non-asymptotic Analysis*, arXiv:2610.31907v1 (first submitted 2026-10-22), https://arxiv.org/html/2610.31907v1.
2. P. Wacker, *Perspectives on locally weighted ensemble Kalman methods*, arXiv:2402.00027v3 (first submitted 2024-01-06; revision 2025-05-06), https://arxiv.org/html/2402.00027v3.
3. X. T. Tong and M. Morzfeld, *Localized ensemble Kalman inversion*, *Inverse Problems* 39 (2023), 064002, arXiv:2201.10821, https://arxiv.org/abs/2201.10821.
