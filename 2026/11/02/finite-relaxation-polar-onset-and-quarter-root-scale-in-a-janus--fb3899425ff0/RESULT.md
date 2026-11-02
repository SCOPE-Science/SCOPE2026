# Finite-relaxation polar onset and quarter-root scale in a Janus chemical slab

## Finding

**Theorem (unique stationary polar threshold despite finite chemical relaxation).** Fix positive parameters \(D_t,D_c,D_r,H,\kappa\) and a positive chemical-to-polarization gain \(G\). In the orientation-only sector of the first-order Janus source-dipole slab model defined below, for each nonzero horizontal Fourier wavenumber \(q>0\), the coupled polar–chemical generator has **only real spectrum**, although the solute has its full finite diffusion time. A growing mode exists precisely when

\[
G>F(q),\qquad F(q)=\left(D_t+\frac{D_r}{q^2}\right)\left(\kappa+D_c q\coth(Hq)\right).
\]

The function \(F\) has exactly one global minimizer \(q_*>0\), for every positive set of parameters. Writing \(G_c=F(q_*)\): if \(G<G_c\), every nonzero Fourier mode is linearly stable; at \(G=G_c\) there is exactly one neutral wavenumber \(q_*\); if \(G>G_c\), precisely one open interval \((q_-,q_+)\) of wavenumbers has a positive eigenvalue. Each such eigenvalue is real and simple. Its growth rate \(s_q>0\) is strictly less than the corresponding quasistatic prediction \(s_{\mathrm{qs}}(q)=Gq^2/[\kappa+D_cq\coth(Hq)]-(D_r+D_tq^2)\). Thus finite chemical relaxation preserves the threshold but strictly slows unstable growth. An oscillatory/Hopf linear onset cannot arise in this sector merely from finite solute relaxation.

As \(D_r\downarrow0\), with \(D_t,D_c,H,\kappa\) fixed, the unique critical wave number and gain satisfy

\[
q_*\sim\left[\frac{3D_r(\kappa H+D_c)}{D_tD_cH^2}\right]^{1/4},
\]

\[
G_c=D_t\left(\kappa+\frac{D_c}{H}\right)
+2\sqrt{\frac{D_tD_rD_c(\kappa H+D_c)}{3}}+O(D_r).
\]

These are spectral statements for the specified linearized equations, not a theorem of nonlinear pattern formation or of the full self-propelled Janus model.

## Assumptions and scope

Particles lie in a two-dimensional substrate plane and their consumed solute occupies the slab \(0<z<H\). The top concentration is pinned by a reservoir, and the bottom surface consumes solute. Constant positive solute diffusivity \(D_c\) is assumed (the hindered-diffusivity layer is switched off). The mean particle number density is \(\rho_0>0\), the surface consumption rate is \(h>0\), and \(\kappa=h\rho_0\). The uniform substrate-plane state has concentration \(c_0=c_\infty/(1+\kappa H/D_c)>0\) at its bottom wall. The source displacement has amplitude \(\varepsilon>0\) and is retained only through first order in \(\varepsilon\).

The translational phoretic mobility is set to \(\mu=0\); thus particles translate diffusively, **not by chemical self-propulsion**. Their planar orientation still responds to chemical gradients, with torque coefficient \(\mu'<0\), and undergoes rotational diffusion \(D_r>0\). This isolates the positive polar-feedback channel rather than modeling the source paper's entire clustering phase. All Fourier wavenumbers in the mathematical first-order model are considered; for a physical dipole expansion one must additionally check \(q\varepsilon\ll1\) near the selected wavenumber. No vertical colloidal motion, excluded-volume drift, or density-dependent solute diffusivity is included.

For a nonzero horizontal Fourier wave vector rotated to \((q,0)\), let \(w\) denote the longitudinal first angular harmonic in the normalization \(w=i(\delta\rho_1+\delta\rho_{-1})\), and \(C(z,t)\) the solute perturbation. The orientation-only block of the linearization is the following closed linear system:

\[
\begin{aligned}
\partial_t w&=-a_qw+b_qC(0,t),&a_q&=D_r+D_tq^2,\\
\partial_t C&=D_c(\partial_z^2-q^2)C,&0&<z<H,\\
C(H,t)&=0,&D_c\partial_z C(0,t)&=\kappa C(0,t)-f_qw,
\end{aligned}
\]

where

\[
b_q=-\frac{\mu'\rho_0q}{2\pi}>0,\quad
f_q=\frac{hc_0\varepsilon q}{2}>0,\quad
G=\frac{b_qf_q}{q^2}=-\frac{\mu'\rho_0hc_0\varepsilon}{4\pi}>0.
\]

This sector is obtained from the source model's particle and solute equations, before imposing its fast-solute limit. The density mode is independently damped at rate \(D_tq^2\), but it can *force* the chemical field in the full triangular system; transverse polarization and higher angular harmonics are independently damped. The neutral density conservation mode at \(q=0\) is excluded from the positive-growth statement.

## Proof

**Step 1: exact solute resolvent.** For a temporal exponential mode \(e^{st}\) with \(\Re s\ge0\), put \(m=\sqrt{q^2+s/D_c}\) with positive real part. The unique bulk solution with bottom value \(C_s\) and zero top value is

\[
C(z)=C_s\frac{\sinh(m(H-z))}{\sinh(mH)}.
\]

The bottom boundary condition therefore gives

\[
C_s=f_q w H_q(s),\qquad
H_q(s)=\left[\kappa+D_cm\coth(Hm)\right]^{-1}.
\]

The coupled dispersion equation is

\[
s+a_q=Gq^2 H_q(s).\tag{1}
\]

At \(s=0\), Eq. (1) reduces exactly to \(G=F(q)\). The sign and normalizations match the source paper's Fourier chemical response, with its quasistatic value recovered at \(s=0\).

**Step 2: chemical relaxation cannot create complex eigenvalues in the polar block.** Set \(\alpha_q=f_q/b_q>0\) and equip \(\mathbb R\oplus L^2(0,H)\) with inner product

\[
\langle(w,C),(v,E)\rangle_q=\alpha_qwv+\int_0^H CE\,dz.
\]

The negative of the coupled generator has the symmetric quadratic form

\[
\begin{aligned}
\mathfrak a_q[(w,C),(v,E)]={}&\alpha_q a_qwv
+D_c\int_0^H(C'E'+q^2CE)\,dz\\
&+\kappa C(0)E(0)-f_q\bigl[wE(0)+vC(0)\bigr].
\end{aligned}
\]

Its form domain consists of scalar \(w\) and \(H^1\) functions vanishing at \(H\). The trace bound controls the two off-diagonal terms; thus the form is closed and bounded below. Integration by parts recovers exactly the PDE and the bottom boundary condition, including the scalar equation because \(\alpha_q b_q=f_q\). By the representation theorem, the generator is self-adjoint in the weighted space. Compactness of the form embedding gives discrete **real** spectrum. Adding the independent stable density/transverse/angular blocks does not introduce a nonreal unstable eigenvalue in the orientation-only model. In particular no nonzero purely imaginary spectral crossing exists for any positive parameter choice.

For a direct check independent of the symmetrization, the Robin–Dirichlet Laplacian has positive eigenvalues \(\lambda_{n,q}\) and normalized real eigenfunctions \(\phi_{n,q}\); its surface response has a convergent positive Stieltjes expansion

\[
H_q(s)=\sum_{n\ge1}\frac{|\phi_{n,q}(0)|^2}{s+\lambda_{n,q}}.
\]

For \(\Re s\ge0\), \(H_q\) is positive and strictly decreasing on the nonnegative real axis; it has negative imaginary part in the upper half-plane. Thus the two sides of (1) cannot match for a nonreal \(s\) in the closed right half-plane. Its real left-minus-right side is strictly increasing for \(s\ge0\), tends to infinity, and vanishes at a unique positive \(s\) precisely when \(Gq^2H_q(0)>a_q\), equivalently \(G>F(q)\). Because \(H_q(s)<H_q(0)\) for positive real \(s\), this growing root satisfies \(0<s_q<Gq^2H_q(0)-a_q\), proving strict growth suppression relative to instantaneous solute equilibration. If the reverse inequality holds, the Stieltjes bound \(|H_q(s)|\le H_q(0)\) for \(\Re s\ge0\) excludes every positive-growth or imaginary-axis eigenvalue except the stationary neutral crossing at equality.

**Step 3: exactly one preferred finite wavelength.** Put

\[
y=Hq,\qquad U=\frac{D_c}{\kappa H},\qquad \beta=\frac{D_rH^2}{D_t},\qquad t(y)=y\coth y.
\]

Then \(F=D_t\kappa(1+\beta/y^2)(1+Ut(y))\). Differentiation shows that \(F'=0\) is equivalent to

\[
\beta=B_U(y):=\frac{Uy^3t'(y)}{2+U[2t(y)-yt'(y)]}.
\]

For every \(y>0\), \(t'(y)>0\), \(t''(y)=2\operatorname{csch}^2y\,[y\coth y-1]>0\), and \(t(y)-yt'(y)=y^2\operatorname{csch}^2y>0\). If \(M(y)=2+U[2t(y)-yt'(y)]\), then \(M>Ut\) and \(M'=U(t'-yt'')\le Ut'\). It follows that \(M'/M<t'/t<1/y\). Consequently

\[
\frac{B'_U(y)}{B_U(y)}=\frac3y+\frac{t''}{t'}-\frac{M'}M>\frac2y>0.
\]

As \(y\downarrow0\), \(B_U(y)\sim Uy^4/[3(1+U)]\), while \(B_U(y)\sim y^2\) as \(y\to\infty\). Hence the equation \(\beta=B_U(y)\) has exactly one solution. Since \(F(q)\to\infty\) at both endpoints \(q\downarrow0\), \(q\to\infty\), this stationary point is the unique global minimum. Strict decrease then increase give exactly two crossings of a higher horizontal level \(G>G_c\), creating one unstable finite-wavenumber band.

**Step 4: critical small-rotation limit.** Let \(A=\kappa+D_c/H\) and \(K=D_cH/3\). As \(q\to0\),

\[
F(q)=D_t A+\frac{D_r A}{q^2}+D_tKq^2+O(D_r+q^4).
\]

The previous monotonic characterization yields \(q_*\to0\) and \(q_*^4\sim D_rA/(D_tK)\), giving the quarter-root formula. Evaluating \(F\) there gives \(G_c=D_tA+2\sqrt{D_tKD_rA}+O(D_r)\), which is the stated half-power threshold correction. All limits hold with the other four parameters fixed and positive.

## Verification

The companion `checker.py` program independently constructs the continuous-slab transfer function, solves the scalar growth-rate equation, calculates the unique stationary wave number by two algorithms, tests the small-rotation formulas, checks the Stieltjes imaginary-sign property, and compares against matrices obtained by finite-volume discretization of the **time-dependent bulk solute PDE**. Running `python checker.py` with NumPy and SciPy yields 220 deterministic numerical assertions passing. These calculations are finite checks, not substitutes for the preceding operator and calculus proofs.

For a dimensionless reference choice \(D_t=D_c=D_r=H=\kappa=1\), the critical mode and gain are approximately \(q_*=1.7214209\) and \(G_c=3.7918904\). The checker compares both stable and unstable sides of this boundary.

## Relationship to prior work

Mabillard, van Wijland, and Fournier (2026) provide the Janus particle/chemical equations, the displaced dipolar source, and the *quasistatic* solute Fourier response. Their linear stability analysis explicitly sets \(\partial_t\delta c=0\) (Appendix B, equations (39)–(49)) and treats a broader translationally self-propelled clustering model. In the zero-translational-mobility specialization, their displayed quasistatic matrix already implies the **stationary** polar neutral-curve expression. Neither that stationary feedback nor the basic possibility of a polar instability is claimed as new here. The claim concerns the corresponding **non-quasistatic** slab spectral classification, strict growth-rate suppression by finite solute time, the exact single-band geometry, and its low-rotation singular asymptotics.

Tucci, Golestanian, and Saha (2024) study density–polarization instabilities of Janus colloids, including a single-species polar channel (Appendix C) and Hopf transitions in active mixtures. Their eliminated/screened chemical response is a different geometry and does not yield the time-dependent finite-height Robin–Dirichlet surface operator treated here. Their work establishes important prior mechanisms and limits any broad claim of novel polar feedback or novel generic finite-wavenumber ordering. A quarter-root scale can also follow in other screened-chemical models by elementary minimization; no novelty of that exponent in isolation is asserted, only the exact coefficient for this finite-height consumption geometry in conjunction with the dynamic spectral theorem.

Liebchen, Marenduzzo, Pagonabarraga, and Cates (2015) already study anisotropic chemical production, dynamic chemical diffusion, aster-type Janus instability and delayed-orientation oscillations in a **two-dimensional volumetric reaction–diffusion** active-swimmer model. Thus chemical memory and polar feedback are not new in general. Their chemical field has volumetric production and bulk decay, rather than a three-dimensional finite-height slab coupled through a consuming **boundary flux**. The present slab theorem neither generalizes their full active-swimmer phase diagram nor contradicts its oscillations, which rely on additional density/self-propulsion feedback.

## Limitations

This is a linear theorem in an orientation-only, zero-phoretic-drift, constant-diffusivity, first-order-source approximation; it does not show that finite-amplitude polarized patterns form, nor predict the experimentally active self-propelled phase in the original article. Finite physical source displacement restricts accurate interpretation to wavenumbers satisfying \(q\varepsilon\ll1\). A finite horizontal box allows only discrete modes and may miss the continuum critical wavenumber. Nonzero translational mobility or multicomponent chemistry can destroy the symmetric-coupling structure and admit complex eigenvalues. A generic abstract positive-feedback theorem or a less obvious equivalent slab reduction in older literature may subsume portions of this result; publication priority requires independent expert checking.

## References

1. J. Mabillard, F. van Wijland and J.-B. Fournier, *Dynamic clustering of active chemotactic Janus particles*, arXiv:2610.26657v1 (first public 2026-10-19), https://arxiv.org/abs/2610.26657, particularly Section III.2 and Appendix B.
2. G. Tucci, R. Golestanian and S. Saha, *Nonreciprocal collective dynamics in a mixture of phoretic Janus colloids*, arXiv:2402.09279v1 (first public 2024-02-14), https://arxiv.org/abs/2402.09279, particularly Appendix C.
3. B. Liebchen, D. Marenduzzo, I. Pagonabarraga and M. E. Cates, *Clustering and pattern formation in chemorepulsive active colloids*, arXiv:1508.04673v1 (first public 2015-08-19), https://arxiv.org/abs/1508.04673, particularly its continuum density–polarization–chemical equations and linear dispersion analysis.
