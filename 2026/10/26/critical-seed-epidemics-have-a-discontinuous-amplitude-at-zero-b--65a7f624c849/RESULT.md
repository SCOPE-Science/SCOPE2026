# Critical seed epidemics have a discontinuous amplitude at zero behavioral turnover

## Finding

For the closed, population-normalized Allen–Heller–Pons two-behavior SIR model (MB) at its exact invasion threshold, arbitrarily slow but positive bidirectional behavior changes determine a **different leading final-size coefficient** from zero behavioral change. Fix \(0<\rho<1/2\), \(0<\beta_2<\beta_1\leq1\), and \(\kappa=\rho\beta_1+(1-\rho)\beta_2\). Set \(\alpha_1=a(1-\rho)\), \(\alpha_2=a\rho\), and let \(Z(a,\varepsilon)\) be the total final recovered fraction when a fraction \(\varepsilon\) is initially infectious and the remainder lies in behavioral shares \(\rho,1-\rho\). For every fixed \(a>0\),
\[
\lim_{\varepsilon\downarrow0}\frac{Z(a,\varepsilon)}{\sqrt{\varepsilon}}=\sqrt{2}.
\]
At \(a=0\), the zero-turnover boundary of the same ODE family, the coefficient instead equals
\[
\lim_{\varepsilon\downarrow0}\frac{Z(0,\varepsilon)}{\sqrt{\varepsilon}}=\sqrt{\frac{2}{M_2}},\quad
M_2=\frac{\rho\beta_1^2+(1-\rho)\beta_2^2}{\kappa^2}
=1+\frac{\rho(1-\rho)(\beta_1-\beta_2)^2}{\kappa^2}>1.
\]
For each fixed \(\varepsilon>0\), however, \(Z(a,\varepsilon)\to Z(0,\varepsilon)\) as \(a\downarrow0\). Thus the initial-seed and turnover limits **do not commute**: taking \(\varepsilon\downarrow0\) first gives \(\sqrt2\), while taking \(a\downarrow0\) first gives \(\sqrt{2/M_2}\). This statement concerns the deterministic near-critical final removed fraction, not the stochastic probability of a major outbreak.

## Assumptions and scope

Use normalized conserved population \(N=1\) and parameters \(0<\rho<1/2\), \(0<\beta_2<\beta_1\leq1\), \(\kappa=\rho\beta_1+(1-\rho)\beta_2\), \(0<\lambda<1\), \(\gamma>0\), and turnover \(a\geq0\). Write \(I=A_1+A_2+I_s\). The precise MB dynamics are
\[
\begin{aligned}
\dot S_1&=\alpha_2S_2-\alpha_1S_1-\beta_1S_1I,\\
\dot S_2&=\alpha_1S_1-\alpha_2S_2-\beta_2S_2I,\\
\dot A_1&=(1-\lambda)\beta_1S_1I+\alpha_2A_2-(\alpha_1+\gamma+\kappa)A_1,\\
\dot A_2&=(1-\lambda)\beta_2S_2I+\alpha_1A_1-(\alpha_2+\gamma+\kappa)A_2,\\
\dot I_s&=\lambda(\beta_1S_1+\beta_2S_2)I+\gamma(A_1+A_2)-\kappa I_s,\\
\dot R&=\kappa I,
\end{aligned}
\]
with \(\alpha_1=a(1-\rho)\), \(\alpha_2=a\rho\), \((S_1,S_2,A_1,A_2,I_s,R)(0)=(\rho(1-\varepsilon),(1-\rho)(1-\varepsilon),0,0,\varepsilon,0)\), and \(0<\varepsilon<1\). For positive \(a\), these turnover rates obey the source's strict \(\alpha_1>\alpha_2>0\) condition. The boundary \(a=0\) is considered only as the continuous zero-turnover extension; the source formally assumes positive switching in MB. The common reproduction quantity at the infection-free reference state equals \(\mathcal R_0=\kappa/\kappa=1\), independent of \(a>0\).

## Proof

**1. Exact reduction and monotonicity.** Positivity of the compartmental equations and conservation of their sum ensure a unique global nonnegative bounded solution. Set \(S=S_1+S_2\), \(d=S_1-\rho S\), and \(\delta=\beta_1-\beta_2>0\). Adding the infected equations cancels symptom progression and behavior transfers exactly. The reduced subsystem is
\[
\begin{aligned}
\dot S&=-(\kappa S+\delta d)I,\\
\dot I&=(\kappa S+\delta d-\kappa)I,\\
\dot R&=\kappa I,\\
\dot d&=-[a+B I]d-\rho(1-\rho)\delta S I,\\
B&=(1-\rho)\beta_1+\rho\beta_2>0.
\end{aligned}
\]
The initial data satisfy \(S(0)=1-\varepsilon\), \(d(0)=0\), and \(I(0)=\varepsilon\). Variation of constants yields \(d(t)\leq0\). As \(S(t)\leq1-\varepsilon\), it follows for all \(t\geq0\) that \(0<I(t)\leq\varepsilon e^{-\kappa\varepsilon t}\). Therefore \(I(t)\to0\), \(R\) increases to a finite \(Z(a,\varepsilon)>0\), and \(S+I+R=1\).

**2. Positive-turnover amplitude and bound.** For fixed \(a>0\), variation of constants and \(0\leq SI\leq\varepsilon\) give the uniform bound
\[
-\frac{\rho(1-\rho)\delta\varepsilon}{a}\leq d(t)\leq0.
\]
Use \(z=R(t)\) as the strictly increasing trajectory coordinate. Dividing the \(I\) equation by \(\dot R=\kappa I\), and using \(S=1-z-I\), gives
\[
\frac{dI}{dz}=-(z+I)+\frac{\delta}{\kappa}d.
\]
Integrating from \(z=0\), where \(I=\varepsilon\), to \(z=Z\), where \(I=0\), yields the **exact balance**
\[
\varepsilon=\frac{Z^2}{2}+\int_0^Z I(z)\,dz-\frac{\delta}{\kappa}\int_0^Z d(z)\,dz.
\]
Both correction integrals on the right are nonnegative. Since \(I\leq\varepsilon\), they imply
\[
0\leq1-\frac{Z(a,\varepsilon)^2}{2\varepsilon}
\leq\left(1+\frac{\rho(1-\rho)\delta^2}{\kappa a}\right)\sqrt{2\varepsilon}.
\]
Here \(Z\leq\sqrt{2\varepsilon}\) was used in the last inequality. For any fixed \(a>0\), the right side tends to zero, proving \(Z(a,\varepsilon)/\sqrt\varepsilon\to\sqrt2\). The estimate explicitly displays the nonuniform dependence on \(a\).

**3. Zero-turnover amplitude.** When \(a=0\), each susceptible class obeys \(\dot S_j=-\beta_j S_j I\), and \(\dot R=\kappa I\); hence
\[
S_1(t)=\rho(1-\varepsilon)e^{-\beta_1R(t)/\kappa},\qquad
S_2(t)=(1-\rho)(1-\varepsilon)e^{-\beta_2R(t)/\kappa}.
\]
With \(I(\infty)=0\), the final size is the unique positive root of
\[
Z+(1-\varepsilon)G(Z)=1,\qquad
G(z)=\rho e^{-(\beta_1/\kappa)z}+(1-\rho)e^{-(\beta_2/\kappa)z}.
\]
Indeed the left side minus one is \(-\varepsilon\) at zero, is positive at one, and has derivative at least \(\varepsilon>0\) on \([0,1]\). The function \(F_0(z)=z+G(z)-1\) is strictly positive for every \(z>0\) because \(e^{-u}>1-u\) for \(u>0\) and \(\rho\beta_1+(1-\rho)\beta_2=\kappa\). Thus its root satisfies \(Z\to0\) as \(\varepsilon\downarrow0\). The final-size equation rewrites as \(F_0(Z)=\varepsilon G(Z)\); Taylor expansion at zero gives \(F_0(z)=M_2z^2/2+O(z^3)\) and \(G(Z)\to1\). Consequently \(Z(0,\varepsilon)^2/\varepsilon\to2/M_2\). Since \(\beta_1\ne\beta_2\), \(M_2>1\).

**4. Continuity at each nonzero seed.** For each fixed \(\varepsilon>0\), solutions on every finite time interval depend continuously on \(a\) by standard smooth ODE dependence. Their remaining recovered fraction after time \(T\) is bounded **uniformly** in \(a\geq0\):
\[
0\leq Z(a,\varepsilon)-R_a(T)
=\kappa\int_T^\infty I_a(t)\,dt\leq e^{-\kappa\varepsilon T}.
\]
First choose large \(T\), then let \(a\downarrow0\). It follows \(Z(a,\varepsilon)\to Z(0,\varepsilon)\). Combining this fact with Parts 2–3 proves the two distinct iterated limits, without exchanging nonuniform limits.

## Verification

All four proof identities follow directly from the stated MB equations; no finite enumeration or numerical integration is used as an infinite-time proof. A concrete admissible example is \(\rho=1/4\), \(\beta_1=1\), \(\beta_2=1/4\), \(\kappa=7/16\), \(\lambda=3/5\), \(\gamma=1/5\). Then \(M_2=76/49\), so the exact zero-turnover coefficient is \(7/\sqrt{38}\), strictly below the positive-turnover coefficient \(\sqrt2\). Direct high-accuracy ODE integrations give the indicative ratios \(Z(0,10^{-4})/\sqrt{10^{-4}}\approx1.1334484\) and \(Z(0.05,10^{-4})/\sqrt{10^{-4}}\approx1.3784199\); these are checks, not part of the proof. The predicted limits are approximately \(1.1355499\) and \(1.4142136\), respectively.

## Relationship to prior work

Allen, Heller, and Pons (2022), Sections 2–3, introduce MA and MB, state the common reproduction number (Theorems 2.1 and 3.2), and study local invasion and parameter sensitivity; their full text does not state the critical-seed, final-size coefficient, or the noncommutation of seed and behavioral-turnover limits. Magal, Seydi, and Webb (2018) establish multigroup final-size theory with conserved population **within each group**, whereas MB exchanges susceptible and asymptomatic persons between behavior classes. El Attouga and El Khalifi (2024) give static susceptibility-heterogeneity final-size formulas and qualitative smaller outbreaks: that literature covers the fixed-class mechanism, not a theorem for arbitrarily small positive bidirectional switching and its singular comparison. Perra et al. (2011) analyze epidemic-induced fear/behavior switches whose rates depend on epidemic prevalence or social contagion, structurally different from the constant bidirectional behavior turnover in MB. General singular-perturbation principles motivate the result but no identified cited theorem supplies the precise two iterated coefficients for this MB system.

## Limitations

This is a deterministic, infinite-population-fraction ODE result at exactly \(\mathcal R_0=1\), along the specified equilibrium-behavior initial composition. It does not quantify stochastic extinction probabilities, variable behavior-switching rates dependent on disease prevalence, seeds with a non-equilibrium behavior composition, or uniformity when \(a\) scales jointly with \(\sqrt\varepsilon\). The \(a=0\) case belongs to the boundary extension of MB; not the source's positive-switching hypothesis. The full literature search cannot exclude an equivalent statement in unindexed literature, and the noncommuting-law's independent validation remains open.

## References

1. R. F. Allen, K. C. Heller, and M. A. Pons, *Analysis of SIR epidemic models with sociological phenomenon*, first public arXiv version dated 2022-07-19, arXiv:2207.08999, Sections 2–3. https://arxiv.org/abs/2207.08999 ; https://arxiv.org/html/2207.08999v2 . Primary MSC2020: 92D30.
2. P. Magal, O. Seydi, and G. F. Webb, *Final size of a multi-group SIR epidemic model: Irreducible and non-irreducible modes of transmission*, Mathematical Biosciences 301 (2018), 59–67, DOI:10.1016/j.mbs.2018.03.020. https://www.math.u-bordeaux.fr/~pmagal100p/papers/MSW%20Math%20Biosci%202018.pdf .
3. S. El Attouga and M. El Khalifi, *Note on a Susceptible-Infectious-Recovered epidemic model with the heterogeneity in susceptibility*, Chaos, Solitons & Fractals 184 (2024), 115041, DOI:10.1016/j.chaos.2024.115041. https://www.researchgate.net/publication/380790714_Note_on_a_Susceptible-Infectious-Recovered_epidemic_model_with_the_heterogeneity_in_susceptibility .
4. N. Perra et al., *Towards a characterization of behavior-disease models*, 2011 arXiv preprint arXiv:1107.0997. https://arxiv.org/html/1107.0997v1 .
