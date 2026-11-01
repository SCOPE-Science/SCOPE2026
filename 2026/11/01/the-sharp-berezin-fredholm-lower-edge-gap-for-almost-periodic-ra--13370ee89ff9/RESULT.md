# The sharp Berezin–Fredholm lower-edge gap for almost-periodic radial Fock symbols

## Finding
For any integer \(d\ge1\), let \(\mathcal F^2(\mathbb C^d)\) be the Gaussian Fock space and let \(T_p\) be its Toeplitz operator with real radial symbol \(f_p(z)=p(|z|)\), where \(p\) is a real continuous Bohr almost-periodic function on \(\mathbb R\) with \(\|p\|_\infty\le1\). Define the spectral–Berezin lower-edge discrepancy
\[
\Delta_d(p):=\liminf_{|z|\to\infty}\widetilde f_p(z)-\min\sigma_{\mathrm{ess}}(T_p).
\]
The **exact sharp universal discrepancy**, independent of the complex dimension, is
\[
\boxed{\sup_{\substack{p\in\mathrm{AP}(\mathbb R;\mathbb R)\\\|p\|_\infty\le1}}\Delta_d(p)
=2\!\left[\operatorname{erf}(\sqrt{\log2})-\operatorname{erf}\!\left(\sqrt{\frac{\log2}{2}}\right)\right]
=0.3321281499670259\ldots.}
\]
Every nonconstant admissible profile has strictly positive discrepancy, but **no admissible profile attains this supremum**. A concrete sequence of smooth periodic profiles, of growing periods and taking values in \([-1,1]\), approaches it. The optimal localized transition radius is
\[
\boxed{a_*=\sqrt{\frac{\log2}{2}}.}
\]
The same sharp constant controls the greatest achievable difference between the limiting Berezin lower bound and the Fredholm essential spectral lower bound for every finite complex dimension. It is not a claim about the largest ratio of those bounds, nor about arbitrary non-radial symbols.

## Assumptions and scope
The normalized Fock norm is \(\|h\|^2=\pi^{-d}\int_{\mathbb C^d}|h(z)|^2e^{-|z|^2}\,dV(z)\). The bounded self-adjoint Toeplitz operator is \(T_p=P M_{f_p}\), where \(P\) is the Fock projection. Its Berezin transform is \(\widetilde f_p(z)=\pi^{-d}\int_{\mathbb C^d}p(|w|)e^{-|w-z|^2}\,dV(w)\). The essential spectrum is the Fredholm essential spectrum; in this self-adjoint setting its minimum exists.

For \(t>0\), let the one-dimensional heat kernel and heat action be
\[
G_t(x)=(4\pi t)^{-1/2}e^{-x^2/(4t)},\qquad (H_tp)(s)=\int_{\mathbb R}G_t(y)p(s+y)\,dy.
\]
A real Bohr almost-periodic function is the uniform limit of real finite trigonometric sums. It has relatively dense approximate periods and a compact translation hull in the supremum topology. The symbols in the theorem have a fixed normalization \(\|p\|_\infty\le1\); without this normalization the extremal gap scales and has no finite upper bound.

## Proof
**1. Identification of the two exact asymptotic lower edges.** Radial invariance makes the monomial subspace of total degree \(m\) an eigenspace with eigenvalue
\[
\lambda_m=\frac{1}{\Gamma(m+d)}\int_0^\infty p(\sqrt u)u^{m+d-1}e^{-u}\,du
=\mathbb E\,p(\sqrt{X_{m+d}}),
\]
where \(X_k\) has gamma law of shape \(k\) and unit scale. The central limit theorem and the delta method imply \(\sqrt{X_k}-\sqrt k\Rightarrow N(0,1/4)\). Therefore for every exponential mode \(e^{i\omega s}\), the eigenvalue is asymptotic to its heat-filtered value \(e^{-\omega^2/8}e^{i\omega\sqrt{m+d}}\). Uniform approximation by trigonometric polynomials and contractivity of the averaging operators extend this to every \(p\) considered:
\[
\lambda_m=(H_{1/8}p)(\sqrt{m+d})+o(1).
\]
This square-root-scale Gaussian approximation is consistent with, and in one complex dimension already follows from, Esmeral and Maximenko's Proposition 6.5 (2015); it is **background, not the claimed new optimization**.

On the other hand, taking \(z=se_1\), the coherent-state formula is \(\widetilde f_p(se_1)=\mathbb E\,p(|se_1+W|)\), where \(W\) is standard complex Gaussian. Since \(|se_1+W|-s\to\operatorname{Re} W_1\sim N(0,1/2)\) almost surely as \(s\to\infty\), the same finite-mode argument gives
\[
\widetilde f_p(se_1)=(H_{1/4}p)(s)+o(1).
\]
Both remainder limits hold independently of dimension. For a continuous Bohr almost-periodic function \(g\), the values along the increasing mesh \(\sqrt{m+d}\) (whose gaps tend to zero) have cluster set \([\inf g,\sup g]\): relatively dense approximate periods reproduce values arbitrarily far out, and the vanishing mesh detects them. Consequently, each finite-dimensional eigenspace contributes only finite multiplicity, and
\[
\min\sigma_{\mathrm{ess}}(T_p)=\inf_{s\in\mathbb R}(H_{1/8}p)(s),\qquad
\liminf_{|z|\to\infty}\widetilde f_p(z)=\inf_{s\in\mathbb R}(H_{1/4}p)(s).
\]
These formulae justify the operator-theoretic interpretation of the optimization.

**2. Universal sharp upper bound.** Write \(m_1=\inf H_{1/8}p\), \(m_2=\inf H_{1/4}p\). The heat-semigroup identity \(H_{1/4}=H_{1/8}H_{1/8}\) implies \(m_2\ge m_1\). Choose \(s_j\in\mathbb R\) with \((H_{1/8}p)(s_j)\to m_1\). For every \(j\), \(m_2\le(H_{1/4}p)(s_j)\). It follows that
\[
0\le\Delta_d(p)=m_2-m_1\le\|G_{1/4}-G_{1/8}\|_{L^1(\mathbb R)}.
\]
The Gaussian kernels are \(G_{1/8}(x)=\sqrt{2/\pi}\,e^{-2x^2}\) and \(G_{1/4}(x)=\pi^{-1/2}e^{-x^2}\). They cross at precisely \(x=\pm a_*\), with \(G_{1/8}>G_{1/4}\) for \(|x|<a_*\). Therefore
\[
\begin{aligned}
\|G_{1/4}-G_{1/8}\|_1
&=2\int_{-a_*}^{a_*}(G_{1/8}-G_{1/4})(x)\,dx\\
&=2\left[\operatorname{erf}(\sqrt{\log2})-\operatorname{erf}(\sqrt{\log2/2})\right].
\end{aligned}
\]
This proves the stated universal bound and its exact value.

**3. A sequence of smooth periodic symbols approaching equality.** For any \(L>4a_*\), define the \(L\)-periodic sign profile \(q_L\) by \(q_L(x)=-1\) when \(\operatorname{dist}(x,L\mathbb Z)<a_*\), and \(q_L(x)=1\) otherwise. For \(t>0\), set \(Q_t=\int_{-a_*}^{a_*}G_t(x)\,dx\). For every \(s\), the heat average of \(q_L\) equals \(1-2\) times the Gaussian mass of the union of the negative intervals centered at \(L\mathbb Z\). The negative interval nearest \(s\) has mass at most \(Q_t\), because a centered interval maximizes Gaussian mass among intervals of a given length. All remaining intervals are at distance at least \(L/2-a_*\) from \(s\), and thus have combined Gaussian mass at most \(\int_{|x|\ge L/2-a_*}G_t(x)\,dx\). Evaluating at \(s=0\), the central negative interval has mass at least \(Q_t\). Hence
\[
1-2Q_t-2\int_{|x|\ge L/2-a_*}G_t(x)\,dx
\le\inf_{s\in\mathbb R}(H_tq_L)(s)\le1-2Q_t,
\]
so \(\inf H_tq_L\to1-2Q_t\) as \(L\to\infty\). In particular,
\[
\lim_{L\to\infty}\big(\inf H_{1/4}q_L-\inf H_{1/8}q_L\big)
=2(Q_{1/8}-Q_{1/4})=\|G_{1/4}-G_{1/8}\|_1.
\]
Although \(q_L\) is discontinuous, smooth it by convolution with a nonnegative compactly supported \(C^\infty\) approximate identity \(\eta_\varepsilon\) of mass one: \(p_{L,\varepsilon}=q_L*\eta_\varepsilon\). Each smoothed profile is real, smooth, \(L\)-periodic and has supremum norm at most one. Since \(H_tq_L\) is globally Lipschitz with constant at most \(\|G_t'\|_1\), uniformly in \(L\),
\[
\|H_t p_{L,\varepsilon}-H_tq_L\|_\infty\le\varepsilon\|G_t'\|_1
\]
when the mollifier is supported in \([-\varepsilon,\varepsilon]\). Choosing \(\varepsilon=1/L\) and letting \(L\to\infty\) proves attainability **in the sense of a supremum** by admissible smooth periodic functions.

**4. Strict nonattainment by all continuous almost-periodic profiles.** Suppose some admissible \(p\) attained the upper bound. With the minimizing sequence \(s_j\) from step 2, equality forces
\[
\int_{\mathbb R}(G_{1/4}-G_{1/8})(y)p(s_j+y)\,dy
\longrightarrow\|G_{1/4}-G_{1/8}\|_1.
\]
By compactness of the translation hull, pass to a subsequence for which \(p(s_j+\cdot)\) converges uniformly to a continuous real function \(q\) with \(|q|\le1\). Equality in the \(L^1\)--\(L^\infty\) pairing requires \(q(y)=\operatorname{sgn}(G_{1/4}-G_{1/8})(y)\) almost everywhere. The right-hand side changes discontinuously at both \(\pm a_*\), contradicting continuity of \(q\). Thus the supremum is never attained.

**5. Positivity for every nonconstant profile.** If \(p\) is nonconstant, \(g=H_{1/8}p\) is nonconstant: the Gaussian Fourier multiplier \(e^{-\omega^2/8}\) never annihilates a Bohr frequency, and Fourier uniqueness holds for almost-periodic functions. If \(\inf H_{1/8}g=\inf g\), translating \(g\) along a minimizing sequence and extracting a uniformly convergent subsequence gives a function \(g_*\ge\inf g\) with \(H_{1/8}g_*(0)=\inf g\). Strict positivity of the Gaussian kernel forces \(g_*\) constant, contradicting the positive oscillation of every translate. Hence \(\Delta_d(p)>0\) for nonconstant \(p\); for constant \(p\), it vanishes.

## Verification
A standalone numerical check independently evaluates both Gaussian kernels, their analytic crossing point and exact total-variation norm; it checks the upper bound against a two-frequency test profile and verifies the periodized negative-bump asymptotics at increasing periods. It also tests the degreewise gamma-integral and coherent-Gaussian approximations for several dimensions and degrees. These finite computations are diagnostics, not substitutes for the heat, compact-hull or nonattainment arguments above. Run the standalone `check.py` with Python, NumPy and SciPy.

## Relationship to prior work
Esmeral and Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906 (2015), Proposition 6.5, **already obtain the one-dimensional Gaussian heat approximation at time \(1/8\)** for general bounded radial symbols. It is used explicitly as a prior ingredient here, not counted as a new discovery. Looi, *Positive Berezin liminf does not imply essential positivity for radial Toeplitz operators on Bergman and Fock spaces*, arXiv:2603.10879 (first public March 11, 2026), proves explicit oscillatory counterexamples in every complex dimension, including the relevant distinct one-frequency attenuation factors. The new claim is the **universal exact optimization** of the lower-edge discrepancy over all normalized continuous Bohr almost-periodic profiles, its nonattainment, and a smooth periodic sharpness sequence; neither inspected primary text supplies this extremal constant.

Bdarneh, *Toeplitz \(C^*\)-algebras on radially weighted Fock spaces: commutativity and spectral representation*, arXiv:2609.20652 (2026), gives general invariant-symbol eigenvalue formulas and nonstandard-weight phenomena. Its complete accessible 21-page text concerns different classification questions and does not calculate this Gaussian two-heat extremum. A result stated in different heat-kernel or statistical-distance terminology remains a publication-priority risk; the elementary \(L^1\) calculation alone is classical, while the operator-theoretic sharp value and strict nonattainment are the specific claims assessed here.

## Limitations
The result is confined to Gaussian Fock spaces, bounded real continuous Bohr almost-periodic radial profiles normalized by their \(L^\infty\) norm, and the asymptotic lower edges. It does not optimize arbitrary bounded measurable radial symbols, characterize individual finite-degree eigenvalues, prove an analogous sharp Bergman-space constant, or establish publication priority over all inaccessible historical sources. The supremum is not attained within the stated class. No independent mathematical audit has been performed.

## References
1. S. Looi, *Positive Berezin liminf does not imply essential positivity for radial Toeplitz operators on Bergman and Fock spaces*, arXiv:2603.10879, March 11, 2026, https://arxiv.org/abs/2603.10879.
2. K. Esmeral and E. A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906, May 29, 2015, Proposition 6.5, https://arxiv.org/abs/1505.07906.
3. K. Bdarneh, *Toeplitz \(C^*\)-algebras on radially weighted Fock spaces: commutativity and spectral representation*, arXiv:2609.20652, September 2026, https://arxiv.org/abs/2609.20652.
