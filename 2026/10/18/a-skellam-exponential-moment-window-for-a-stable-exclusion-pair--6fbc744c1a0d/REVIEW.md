# Scientific review

## Correctness — PASS
The state-dependent tagged jumps and gap transitions yield a generator eigenfunction \(e^{\theta x+u_\theta h}\) with eigenvalue \(\Lambda(\theta)\) at the boundary and in the interior. Its Doob transform has a genuine positive recurrent M/M/1 gap whenever \(\beta_\theta<\delta\). The extra condition \(B_\theta<\delta\) is exactly the integrability requirement for the back-transform; a geometric Lyapunov bound proves convergence of the required expectation, not merely convergence in law. The local rare-event lower bound follows from an ergodic law under the tilted measure, and the upper bound uses an exponential moment. The stated domain excludes any unproved continuation beyond this branch. The independent executable checker passed 1265 exact rational identities and 72 finite semigroup comparisons, but finite checks are not an infinite-time proof.

## Originality — PASS (qualified)
The 2022 full-text primary theorem already proves the stable pair's exact speed, Gaussian central limit theorem, and diffusion coefficient. Those are excluded from the new contribution. What remains is an explicit non-Gaussian exponential-moment asymptotic with fixed-gap amplitude and its local speed-deviation rate. The full texts of arXiv:2205.14990 and arXiv:2610.03206 were inspected: neither states this remaining claim. Searches for marked M/M/1 currents, equivalent tilted generators, Skellam and exclusion large deviations, and accessible mathematical findings revealed no direct coverage. A generic queueing current-LDP result not recovered by these searches remains a genuine independent-priority risk; the closed form is not claimed to be universally unknown merely because searches were negative.

## Mathematical value — PASS
The complete speed and variance of the stable two-particle cloud were known. A local non-Gaussian rare-event rate distinguishes interacting tagged-particle extremes that cannot be deduced from the published central limit theorem. The exact amplitude shows how initial spacing persists in exponential moment asymptotics even though the extensive exponent is universal for each rate quadruple. This is a natural distributional refinement of a physically motivated jamming cloud, not an arbitrary finite parameter table.

## Scope and risks
Strictly positive rates and \(a_1+b_2<b_1+a_2\), fixed initial gap, and tilts in an explicit interval only. The same-model analysis does not establish global tilts, a full large-deviation principle, or priority against every queueing-theory source.

Self-review: passed. Independent audit: not yet performed.
