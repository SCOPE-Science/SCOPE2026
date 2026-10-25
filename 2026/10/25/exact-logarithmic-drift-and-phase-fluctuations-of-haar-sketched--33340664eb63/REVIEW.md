# Self-review of Haar-sketched Euler rotation

## Correctness

**PASS.** For each deterministic nonzero initial state, fresh Haar angles generate independent uniform relative angles and hence the exact complex factor in the theorem. The logarithm is valid on the full factor circle because its radius is smaller than its center distance from zero. Fourier orthogonality proves the complete second-order log-radius/phase covariance; elementary moment factorization yields the first and second complex norms. The determinant lemma proves every sample update has determinant one. Exact finite-time expansion proves the strictly positive compensated strong-error limit and Lindeberg applies to the bounded triangular array. The included reproducibility program passed angular integration, direct update, determinant, path simulation and small-step checks; finite tests are not substituted for proof.

## Originality

**PASS subject to literature-access risk.** The source on right-sketched time stepping defines the method and gives broad bias, variance and error bounds rather than the joint phase-radius law. Full texts of two-shear Lyapunov bounds and selected isotropic matrix ensemble results were compared by mathematical implication, including what the stronger general results actually quantify. Nearby indexed claims on harmonic Langevin sampling and coupled numerical rollout have different objects and do not imply the theorem. The specialized combination of joint log fluctuation law and exact compensated finite-time error was not found in searched sources; this does not prove absolute uniqueness. A plausible 2026 rotationally invariant random-product article was available only as an abstract, so priority remains uncertain.

## Mathematical value

**PASS.** Stochastic right sketches reduce least-squares costs but may change structural invariants. The derived nonzero almost-sure expansion within strictly area-preserving one-step maps, and the sharp root-step strong-error constant after correcting mean bias, give physically interpretable benchmarks that a generic variance inequality hides. The result specifies all parameters and limiting regimes, and isolates equal phase/radial stochastic fluctuation variances.

## Literature and limitations

Motivation and method: Dong, Schwerdtner and Peherstorfer, arXiv:2512.19009. Adjacent shear bounds: Thiffeault, arXiv:1706.03398. Matrix-ensemble background: Forrester and Zhang, arXiv:1805.05529. Residual priority risk: Q. Dong, DOI:10.1016/j.spl.2026.110703 (abstract only). The theorem is not established for higher dimensions, correlated sketches, nonlinear problems, or numerical error in the sketch solve. Its normalized phase is unwrapped and the step preserves area, not energy.

Self-review: passed. Independent audit: not yet performed.
