# Critical contact-feedback decay and matched endemic onset in adaptive SIS dynamics

## Finding

For the two-dimensional adaptive susceptible–infected–susceptible (SIS) model of Achterberg and Sensi, nondecreasing contact breaking and nonincreasing contact creation yield an exact coefficient shared by the critical extinction tail and the endemic branch emerging at the threshold. Define the prevalence-dependent target contact density
\[
Z(y)=\frac{\xi C(y)}{\zeta B(y)+\xi C(y)},\qquad z_0=Z(0),\qquad \tau_c=\frac1{z_0},
\]
and its contact-feedback curvature parameter
\[
K=1-\tau_c Z'(0)
 =1+\frac{\zeta[\,C(0)B'(0)-B(0)C'(0)\,]}{C(0)[\,\zeta B(0)+\xi C(0)\,]}\ge1.
\]
At the exact epidemic threshold \(\tau=\tau_c\), every trajectory with initially positive infection obeys
\[
\lim_{t\to\infty}t y(t)=\frac1K,\qquad
\lim_{t\to\infty}t(z(t)-z_0)=\frac{Z'(0)}K.
\]
If \(r=\tau z_0-1\downarrow0\) through positive values, the endemic equilibrium has the **matched onset law**
\[
y_*(r)=\frac{r}{K}+O(r^2),\qquad
z_*(r)=z_0+\frac{Z'(0)}K r+O(r^2).
\]
The same contact-slope coefficient therefore determines both the algebraic critical extinction rate and the small-supercritical endemic fraction. This coefficient is unchanged when both contact-adjustment rates are multiplied by the same positive constant. Subcritical infection decays exponentially, whereas the unique supercritical endemic equilibrium attracts every solution with initially positive infection.

## Assumptions and scope

All time variables below are measured in units of the infectious recovery time. Consider
\[
\dot y=y[-1+\tau(1-y)z],\qquad
\dot z=-\zeta z B(y)+\xi(1-z)C(y),
\]
for \(t\ge0\), with infection prevalence \(y\in[0,1]\), contact density \(z\in[0,1]\), and strictly positive constants \(\tau,\zeta,\xi\). Assume \(B,C\in C^2([0,1])\), \(B(0)\ge0\), \(B(y)>0\) for all \(0<y\le1\), \(B'(y)\ge0\), \(C(y)>0\), and \(C'(y)\le0\) everywhere on \([0,1]\). All conclusions hold for every \(0<y(0)\le1\) and every \(z(0)\in[0,1]\).

Write \(k(y)=\zeta B(y)+\xi C(y)\); then \(k(y)>0\), and the second equation is \(\dot z=-k(y)[z-Z(y)]\). The disease-free equilibrium is \((0,z_0)\), the reproduction number is \(\mathcal R_0=\tau z_0\), and \(\tau_c=1/z_0\). Explicitly,
\[
Z'(0)=\frac{\xi\zeta[\,B(0)C'(0)-C(0)B'(0)\,]}{[\,\zeta B(0)+\xi C(0)\,]^2}\le0.
\]
In particular \(K=1-\tau_c Z'(0)\ge1\). The strict positivity of \(C\) is material: it excludes degenerate zero-contact disease-free states. For positive infection, the contact coordinate is eventually interior, even if initialized on the boundary.

## Proof

**Forward invariance and contact envelope.** The vector field points inward at \(y=1\) and \(z=0\), is tangent at \(y=0\), and points inward or tangent at \(z=1\). Infected fractions initially positive remain positive at all finite times. Differentiating \(Z\) gives \(Z'(y)\le0\). Let \(k_{\min}=\min_{[0,1]}k>0\). Since \(Z(y)\le z_0\), the scalar comparison theorem yields
\[
z(t)\le z_0+\bigl(z(0)-z_0\bigr)_+e^{-k_{\min}t}.
\]
This bound needs no assumption of initially equilibrated contacts.

**At and below the threshold.** For \(\mathcal R_0<1\), the envelope gives
\[
\frac{\dot y}{y}\le\mathcal R_0-1+\tau\bigl(z(0)-z_0\bigr)_+e^{-k_{\min}t},
\]
so prevalence decays exponentially. At equality \(\mathcal R_0=1\), the same inequality retaining the susceptible factor gives
\[
\dot y\le-y^2+\tau\bigl(z(0)-z_0\bigr)_+e^{-k_{\min}t}y.
\]
Multiplication by an integrating factor bounded above and away from zero reduces this to a Riccati comparison, proving \(y(t)=O(1/t)\) and hence \(y(t)\to0\). In either case, stable scalar contact relaxation, \(\dot z=-k(y)[z-Z(y)]\), gives \(z(t)\to z_0\).

**Critical coefficient.** Put \(w=z-z_0\), \(u=w/y\), and \(r_t=\dot y/y\). The exact quotient equation is
\[
\dot u=-[k(y)+r_t]u+k(y)\frac{Z(y)-z_0}{y}.
\]
At the critical threshold, \(y\to0\), \(z\to z_0\), and therefore \(r_t\to0\). By differentiability, the coefficient of \(u\) tends to \(-k(0)<0\), while the forcing tends to \(k(0)Z'(0)\). Variation of constants for an asymptotically stable scalar linear equation gives
\[
\lim_{t\to\infty}u(t)=Z'(0).
\]
Using \(\tau_c z_0=1\), an exact rearrangement of the infection equation gives
\[
\left(\frac1y\right)'=1-\tau_c\frac{z-z_0}{y}+\tau_c(z-z_0)\longrightarrow 1-\tau_c Z'(0)=K.
\]
Integrating and dividing by \(t\) now yields \(t y(t)\to1/K\). Finally \(t w(t)=(t y(t))u(t)\to Z'(0)/K\).

**Endemic uniqueness, attraction, and onset.** When \(\mathcal R_0>1\), any positive equilibrium has \(z=Z(y)\) and solves
\[
\tau(1-y)Z(y)=1.
\]
The left side is strictly decreasing from \(\mathcal R_0>1\) to zero on \([0,1]\); thus there is exactly one root \(y_*\in(0,1)\). Here \(0<Z(y_*)<1\). Its Jacobian has strictly negative trace and positive determinant because the infection self-derivative equals \(-\tau y_*z_*<0\), the infection-to-contact derivative is positive, and the contact-to-infection derivative is nonpositive. The disease-free equilibrium is a saddle with stable manifold contained in \(y=0\). In the interior, the Dulac multiplier \(1/(yz)\) gives divergence \(-\tau-\xi C(y)/(yz^2)<0\), so nonconstant periodic orbits are impossible. The positive-infection boundary is inward-pointing, and planar limit-set theory then yields attraction to the unique endemic sink for all \(y(0)>0\). The absence of cycles, and conditional uniqueness-implies-global-attraction argument, were already developed in the source paper and are used here, not claimed as new.

For the quantitative branch, set \(r=\tau z_0-1\) and \(\tau=\tau_c(1+r)\). Taylor expansion of \(\tau(1-y)Z(y)=1\) at \((r,y)=(0,0)\) has first-order part \(r-Ky\). The implicit-function theorem, since \(K>0\), yields \(y_*(r)=r/K+O(r^2)\), then \(z_*(r)=Z(y_*(r))=z_0+Z'(0)r/K+O(r^2)\). Both \(K\) and \(Z'(0)\) involve \(\zeta,\xi\) only through their ratio: their common scaling changes transient contact relaxation but not either leading asymptotic coefficient.

## Verification

Run `python verify.py` after installing the packages from `requirements.txt`. Symbolic derivatives and exact fractions verify the contact slopes and shared prefactors for four admissible response/rate settings. Numerical ODE integrations to normalized times \(30{,}000\) or \(40{,}000\) corroborate the critical time-weighted limits. Three small positive excess values independently test the endemic onset slope by root solving.

In particular, \(B(y)=1+y\), \(C(y)=1-y/2\), \(\zeta=\xi=1\) give \(z_0=1/2\), \(Z'(0)=-3/8\), and \(K=7/4\). Hence the exact predictions are \(t y(t)\to4/7\) and \(t(z(t)-1/2)\to-3/14\); at time \(30{,}000\), the script gives approximately \(0.571381\) and \(-0.214270\), respectively. The prevalence-proportional breaking example gives \(K=3\), and quadratic contact breaking gives \(K=1\). These calculations corroborate but do not substitute for the infinite-time proof.

## Relationship to prior work

Achterberg and Sensi introduced this exact two-equation adaptive SIS system, established its disease-free reproduction number, proved the absence of periodic orbits, and derived examples of endemic equilibria and stability. Those foundational and qualitative statements are not new. In their Sections 3–4 they leave the equality cases of several local stability tests unresolved and ask which response functions guarantee endemic uniqueness. The present result supplies an explicit quantitative critical-decay coefficient and its equality with the supercritical endemic-onset slope throughout a natural class of monotone responses, including both positive baseline breaking and breaking that vanishes at zero prevalence. The original paper gives neither this general critical-time law nor its contact-density asymptotic.

The later multigroup extension by Achterberg, Sensi and Sottile assumes monotone contact responses and proves disease-free stability for \(\mathcal R_0<1\), alongside multigroup equilibrium results and examples of oscillations. Its strictly subcritical statement is consistent with, but does not imply, the exact \(\mathcal R_0=1\) law or the matched onset coefficient in the one-group limit. More general critical-rate results for other epidemic systems are not proofs of this coefficient without an explicit reduction of their dynamics to these equations.

## Limitations

This is a deterministic mean-field theorem with smooth, monotone contact responses and strictly positive creation activity. It does not cover vanishing contact creation, nonmonotone behavioral feedback, multiple communities, delays, stochastic finite-population extinction, or arbitrary time dependence in parameters. The critical time is normalized by the recovery rate; unnormalized physical time changes the numerical coefficient accordingly. No universal finite-time error estimate for the \(t^{-1}\) asymptotic is claimed. Qualitative uniqueness/global convergence overlap known dynamical-systems methods; the distinct contribution is the matched critical and endemic coefficients and their precise assumptions.

## References

1. M. A. Achterberg and M. Sensi, *A minimal model for adaptive SIS epidemics*, first public arXiv submission 2022-09-02, arXiv:2209.01224; *Nonlinear Dynamics* **111** (2023), 12657–12670, doi:10.1007/s11071-023-08498-4. Full open-access article: https://link.springer.com/article/10.1007/s11071-023-08498-4.
2. M. A. Achterberg, M. Sensi and S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, first public arXiv submission 2024-07-24, arXiv:2407.17639; *Chaos* **35** (2025), 033127, doi:10.1063/5.0246228. Full online preprint: https://arxiv.org/abs/2407.17639.
3. Classical Bendixson–Dulac criterion and Poincaré–Bendixson planar limit-set theory (standard results; the system-specific Dulac expression is reproduced above).
