# Sharp total-variation boundary cusp for the Newton kernel spherical law

## Finding

For each fixed integer dimension \(d\ge3\), the Newton kernel-based spherical laws introduced in [1] approach their integrable boundary-cusp law at an exact, dimension-dependent first-order total-variation rate, with a **negative fractional-power correction** that is universal in exponent:

\[
\boxed{\quad
 d_{\mathrm{TV}}(\nu_{1-\varepsilon},\nu_1)
 =\frac{d-2}{2}\,\varepsilon
 -(d-2)c_d\varepsilon^{3/2}
 +O_d(\varepsilon^2),\qquad
 c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}.
 \quad}
\]

The exact maximizing measurable event for total variation is the complement of the spherical cap \(\{x:\mu\cdot x>(1+\rho)/2\}\) for every \(0\le\rho<1\). The limiting signed first variation is singular:

\[
\frac{\nu_{1-\varepsilon}-\nu_1}{\varepsilon}
\ \Longrightarrow\ \frac{d-2}{2}(\nu_1-\delta_\mu)
\]

weakly against continuous functions on the sphere; this convergence **does not** hold in total variation. In dimension \(d=3\), an all-parameter closed form strengthens the asymptotic result:

\[
 d_{\mathrm{TV}}(\nu_{\rho},\nu_1)
 =\frac{(1-\rho)-(1-\rho)^{3/2}}{2\rho}
 \quad(0<\rho<1),
\]

with continuous value \(1/4\) at \(\rho=0\).

## Assumptions and scope

Fix an integer \(d\ge3\) and a direction \(\mu\) on the unit sphere \(S^{d-1}\subset\mathbb R^d\). Let \(\sigma_d\) be *probability-normalized* surface measure. For \(0\le\rho<1\), define \(\nu_\rho\) by its density

\[
 f_\rho(x)=\|x-\rho\mu\|^{-(d-2)}\quad\text{with respect to }\sigma_d.
\]

Define \(\nu_1\) by the same density at \(\rho=1\), assigning any value at the single point \(\mu\); the cusp is integrable and normalization equals one. Define \(d_{\mathrm{TV}}(P,Q)=\sup_A|P(A)-Q(A)|=\tfrac12\int|dP-dQ|\). All asymptotic constants are for fixed \(d\); uniformity as \(d\) grows is not claimed. The Dirac point mass at \(\mu\) is denoted \(\delta_\mu\). Weak signed convergence refers to testing against continuous functions.

## Proof

**Normalization and the one-dimensional reduction.** For \(\|a\|<1\), the Newton kernel \(\|x-a\|^{2-d}\), considered as a function of \(a\), is harmonic for every fixed \(\|x\|=1\). Its spherical average \(H(a)\) is radial and harmonic on the unit ball. Since it is bounded near \(a=0\), radial harmonicity forces it to be constant. Thus \(H(a)=H(0)=1\), proving the interior normalization independently of the sampler in [1].

Write \(t=\mu\cdot x\), \(u=1-t\), and set \(a_d=(d-2)/2\), \(b_d=(d-3)/2\). Under uniform surface measure, the latitude density of \(t\) is \(c_d(1-t^2)^{b_d}\). Since \(f_1=(2u)^{-a_d}\), the distribution of \(u\) under \(\nu_1\) has density

\[
 h_d(u)=\frac{c_d}{\sqrt2}\,u^{-1/2}(1-u/2)^{b_d},
 \qquad 0<u<2.
\]

In particular, \(u/2\) is \(\operatorname{Beta}(1/2,(d-1)/2)\) under \(\nu_1\), proving its mass is one and its cusp integrable. The likelihood ratio relative to \(\nu_1\), with \(\varepsilon=1-\rho\), is

\[
R_\varepsilon(u)=\frac{f_{1-\varepsilon}}{f_1}
=\left(1-\varepsilon+\frac{\varepsilon^2}{2u}\right)^{-a_d}.
\]

**Exact total-variation event.** Direct comparison of the squared distances gives \(f_\rho(x)>f_1(x)\) precisely when \(t<(1+\rho)/2\), equivalently \(u>\varepsilon/2\); the opposite strict inequality holds on the corresponding cap. As both laws have mass one, total variation equals the positive mass discrepancy:

\[
 d_{\mathrm{TV}}(\nu_{1-\varepsilon},\nu_1)
 =\int_{\varepsilon/2}^{2}
 \bigl(R_\varepsilon(u)-1\bigr)h_d(u)\,du.
\tag{1}
\]

This identifies a maximizing measurable event for every parameter, without a limiting argument.

**Uniform outer expansion.** On \(u\ge\varepsilon/2\), let \(z=\varepsilon-\varepsilon^2/(2u)\). Then \(0\le z\le\varepsilon\) and, uniformly in this region as \(\varepsilon\downarrow0\),

\[
 R_\varepsilon(u)-1
 =a_d\varepsilon-\frac{a_d\varepsilon^2}{2u}
 +O_d(\varepsilon^2),
\]

since \((1-z)^{-a_d}=1+a_dz+O_d(z^2)\). The cusp's beta density yields the two sharp endpoint integrals

\[
 \int_0^{\varepsilon/2}h_d(u)\,du
 =c_d\sqrt\varepsilon+O_d(\varepsilon^{3/2}),
 \qquad
 \int_{\varepsilon/2}^{2}\frac{h_d(u)}{u}\,du
 =\frac{2c_d}{\sqrt\varepsilon}+O_d(1).
\]

Substituting in (1) gives

\[
 d_{\mathrm{TV}}=a_d\varepsilon(1-c_d\sqrt\varepsilon)
 -a_dc_d\varepsilon^{3/2}+O_d(\varepsilon^2)
 =a_d\varepsilon-2a_dc_d\varepsilon^{3/2}+O_d(\varepsilon^2),
\]

proving both the sharp leading constant and the nonanalytic correction. All bounds are uniform over the integration region for fixed \(d\); no Taylor expansion is used in the singular inner cap.

**Signed derivative.** Let \(Q_\varepsilon^+\) and \(Q_\varepsilon^-\) denote the positive and negative parts of \(\nu_{1-\varepsilon}-\nu_1\). On the positive region, \((R_\varepsilon-1)/\varepsilon\to a_d\) pointwise, and the mean-value theorem bounds it by a constant depending only on \(d\) for \(\varepsilon\le1/2\). Dominated convergence against \(\nu_1\), including the moving indicator \(u>\varepsilon/2\), proves \(Q_\varepsilon^+/\varepsilon\to a_d\nu_1\) **in total variation**. The negative part has the same mass, so \(Q_\varepsilon^-(S^{d-1})/\varepsilon\to a_d\), but its support lies in \(u<\varepsilon/2\), a shrinking cap about \(\mu\). Therefore \(Q_\varepsilon^-/\varepsilon\Rightarrow a_d\delta_\mu\), giving the stated weak signed limit. Each quotient is absolutely continuous with respect to surface measure while the weak derivative has a nonzero atom, precluding total-variation differentiability at \(\rho=1\).

**Exact three-dimensional formula.** When \(d=3\), the latitude measure is \(dt/2\), the two densities are reciprocal square roots, and both antiderivatives are elementary. Evaluating them on \(-1\le t\le(1+\rho)/2\) gives

\[
\frac12\left[
\frac{1+\rho-\sqrt{1-\rho}}{\rho}
 -\bigl(2-\sqrt{1-\rho}\bigr)
\right]
=\frac{(1-\rho)-(1-\rho)^{3/2}}{2\rho}.
\]

At \(\rho=0\), the expression has removable limit \(1/4\).

## Verification

A standalone Python-standard-library verifier is provided at `verification/check_newton_boundary.py` and can be run with `python3 verification/check_newton_boundary.py` after extracting this package. It tests the interior and cusp probability normalizations by independent latitude quadrature, equality of positive and negative total-variation masses, an exact rational antiderivative for \(d=3\) at rational square-gap parameters, and bounded \(\varepsilon^2\)-scale remainders for several dimensions. The recorded run passed **333 exact-rational or numerical-quadrature assertions**. Numerical tests neither prove uniform asymptotics nor establish the weak derivative; the preceding analytic steps supply those statements.

## Relationship to prior work

Sablica and Hornik [1], Corollary 1 and Section 4, introduce this Newton kernel-based family, prove unit normalization, and note pointwise convergence to the integrable cusp. Their subsequent sections concern simulation efficiency; the all-parameter maximizing event, sharp total-variation expansion, fractional correction, and singular signed first variation are not stated there. The classical Newton shell theorem supplies normalization but does not by itself evaluate the sign-change cap or its asymmetric boundary correction.

Baringhaus and Grübel [2] develop discrete mixture representations for other spherical families, including von Mises–Fisher, Watson, spherical Cauchy and angular Gaussian distributions. The inspected family definitions and results do not directly cover this Newton-kernel total-variation boundary law. Earlier or unindexed potential-theory formulas may imply one or more parts of the result; originality is assessed against accessible literature, not certified by absence of search hits.

## Limitations

This concerns one fixed interior direction and one radial approach to a boundary cusp, not general spatial perturbations, nonradial parameter changes, or a growing dimension. The \(O_d(\varepsilon^2)\) bound is qualitative in \(d\); no finite-sample estimation or Monte Carlo coupling guarantee beyond the exact probability-metric statement is claimed. Historical-priority risk in the classical potential-theory literature remains. The work has not undergone independent mathematical audit.

## References

[1] L. Sablica and K. Hornik, *Direct Simulation of Poisson and Newton Kernel Distributions*, arXiv:2610.32506v1 (first posted October 23, 2026), especially Section 4 and Corollary 1. https://arxiv.org/pdf/2610.32506

[2] L. Baringhaus and R. Grübel, *Discrete mixture representations of spherical distributions*, arXiv:2301.03870v3 (2023), Introduction and Sections 2–4. https://arxiv.org/pdf/2301.03870
