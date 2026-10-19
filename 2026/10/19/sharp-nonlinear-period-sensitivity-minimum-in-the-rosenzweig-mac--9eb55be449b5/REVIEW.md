# Scientific review: sharp Rosenzweig–MacArthur period sensitivity

**Correctness — PASS.** A direct third-order Hopf normal form of the rational physical-time vector field, with eigenvector normalization fixed by prey's first harmonic, gives \(\operatorname{Re}G_{21}=-4/(1+h)\) and \(\operatorname{Im}G_{21}=-8\omega C(h)\). The exact crossing yields a unique small stable orbit. Positivity, endpoint divergence and Descartes' transformed derivative prove a unique sharp global minimum. The included SymPy checker passes, and finite-distance numerical shooting supports the coefficient without being used as proof.

**Originality — PASS, qualified.** The same-object 2025 analysis, read through its model setup and full Hopf/phase-portrait sections, establishes existence and stability in a state-dependently rescaled time, not this physical-time normalized period slope or unique sharp optimizer. Published related normal-form/oscillator results address other vector fields or other invariants. The 1963 source's abstract explicitly mentions a period equation, but its complete body could not be compared: a residual historical-priority risk remains. A bounded search cannot establish global novelty.

**Mathematical value — PASS.** Relative physical period and first prey harmonic are natural observables, and their leading coupling describes nonlinear slowing separately from parameter-driven shifts in equilibrium frequency. Determining its entire-parameter positive response and unique optimum gives a sharp interpretable invariant, not a textbook restatement of Hopf stability.

**Closest literature and limitations.** Rosenzweig and MacArthur (1963) originated the ecological system; the later global phase-portrait analysis derives supercritical Hopf behavior and uniqueness but uses a nonconstant time change, while Liou–Cheng addresses limit-cycle uniqueness. The result holds for shrinking stable cycles at each fixed \(0<h<1\), not global finite-amplitude period monotonicity. Primary historical priority remains uncertain due to an inaccessible article body. No independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
