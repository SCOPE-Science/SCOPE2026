# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The homogeneous reduction of both source schemes is algebraic.  With \(C_0=|\Omega|c/\varepsilon^2\), one has \(S_n=(\sqrt{|\Omega|}/\varepsilon)Q_n\).  Scaling \(r^n=(\sqrt{|\Omega|}/\varepsilon)q^n\) converts the SAV phase and auxiliary equations exactly into the IEQ equations, including consistent initialization, so the conjugacy holds by induction for all iterates.

Eliminating the first auxiliary update gives
\[
u^1(c)=u_0+\frac{x u_0(1-u_0^2)(A+4c)}{A+4c+2xu_0^2A}.
\]
Its derivative with respect to \(c\) is strictly positive for \(x>0\) and \(0<u_0<1\).  Solving \(u^1>1\) gives the stated \(\tau_*(c)\) exactly.  Direct differentiation gives a strictly negative threshold derivative, and the endpoint limits follow by taking \(c\downarrow0\) and \(c\to\infty\).  The source paper's formula for the second IEQ/SAV scaling factor is positive, hence the sign of \(u^2-u^1\) is exactly the sign of \(u^1(1-(u^1)^2)\).  This proves the critical-shift phase diagram.  The supplied deterministic script independently evaluates both recurrences and reproduces the exact conjugacy and sign switch to floating-point precision.

Adversarial checks included dimensional normalization of the SAV constant, the strict-versus-nonstrict endpoint cases, positivity of the first iterate, and the distinction between homogeneous and nonhomogeneous dynamics.  At \(x=1/[u_0(1+u_0)]\), no finite positive shift reaches the limiting overshoot threshold; at \(x=1/[u_0(1-u_0)]\), every positive shift lies beyond its threshold.  These endpoint conventions are reflected in the phase diagram.

## Originality

**PASS, to the best of our knowledge.** The full HTML of arXiv:2609.19023v1 was inspected at its IEQ and SAV definitions, homogeneous counterexamples, threshold formulas, perturbation arguments, numerical sections, and conclusions.  The paper gives the two large-step threshold formulas separately and fixes particular auxiliary constants in its experiments, but no normalized IEQ/SAV conjugacy, monotonicity of the failure threshold with respect to the shift, or critical-shift sign bifurcation was located.  Repository searches by source identifier, Allen–Cahn, IEQ/SAV, auxiliary-constant, and potential-shift terminology found no prior SCOPE record covering the claim.

The broad phenomenon of auxiliary-shift sensitivity is explicitly excluded from the novelty claim.  Liu (arXiv:1906.03621) notes that selecting the positive constant in classical IEQ/SAV can be non-obvious.  Shen and Yang (2020) present IEQ and SAV in a unified framework.  Jiang et al. (JCP 2022, 110954) explain that temporal discretization breaks exact consistency between numerical auxiliary variables and their continuous definitions.  Most importantly, Russo, Ducceschi, and Bilbao (Nonlinear Dynamics 2026, article 857) explicitly report that SAV global error for nonlinear string models can depend strongly on a potential-shift constant and analyze how a shift affects local regularity/error constants.  These works establish that shift dependence in auxiliary-variable methods is not new in general.

The remaining novelty claim is source-specific and narrower: for the first-order Allen–Cahn IEQ/SAV schemes of arXiv:2609.19023v1, the two homogeneous dynamics collapse exactly under \(C_{\rm IEQ}=\varepsilon^2C_0/|\Omega|\), and their pointwise-monotonicity failure has an explicit one-parameter phase diagram with a unique shift that flips the second increment.  No checked source was found to state this exact result.

Residual originality risk remains because the IEQ/SAV literature is large, and older analyses of scalar reductions or parameter dependence may contain equivalent algebra without using the present pointwise-monotonicity language.  The 2020 survey was inspected through its accessible public text and relevant definitions rather than line by line in every application, and the 2026 nonlinear-string paper concerns a different Hamiltonian/wave setting.  The motivating Allen–Cahn preprint is recent, so contemporaneous revisions or follow-up notes are also possible.

## Value

**PASS.** The result converts the source paper's qualitative statement “sufficiently large time steps fail” into a complete shift/time-step phase diagram on the invariant class used to prove failure.  It also shows that two apparently separate IEQ and SAV counterexamples are one normalized recurrence and that an auxiliary constant which is irrelevant to the continuous Allen–Cahn equation can change the sign of a discrete phase increment.  This matters for interpretation and parameter selection: modified-energy stability alone does not remove a convention-dependent dynamical degree of freedom.

The explicit transition window is practically informative.  Within it, the same \(u_0\), \(\varepsilon\), and \(\tau\) can be monotone for one admissible positive shift and wrong-signed for another.  The large-shift limit of the first update is the explicit-Euler reaction step, explaining mechanistically why larger shifts lower the overshoot threshold in this scheme.

## Limitations

The exact IEQ/SAV conjugacy holds only for spatially homogeneous states.  Nonhomogeneous IEQ and SAV remain different because one auxiliary variable is local and the other is global.  The theorem classifies the first two homogeneous steps from consistent initialization; it does not provide a long-time convergence rate, nonlinear stability region, or universal optimal-shift rule.  Existing work shows that larger shifts can have different benefits in other SAV settings, so the monotone-threshold conclusion should not be generalized beyond the analyzed Allen–Cahn recurrence.  No new perturbation radius is derived for nonhomogeneous data.
