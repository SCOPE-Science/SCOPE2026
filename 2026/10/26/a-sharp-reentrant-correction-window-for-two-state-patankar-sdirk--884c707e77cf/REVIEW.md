# Three-axis scientific review

## Correctness — PASS

The proof derives the two SDIRK stage components from the two-by-two exchange resolvent, constructs the source's stage-ratio averaged generator, explicitly solves the corrected system, and takes the denominator-floor limit in all three predictor regimes (interior, lower face, upper face). The first stage is uniformly strictly interior for each fixed admissible parameter tuple, so the singular weights diverge precisely as asserted. Differentiating the scalar SDIRK stability function gives its global negative minimum and the sharp quadratic window; direct scalar ODE integration establishes the positive exact comparator. A separate standard-library verifier independently reconstructs the stages and correction by matrix inversions and passes 9,020 assertions. All quantifiers and boundary cases are covered analytically.

## Originality — PASS, with remaining priority risk

The originating 2026 article specifies and analyzes the source method, positivity and formal accuracy, but does not report an exact vanishing-denominator-floor limit on the complete two-state simplex, the sharp \(3-2\sqrt2\) rate threshold, the reentrant step-size window, or the boundary-layer coefficient. Torlo–Öffner–Ranocha's earlier analysis warns of oscillation and order loss for different Patankar families, not the claimed limit for the 2026 scheme. The fixed-cutoff small-step limit does not imply the finite-step vanishing-cutoff result; the two limiting operations ask different questions. Searches of mathematical claim records and primary literature identified no covering theorem. An unlocated equivalent within general positivity-projection theory cannot be categorically ruled out.

## Mathematical value — PASS

The exact phase diagram answers a relevant design question: when can an unconditionally positivity-preserving, conservative post-correction force a numerically stiff step onto the wrong face of the mass simplex despite a strictly positive exact state? The complete singular-floor map distinguishes a robust interior regime from a sharp clipping regime, and the rate threshold, explicit step-size interval, and \(O(\varepsilon)\) boundary layer quantify a failure unavailable from positivity or asymptotic-order statements alone. The result is a motivated nontrivial boundary for an explicitly published ODE integrator, not a numerical table or arbitrary parameter slice.

## Scope, closest literature and risks

Relevant originals: Nurkhametova et al., arXiv:2602.15271, equations (21)/(25), SDIRK21 Section 4.2.1, and full Sections 3–5; Torlo et al., arXiv:2108.07347, Sections 2–5. The source's formal small-timestep convergence analysis remains valid in its stated regime. The present theorem does not concern global error, nonlinear kinetics, adaptive steps, all-stage correction, or floating-point robustness. Primary-literature priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
