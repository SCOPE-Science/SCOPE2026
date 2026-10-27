# Sharp unequal-depth Kelvin–Helmholtz onset selection

## Finding
For two stably stratified, inviscid fluids of unequal finite depths beneath rigid horizontal boundaries, there is a **sharp weighted-depth transition** between instability that first appears in the long-wave limit and instability that first appears at exactly one nonzero wavenumber. The global criterion involves only three weighted depth moments; the finite-wavenumber branch emerges with an explicit square-root law.

Write \(\rho_{\mathrm l}>\rho_{\mathrm u}>0\) for lower and upper densities, \(h_{\mathrm l},h_{\mathrm u}>0\) for the depths, \(h_{\mathrm l}\ne h_{\mathrm u}\), \(g>0\), and \(\gamma>0\) for gravity and surface tension. Define
\[
 A=g(\rho_{\mathrm l}-\rho_{\mathrm u}),\quad
 M_j=\frac{h_{\mathrm l}^j}{\rho_{\mathrm l}}+\frac{h_{\mathrm u}^j}{\rho_{\mathrm u}},\quad
 b=\frac A\gamma,\quad b_c=\frac{3M_1}{M_3}.
\]
For relative interfacial velocity \(U=|U_{\mathrm l}-U_{\mathrm u}|\), every positive wavenumber \(k\) is unstable precisely when
\[
 U^2>\gamma (b+k^2)S(k^2),\quad
 S(z)=\sum_{i\in\{\mathrm l,\mathrm u\}}
 \frac{\tanh(h_i\sqrt z)}{\rho_i\sqrt z},\quad S(0)=M_1.
\]
The exact onset threshold is \(U_{\rm crit}^2=\gamma\inf_{z>0}(b+z)S(z)\). Its complete classification is:

* If \(b\le b_c\), \((b+z)S(z)\) increases strictly on \(z>0\) and \(U_{\rm crit}^2=A M_1\). The infimum is approached only as \(k\to0^+\).
* If \(b>b_c\), this function has a **unique** strict global minimizer \(z_*>0\), characterized without competing roots by
\[
 -\frac{S(z_*)}{S'(z_*)}-z_*=b,
 \qquad U_{\rm crit}^2=\gamma(b+z_*)S(z_*).
\]
The selected marginal wavenumber is \(k_*=\sqrt{z_*}\).

The bifurcation at \(b_c\) is quantitative. Put
\[
 C=\frac{12M_1M_5}{5M_3^2}-2\ge\frac25.
\]
At fixed positive depths and densities, as \(\varepsilon=b-b_c\to0^+\),
\[
 k_*^2=\frac{\varepsilon}{C}+O(\varepsilon^2),\qquad
 bM_1-(b+k_*^2)S(k_*^2)=\frac{M_3}{6C}\varepsilon^2+O(\varepsilon^3).
\]
Both are sharp, positive-coefficient asymptotics. At the onset shear, a finite-wavenumber mode has a repeated real frequency only in the second case; such a double root can cause algebraic time growth, but strict exponential instability requires \(U>U_{\rm crit}\).

The selection boundary differs physically from the corresponding *zero-shear gravity–capillary phase-speed* boundary whenever the unequal depths are not specially balanced. The latter has critical surface tension
\[
 \gamma_{\rm phase}=\frac A3\frac{\rho_{\mathrm l}h_{\mathrm l}+\rho_{\mathrm u}h_{\mathrm u}}{\rho_{\mathrm l}/h_{\mathrm l}+\rho_{\mathrm u}/h_{\mathrm u}},
\]
while the shear-instability selection boundary is \(\gamma_{\rm KH}=AM_3/(3M_1)\), and
\[
 \gamma_{\rm KH}-\gamma_{\rm phase}=\frac A3
 \frac{(h_{\mathrm l}^2-h_{\mathrm u}^2)(h_{\mathrm l}\rho_{\mathrm u}-h_{\mathrm u}\rho_{\mathrm l})}
 {h_{\mathrm l}\rho_{\mathrm u}+h_{\mathrm u}\rho_{\mathrm l}}.
\]
Either sign occurs for admissible density and depth contrasts. Consequently the two wave-selection problems are not equivalent in general unequal-depth configurations.

## Assumptions and scope
The fluids are immiscible, homogeneous within each layer, incompressible, inviscid, irrotational away from the interface, and occupy parallel layers with impermeable rigid boundaries at vertical distances \(h_{\mathrm l}\) and \(h_{\mathrm u}\). Gravity points downward, heavier fluid lies below, and tangential base velocities are constant within each layer. The interface has constant positive tension. The conclusion concerns linear temporal normal modes with real horizontal wavenumber \(k>0\), in a horizontally unbounded geometry. No assertion is made about viscosity, finite horizontal periods, smooth shear profiles, nonlinear saturation, or the fastest-growing mode above onset. The unique \(k_*\) is the **first marginal** mode as shear increases, not necessarily the fastest-growing mode at a larger shear.

## Proof
**1. Exact dispersion reduction.** Let \(\alpha_i(k)=\rho_i\coth(kh_i)>0\). Solving Laplace's equation for each velocity potential, imposing impermeability at the lids and the linearized kinematic and capillary pressure conditions at the interface, yields the standard quadratic relation
\[
 \alpha_{\mathrm l}(\omega-kU_{\mathrm l})^2+
 \alpha_{\mathrm u}(\omega-kU_{\mathrm u})^2=A k+\gamma k^3.
\]
Completing the square shows that the temporal frequency becomes nonreal exactly when
\[
 U^2>\left(\frac A k+\gamma k\right)
 \left(\frac1{\alpha_{\mathrm l}}+\frac1{\alpha_{\mathrm u}}\right).
\]
Because \(\alpha_i^{-1}=\tanh(kh_i)/\rho_i\), the displayed instability condition in the finding follows. Equality gives a repeated real root; a linearly growing generalized mode is possible, so this is a threshold for exponential instability rather than a claim of uniform boundedness. Taking the infimum gives the shear-onset characterization.

**2. Positive spectral decomposition.** Set \(z=k^2\). The standard Mittag–Leffler identity (equivalently, the endpoint Green function of a Dirichlet–Neumann interval Laplacian) is
\[
 \frac{\tanh(h\sqrt z)}{\sqrt z}
 =\frac2h\sum_{n=0}^{\infty}
 \frac1{z+\pi^2(n+\tfrac12)^2/h^2},\qquad z\ge0.
\]
It follows that \(S(z)=\sum_j c_j/(z+a_j)\), with \(c_j,a_j>0\); the series and its required derivatives converge locally uniformly on \([0,\infty)\). In particular \(S'(z)<0\). Define
\[
 B(z)=-\frac{S(z)}{S'(z)}-z
 =\frac{\sum_j c_j a_j/(z+a_j)^2}
 {\sum_j c_j/(z+a_j)^2}.
\]
This is the mean of the positive spectral numbers \(a_j\) under the probability weights proportional to \(c_j/(z+a_j)^2\). Differentiation gives
\[
 B'(z)=-2\operatorname{Cov}_z\!\left(a,\frac1{z+a}\right)>0.
\]
The covariance is strictly negative because \(a\mapsto a\) is strictly increasing and \(a\mapsto(z+a)^{-1}\) strictly decreasing, while the discrete measure has at least two distinct support points. The inequality also follows by symmetrizing the corresponding double series, whose terms are nonnegative and some strictly positive.

**3. Endpoints and global selection.** The Taylor series of \(\tanh\) yields
\[
 S(z)=M_1-\frac{M_3}{3}z+\frac{2M_5}{15}z^2+O(z^3),
\]
so \(B(0)=3M_1/M_3=b_c\). As \(z\to\infty\), \(S(z)\sim(1/\rho_{\mathrm l}+1/\rho_{\mathrm u})z^{-1/2}\) and \(S'(z)\sim-\tfrac12(1/\rho_{\mathrm l}+1/\rho_{\mathrm u})z^{-3/2}\), whence \(B(z)\sim z\to\infty\). Finally
\[
 \frac{d}{dz}[(b+z)S(z)]=-S'(z)[B(z)-b].
\]
Since \(-S'(z)>0\), strict monotonicity and the range of \(B\) show that the derivative has no positive zero for \(b\le b_c\), and exactly one sign change from negative to positive for \(b>b_c\). The function diverges like \(\sqrt z\) as \(z\to\infty\), so the sole critical point is the strict global minimizer. This proves the complete onset classification, including the boundary cases.

**4. Sharp onset expansion.** Differentiating the Taylor series gives
\[
 B(z)=b_c+Cz+O(z^2),\qquad
 C=\frac{12M_1M_5}{5M_3^2}-2.
\]
The Cauchy–Schwarz inequality \(M_1M_5\ge M_3^2\) implies \(C\ge2/5>0\). Analytic inversion near zero proves \(z_*=\varepsilon/C+O(\varepsilon^2)\). Expanding \((b+z)S(z)\) and substituting this relation gives the positive quadratic difference in the finding.

**5. Distinction from the phase-speed problem.** At zero shear the two-layer gravity–capillary phase speed satisfies
\[
 c^2(k)=\frac{A+\gamma k^2}{k[\rho_{\mathrm l}\coth(kh_{\mathrm l})+\rho_{\mathrm u}\coth(kh_{\mathrm u})]}.
\]
Expanding its denominator at small \(k\) gives the indicated \(\gamma_{\rm phase}\). Direct common-denominator algebra, with positive denominators, yields the exact difference formula. Since \(\rho_{\mathrm l}>\rho_{\mathrm u}>0\) and the two depths are otherwise arbitrary and unequal, both signs of that difference occur; the two minimization kernels are not interchangeable.

## Verification
Run `python verify.py` with Python 3, NumPy, SciPy, and mpmath. The checker evaluates the exact dispersion discriminant against the scalar threshold, independently minimizes the positive-wavenumber function and compares it with the unique root, checks monotonicity on sampled positive ranges, and tests the near-critical asymptotics using high-precision arithmetic. The analytic argument above, not finite numerical sampling, establishes uniqueness for every admissible parameter value.

## Relationship to prior work
Miloshevsky and Hassanein (2010), equations (1)–(4), provide the finite-layer Kelvin–Helmholtz dispersion and explicitly discuss numerical minimization of the critical wavenumber, including the equal-depth specialization. Lannes and Ming (2015), Section 3.2 and Proposition 1, formulate the general rigid-lid two-fluid all-mode stability criterion through a minimum and provide bounds rather than an explicit critical shear. The classical finite-depth gravity–capillary phase-speed transition involves a different denominator and is a separate problem; the equal-depth specialization coincides up to a positive constant and is therefore **not** claimed as new. Here the unequal-depth global root-count theorem, exact weighted-depth boundary, critical scaling and algebraic distinction between the two onset thresholds are assessed together.

## Limitations
This theorem concerns onset of *linear temporal* Kelvin–Helmholtz instability, not the nonlinear fate of an unstable interface. No statement of statistical parameter-estimation stability or experimental error bars is made. Prior literature may contain an equivalent specialization of the all-mode stability condition; the related finite-depth analysis by Lannes and Ming already supplies its variational form. Independent scientific audit has not been performed.

## References
1. G. V. Miloshevsky and A. Hassanein, “Modelling of Kelvin–Helmholtz instability and splashing of melt layers from plasma-facing components in tokamaks under plasma impact,” *Nuclear Fusion* **50** (2010), 115005, DOI: 10.1088/0029-5515/50/11/115005. Open text: https://engineering.purdue.edu/CMUXE/GenaPDFs/NF-2010.pdf . Published 2010-09-30.
2. D. Lannes and M. Ming, “The Kelvin-Helmholtz Instabilities in Two-Fluids Shallow Water Models,” Section 3 (rigid-lid linear stability) and Proposition 1. Author-hosted text: https://david-lannes.perso.math.cnrs.fr/wp-content/uploads/2019/01/lannesming.pdf . An early public copy was indexed 2015-01-14 (HAL hal-01101993).
3. Classical finite-depth capillary–gravity phase-speed literature and dispersion relation; see the distinct wave-phase-speed formulation in Lannes and Ming, Section 3, and the references therein.
