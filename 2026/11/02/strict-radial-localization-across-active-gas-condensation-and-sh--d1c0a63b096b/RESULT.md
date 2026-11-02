# Strict radial localization across active-gas condensation and sharp exponential scaling laws

## Finding

Consider the explicit symmetric stationary **mean-field** density of a one-dimensional interacting run-and-tumble gas under instantaneous local Poisson resetting. Normalize its total mass to a spatial probability law. Increasing the reset rate makes the distance from the reset origin **strictly smaller in first-order stochastic order**, across the gas-to-droplet transition. This remains true even where the dense droplet's physical half-width grows with resetting. In the coexistence interval, the condensed profile is also strictly more localized than the supersaturated gas-only stationary profile at the same rate.

The whole scaled spatial law has two quantitative exponential limits. Its weak-reset limit is exponential of rate one, with a sharp first-order total-variation correction. Its strong-reset limit is exponential of rate \(\rho_m\), with an **exact**, nonzero total-variation discrepancy proportional to the residual gas mass.

Define
\[
\chi(r)=\frac{\sqrt{r(r+\alpha)}}{v_0},\qquad q=\frac{M\chi(r)}2,\qquad Y_q=\chi(r)|X_r|,
\]
where \(X_r\) has the normalized symmetric density \(\rho_r(x)/M\). For \(m=\rho_m\ge4\), let
\[
H_m(u)=\frac m2\left(1-\sqrt{1-4u/m}\right),\quad
J_m(a,b)=\int_a^b\frac{du}{H_m(u)},\quad 0<a\le b\le m/4.
\]
The upper-survival quantile \(y_q(s)\), defined uniquely by \(\Pr(Y_q>y_q(s))=s\) for \(0<s<1\), is exactly
\[
y_q(s)=
\begin{cases}
J_m(qs,q),&0<q\le1,\\[2pt]
\dfrac{\log q}{m}+J_m(qs,1),&q>1,\quad 0<s<1/q,\\[2pt]
\dfrac{\log(1/s)}{m},&q>1,\quad 1/q\le s<1.
\end{cases}
\]
Here \(J_m(a,b)=\log[H_m(b)/H_m(a)]-2[H_m(b)-H_m(a)]/m\) is elementary. Consequently, for every \(0<s<1\) and \(0<r_1<r_2\),
\[
\frac{y_{q(r_2)}(s)}{\chi(r_2)}
<\frac{y_{q(r_1)}(s)}{\chi(r_1)}.
\]
Equivalently, the stationary radial laws are strictly ordered from large to small with increasing resetting, and every strictly increasing integrable radial observable has strictly decreasing stationary expectation. In addition, **every fixed radial survival quantile has the same downward derivative jump at the condensation threshold**. Writing \(x_q(s)=My_q(s)/(2q)\),
\[
\left.\frac{\partial x_q(s)}{\partial q}\right|_{q=1+}
-\left.\frac{\partial x_q(s)}{\partial q}\right|_{q=1-}
=\frac{M}{2m}\bigl[H_m(1)+1-m\bigr]<0,
\quad 0<s<1.
\]
The jump is independent of which quantile is observed.

For \(m>4\), when \(1<q\le m/4\) both the droplet and supersaturated gas-only profiles exist. Let their physical radial upper-survival quantiles be \(x_{\mathrm{drop}}(s)\) and \(x_{\mathrm{gas}}(s)\). Then
\[
x_{\mathrm{drop}}(s)<x_{\mathrm{gas}}(s)
\quad(0<s<1).
\]
This is an ordering of two **stationary mean-field profiles** at the same model parameters, not an assertion about transition probabilities between phases.

Let \(E_\lambda\) denote an exponential random variable of rate \(\lambda\). As \(q\downarrow0\),
\[
d_{\mathrm{TV}}\bigl(\mathcal L(Y_q),\mathcal L(E_1)\bigr)
=\frac{q}{4m}+O(q^2).
\]
For every \(q>1\) there is the following **exact identity**, with no asymptotic remainder:
\[
d_{\mathrm{TV}}\bigl(\mathcal L(Y_q),\mathcal L(E_m)\bigr)
=\frac{\Delta_m}{q},\qquad
\Delta_m=\frac12\int_0^\infty
\bigl|g_m(z)-m e^{-mz}\bigr|\,dz\in(0,1),
\]
where \(g_m(0)=H_m(1)\) and \(g_m\) is the unique decreasing gas solution of \((1-2g_m/m)g_m'=-g_m\). In particular, for each fixed \(0<p<1\), the physical \(p\)-quantile of \(|X_r|\) satisfies, exactly once \(q\ge1/(1-p)\),
\[
x_p(r)=\frac{\log[1/(1-p)]}{m\chi(r)},
\quad\text{and}\quad
\lim_{r\to\infty}r x_p(r)=\frac{v_0}{m}\log\frac1{1-p}.
\]

## Assumptions and scope

Fix \(M>0\), \(v_0>0\), \(\alpha>0\), \(r>0\), and \(m=\rho_m\ge4\). The speed is \(v_0(1-\rho/m)\) in the dilute phase and \(v_0/m\) in the dense phase. The population has independent local, instantaneous resets to the origin at rate \(r\) and uniform orientation randomization at tumble times of intensity \(\alpha\). We study the explicit symmetric stationary **continuum mean-field density** obtained from these constitutive and kinetic equations. The branch is gas-only for \(q\le1\), and the central droplet plus exterior gas for \(q>1\). The supersaturated gas-only branch is considered separately only where it exists, \(q\le m/4\).

The normalized law \(X_r\) is a sample drawn from the *deterministic stationary mass profile*; no stochastic ordering of microscopic interacting particle configurations, no uniqueness among arbitrary weak stationary states, and no dynamical stability assertion is implied. At the marginal case \(m=4\) the explicit interface remains well defined; no claim of robust interface stability is made. All distances are measured relative to the reset origin.

## Proof

**1. Reduction to cumulative mass.** In the gas phase, use dimensionless position \(y=\chi|x|\) and denote the stationary density by \(g(y)\). The stationary gas equation is
\[
(1-2g/m)\,g'(y)=-g(y).
\]
Its increasing current variable \(U(y)=R_m(g(y))\), where \(R_m(h)=h-h^2/m\), satisfies \(U'=-g\). The low-density inverse of \(R_m\) is precisely \(H_m\). If the total dimensionless half-line mass is \(q=M\chi/2\), the gas-only profile has \(U(0)=q\), and
\[
\Pr(Y_q>y)=\frac{U(y)}q,\qquad
\frac{dy}{dU}=-\frac1{H_m(U)}.
\]
Setting the survival probability equal to \(s\) proves \(y_q(s)=J_m(qs,q)\) whenever the single-gas profile is selected. It also proves that the entire supersaturated gas profile has the same formula for \(1<q\le m/4\).

**2. Droplet cumulative mass.** For \(q>1\) the source stationary solution has half-width \(b=\log q/(m\chi)\). In the core \(0\le y\le L=\log q/m\), its normalized one-sided density is \(m e^{-my}\), while outside the core it is \(q^{-1}g_m(y-L)\). Indeed, the physical core density is \(mq e^{-my}\), the one-sided normalized mass factor is \(1/q\), and the translated gas profile \(g_m\) has mass one because
\[
\int_0^\infty g_m(z)\,dz
=R_m(g_m(0))-R_m(0)=R_m(H_m(1))=1.
\]
The normalized survival is therefore
\[
\Pr(Y_q>y)=
\begin{cases}
e^{-my},&0\le y\le L,\\
q^{-1}R_m(g_m(y-L)),&y>L.
\end{cases}
\]
For \(s\ge1/q\) the survival quantile lies in the core and equals \(\log(1/s)/m\). For \(s<1/q\), the exterior mass variable at that quantile equals \(qs\); its distance beyond the interface is \(J_m(qs,1)\). This yields the complete displayed quantile formula. At \(q=1\) the gas and droplet formulas coincide.

**3. Strict order across resetting rates.** In the gas regime, differentiating the positive integral representation
\[
y_q(s)=\int_s^1\frac{1-H_m(qt)/m}{t}\,dt
\]
gives
\[
\frac{\partial y_q(s)}{\partial q}
=-\frac{H_m(q)-H_m(qs)}{mq}<0
\qquad(0<q<1).
\]
In the exterior quantile regime \(q>1\), \(qs<1\), the derivative is
\[
\frac{\partial y_q(s)}{\partial q}
=\frac{H_m(qs)+1-m}{mq}<0,
\]
since \(H_m(qs)\le m/2\) and \(m\ge4\). In the remaining core regime \(q\ge1/s\), the dimensionless quantile is constant. Continuity at both regime boundaries follows from the formulas. Thus \(q\mapsto y_q(s)\) is nonincreasing and strictly positive; \(q\mapsto y_q(s)/q\) is strictly decreasing. Since \(\chi=2q/M\) strictly increases with \(r\), the physical radius quantiles are strictly decreasing. The comparison holds simultaneously for every survival level, proving first-order stochastic order. Integrating tail probabilities yields the expectation consequence (for a strictly increasing observable with finite expectation). Taking fixed-level one-sided derivatives at \(q=1\) gives \(\partial_q y_{1-}(s)=[H_m(s)-H_m(1)]/m\) and \(\partial_q y_{1+}(s)=[H_m(s)+1-m]/m\); their difference is \([H_m(1)+1-m]/m\), independent of \(s\). Since \(y_q(s)\) is continuous at \(q=1\), the derivative of the scaling factor \(M/(2q)\) cancels in the jump. The displayed physical-quantile kink follows, including at \(m=4\) where the derivatives are finite one-sided values despite a singular gas-density slope at the interface.

**4. Branch ordering at coexistence.** For \(m>4\) and \(1<q\le m/4\), the gas-only scaled quantile remains \(J_m(qs,q)\). If \(s<1/q\), subtracting the droplet quantile gives
\[
y_{\mathrm{gas}}(s)-y_{\mathrm{drop}}(s)
=\int_1^q\left[\frac1{H_m(u)}-\frac1{mu}\right]du>0.
\]
If \(s\ge1/q\), the difference is
\[
\int_{qs}^{q}\left[\frac1{H_m(u)}-\frac1{mu}\right]du>0.
\]
Both integrands are positive on the displayed integration ranges: \(u\ge1\), whereas \(H_m(u)\le m/2<mu\). Dividing by the common \(\chi\) completes the stationary-branch comparison.

**5. Exact strong-reset total variation.** On the growing interval \([0,L]\), the density of \(Y_q\) equals the \(E_m\) density exactly. For \(y=L+z\), the two densities are respectively \(q^{-1}g_m(z)\) and \(q^{-1}m e^{-mz}\). Thus their half-\(L^1\) distance is exactly \(\Delta_m/q\). Both tail distributions have mass one before multiplication by \(q^{-1}\), and they are not equal since \(g_m(0)=H_m(1)\le m/2<m\); hence \(0<\Delta_m<1\). For fixed survival fraction \(s=1-p\), eventually \(s\ge1/q\), and the exact core-quantile formula supplies the stated physical asymptotics.

**6. Sharp weak-reset correction.** The gas-only profile satisfies
\[
\log g_q(y)-\frac{2g_q(y)}m
=\log H_m(q)-\frac{2H_m(q)}m-y.
\]
For small \(q\), the analytic low-density inverse gives the uniform integrable expansion
\[
\frac{g_q(y)}q=e^{-y}+\frac q m\left(2e^{-2y}-e^{-y}\right)+O(q^2 e^{-y}),
\qquad y\ge0.
\]
The error estimate follows from the convergent Taylor series of the principal real inverse of \(h\mapsto h e^{-2h/m}\) for a uniformly small argument proportional to \(q e^{-y}\). Since
\[
\int_0^\infty\left|2e^{-2y}-e^{-y}\right|dy
=\int_0^1|2t-1|dt=\frac12,
\]
the half-\(L^1\) distance is \(q/(4m)+O(q^2)\), proving the claimed sharp weak-reset constant.

## Verification

`verify_quantile.py` is a standalone Python 3 script (standard library only). It independently inverts the implicit gas profile by numerical bisection, compares it with exact mass-quantile formulas, tests strict and nonstrict orders across phase boundaries, compares the two coexisting profiles, verifies the translated gas-tail identity, and checks the first-order weak-reset total-variation coefficient. Executing `python3 verify_quantile.py` passed 3,123 deterministic assertions for \(m\in\{4,5,10,20\}\). The script numerically estimated \(\Delta_4\approx0.3784\), \(\Delta_5\approx0.4721\), \(\Delta_{10}\approx0.6761\), and \(\Delta_{20}\approx0.8046\). These finite checks are corroboration, **not** proofs of all-parameter or infinite-domain assertions; the analytical steps above supply those proofs.

## Relationship to prior work

Pascal Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting* (arXiv:2610.26149, first publicly submitted October 19, 2026), derives the kinetic equations, exact gas and droplet density profiles, critical reset rate, metastable gas coexistence, dense mass, and nonmonotone droplet half-width. In particular its Sections 3–4 and equations (22), (25), (31)–(44) are the established inputs used here. **Those profile and width formulas are not claimed as new.** The new assertion is the strict probability-law ordering of *the full stationary radius* across the transition and between coexisting stationary branches, together with the two sharp exponential total-variation laws. An increasing droplet half-width alone does not determine the sign of these distributional comparisons. The result is a direct, specialized mathematical consequence of the established exact profiles, not an independent derivation of a new physical model.

Established resetting literature, including Evans–Majumdar–Schehr's 2020 review, studies localization in many noninteracting and interacting systems. A run-and-tumble process with a sticky boundary, studied by Bressloff and Linn (2026), has a different boundary and resetting mechanism and does not supply the specific two-phase stationary profiles or the quantitative comparison made here.

## Limitations

The strict order holds only for the specified symmetric stationary continuum mean-field profile selected by phase and for instantaneous resetting. It does not assert a coupling of microscopic particle trajectories, microscopic finite-population stochastic order, or rigorous dynamic convergence to a selected mean-field branch. The gas-only coexistence comparison assumes that both explicit stationary branches exist and is not itself a metastability proof. The scaled limiting exponentials are distributions of normalized mass sampled from the profiles, not laws of reset times or fluctuations of the microscopic particle current. Publication-priority coverage beyond the inspected primary literature can remain implicit in a general theorem and has not been independently certified.

## References

1. P. Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, arXiv:2610.26149, version 1 (October 19, 2026), version 2 (October 20, 2026), https://arxiv.org/html/2610.26149v2 .
2. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic resetting and applications*, Journal of Physics A: Mathematical and Theoretical (2020).
3. P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, Physical Review E 113, 054122 (2026), https://doi.org/10.1103/dcnh-bhwc .
