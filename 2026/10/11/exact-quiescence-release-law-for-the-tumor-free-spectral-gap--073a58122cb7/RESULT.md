# Exact quiescence-release law for the tumor-free spectral gap
## Finding
Consider the continuous-treatment formulation of the malignant-glioma model in arXiv:2609.39191v1 at its tumor-free equilibrium \(P\). Define
\[
g=\beta_2+\gamma_1,
\qquad
m_1=\alpha_4+(\alpha_1+\varepsilon_1)E^*-r_1,
\qquad
m_2=\alpha_5+\alpha_2C^*-r_2,
\]
and
\[
m_*=\min\{m_1,m_2\},
\qquad
\kappa=\min\{\tau,\mu,\rho_1+\alpha_6+\alpha_3E^*\}.
\]
The source's strict tumor-free stability conditions are exactly \(m_1>0\) and \(m_2>0\). Throughout this stable region, the positive local spectral gap
\[
G=-\max_{\lambda\in\sigma(D F(P))}\operatorname{Re}\lambda
\]
is
\[
G(g)=\min\{\kappa,\rho(g,m_*)\},
\qquad
\rho(g,m)=\frac{g+\beta_1+m-\sqrt{(g+\beta_1+m)^2-4gm}}{2}.
\]
For each fixed \(m>0\), the map \(g\mapsto\rho(g,m)\) is strictly increasing and strictly concave, satisfies
\[
\lim_{g\downarrow0}\rho(g,m)=0,
\qquad
\lim_{g\to\infty}\rho(g,m)=m,
\]
and has the asymptotic expansions
\[
\rho(g,m)=\frac{m}{\beta_1+m}g+O(g^2)\quad(g\downarrow0),
\]
\[
\rho(g,m)=m-\frac{\beta_1m}{g}+O(g^{-2})\quad(g\to\infty).
\]
Consequently the continuous radiotherapy-induced recruitment parameter \(\gamma_1\), which enters through \(g=\beta_2+\gamma_1\), does not alter the stability threshold but does strictly accelerate the slow tumor-decay mode once the tumor-free equilibrium is stable. The gain has diminishing returns. If \(0<\kappa<m_*\), the full spectral gap reaches the non-tumor bottleneck exactly when
\[
g=g_{\mathrm{cap}}=\frac{\kappa(\beta_1+m_*-\kappa)}{m_*-\kappa},
\]
and remains equal to \(\kappa\) for larger \(g\). If \(\kappa\ge m_*\), the gap instead approaches \(m_*\) and never reaches \(\kappa\) at finite \(g\).

## Assumptions and scope
All parameters are in the biologically relevant positive regime used for Proposition 7 of arXiv:2609.39191v1, with \(\beta_1>0\), \(g=\beta_2+\gamma_1>0\), and the strict stability margins \(m_1,m_2>0\). The equilibrium values are those of the source,
\[
E^*=\frac{\bar E_0}{\mu},
\qquad
C^*=\frac{\bar C_0}{\rho_1+\alpha_6+\alpha_3E^*}.
\]
The claim concerns only the local linear spectral gap at the tumor-free equilibrium of the continuous-treatment autonomous system. It is not a statement about the impulsive treatment protocol, global nonlinear eradication, clinical efficacy, or optimal dosing.

## Proof
The source factorizes the characteristic polynomial at \(P\) into three scalar factors and three quadratic factors. The scalar eigenvalues are
\[
-\tau,\qquad -\mu,\qquad -(\rho_1+\alpha_6+\alpha_3E^*),
\]
so their positive decay-rate bottleneck is \(\kappa\).

Using the source definitions of its auxiliary coefficients \(a\) and \(b\), the three quadratic factors can be rewritten as
\[
\lambda^2+(g+\beta_1+m)\lambda+gm=0
\]
with
\[
m\in\{m_1+\alpha_2C^*,\;m_2,\;m_1\}.
\]
Because \(m_1,m_2>0\), all three such \(m\) are positive. Their discriminant is
\[
\Delta=(g+\beta_1+m)^2-4gm=(g+\beta_1-m)^2+4\beta_1m>0,
\]
so each block has two real negative eigenvalues. The slower positive decay rate of a block is
\[
\rho(g,m)=\frac{g+\beta_1+m-\sqrt\Delta}{2}.
\]
For fixed \(g>0\),
\[
\frac{\partial\rho}{\partial m}
=\frac12\left(1-\frac{\beta_1+m-g}{\sqrt\Delta}\right)>0,
\]
because
\[
\Delta-(\beta_1+m-g)^2=4\beta_1g>0.
\]
Hence the slowest tumor block is the one with \(m=m_*\), since \(m_1+\alpha_2C^*\ge m_1\). This proves
\[
G(g)=\min\{\kappa,\rho(g,m_*)\}.
\]

For the recruitment dependence,
\[
\frac{\partial\rho}{\partial g}
=\frac12\left(1-\frac{g+\beta_1-m}{\sqrt\Delta}\right)>0,
\]
since
\[
\Delta-(g+\beta_1-m)^2=4\beta_1m>0.
\]
A second differentiation gives
\[
\frac{\partial^2\rho}{\partial g^2}
=-\frac{2\beta_1m}{\Delta^{3/2}}<0.
\]
The two limits and asymptotic expansions follow by direct expansion of the quadratic root. Finally, solving \(\rho(g,m_*)=\kappa\) for \(g\) gives
\[
g=\frac{\kappa(\beta_1+m_*-\kappa)}{m_*-\kappa},
\]
which is positive and finite exactly when \(0<\kappa<m_*\).

## Verification
The characteristic factors, equilibrium values, and strict stability inequalities were independently reconstructed from Proposition 7 and equations (55)--(69) of arXiv:2609.39191v1. The algebra was checked by expanding each rewritten quadratic and by differentiating the closed-form root. In particular,
\[
\Delta-(g+\beta_1-m)^2=4\beta_1m,
\qquad
\Delta-(\beta_1+m-g)^2=4\beta_1g,
\]
which certify the strict derivative signs in the stated positive domain. No finite numerical experiment is used as proof.

## Relationship to prior work
The motivating paper proves an if-and-only-if local stability threshold for the continuously treated tumor-free equilibrium. Its threshold does not contain \(\beta_2+\gamma_1\), although that combination remains present in all three tumor-sector characteristic quadratics. The present result extracts the exact spectral-gap dependence hidden in those factors and shows that quiescence release controls convergence speed rather than the threshold itself.

The 2025 chemoradiotherapy predecessor arXiv:2504.17481 models proliferative/quiescent switching and treatment-induced recruitment, but its radiotherapy recruitment is impulsive rather than the continuous \(\gamma_1\) mechanism analyzed here. The 2025 CAR-T plus chemotherapy model arXiv:2501.13774 analyzes tumor eradication under constant treatment but does not use the same proliferative/quiescent pair. A 2014 renewal-equation study by Alarcón, Getto, and Nakata addresses stability in a different age-structured quiescence model. None of the inspected material supplied the exact local spectral-gap law above.

## Limitations
This result is local and linear. It does not imply a global basin size, a nonlinear convergence estimate far from the equilibrium, or superiority of increasing radiotherapy-induced recruitment in a clinical treatment protocol. The parameter \(\gamma_1\) is interpreted only within the continuous-treatment idealization of the source. An equivalent spectral-root observation may exist in older literature under a different biological normalization; no such implication-equivalent statement was found in the checked sources.

## References
1. D. Sinelshchikov, N. A. Mora Millán, M. Perales-Patón, J. Belmonte-Beitia, and M. Italia, “Combining standard chemoradiotherapy with CAR-T cell therapy in malignant gliomas: Insights from an impulsive mathematical framework and virtual trials,” arXiv:2609.39191v1, 2026.
2. M. Perales-Patón et al., “Optimizing chemoradiotherapy for malignant gliomas: a validated mathematical approach,” arXiv:2504.17481v1, 2025.
3. D. Sinelshchikov, J. Belmonte-Beitia, and M. Italia, “A mathematical model of CAR-T cell therapy in combination with chemotherapy for malignant gliomas,” arXiv:2501.13774v2, 2025.
4. T. Alarcón, P. Getto, and Y. Nakata, “Stability Analysis of a Renewal Equation for Cell Population Dynamics with Quiescence,” SIAM Journal on Applied Mathematics 74 (2014), DOI:10.1137/130940438.
