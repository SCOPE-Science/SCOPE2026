# Scientific review

**Correctness — PASS.** The exact Itô second-moment closure, two successive strictly positive variation-of-constants comparisons, strict monotonicity, and the constant-stiffness tail establish the global time minimum with the endpoint constraint. The critical \(\log\log\) term comes from an explicitly nonzero Jordan-type forcing coefficient \(2\delta_y\) rather than a heuristic numerical fit. The accompanying independent ODE/quadrature checks pass but are not used as proof. All parameters are strictly positive; only stiffness increase is treated.

**Originality — PASS, with residual priority risk.** The same physical model and tolerance metric, and an instantaneous step-time baseline, are already in Casert–Whitelam (2024), including supplementary section S3B. The new claim excludes those observations and instead determines exact globally optimal finite-slew admissible controls for all tolerances, the terminal endpoint constraint, and three high-accuracy asymptotics with critical double logarithm. Davis–Proesmans–Fodor (2024) studies approximate dissipation minimization under slow driving, and Gupta–Klapp–Sivak (2023) controls excess work in a different bistable landscape. Targeted independent mathematical-record searches did not find the precise reachability result; this is not a uniqueness proof over all publications. A general positive-system reachability theorem could subsume it.

**Value — PASS.** Real actuators cannot jump stiffness discontinuously, whereas the main-source optimal-speed benchmark allows that idealization. The exact finite-slew duration and the critical logarithmic slowdown provide meaningful instrument-design benchmarks for choosing stiffness and required hold time near small tolerances. The full attainable-time boundary and the resonance are structural, not arbitrary numerical observations.

The result is limited to centered second moments for an independent-Gaussian single-particle process, not the full nonequilibrium state, heat-optimal control, or interacting active matter.

Self-review: passed. Independent audit: not yet performed.
