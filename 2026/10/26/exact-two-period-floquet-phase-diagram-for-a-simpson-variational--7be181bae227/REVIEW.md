# Scientific review

**Correctness — PASS.** The stated map is the canonical harmonic-oscillator Simpson step in dimensionless coordinates. Exact polynomial factorization proves the full strict Floquet classification, and the monotone off-diagonal ratio resolves all neutral boundaries. The reciprocal-product identity and local resonance exponent are proven algebraically. The executable exact-rational polynomial verifier reports success. No finite test is substituted for an infinite statement.

**Originality — PASS on examined evidence.** The 2023 primary work derives the constant-step symplectic map, fixed-step stability and preserved modified energy. It does not present an alternating-step Floquet phase diagram. Skeel's 1993 result shows variable-step Störmer/Verlet instability, which motivates the question but does not determine this method's exact two-parameter stability region. The accessible summary of the 2024 general-quadratic Simpson follow-up describes a fixed-step implicit scheme and multidegree-of-freedom benchmarks, not the stated switching result. Semantic database searches found no matching implication. The inaccessible complete follow-up and classical literature are residual originality risks, not claimed absence-of-evidence proofs.

**Value — PASS.** The complete two-step switching classification directly addresses whether fixed-step symplectic energy control survives periodic step adaptation. It identifies both a sharp resonance with arbitrarily small perturbations and a nontrivial stable curve under large changes of steps. These are structural design boundaries for a recently proposed geometric integrator rather than an arbitrary sample computation.

**Limits.** The exact theorem is restricted to the specified one-mode canonical map and repeated two-step switching; it does not establish general adaptive-scheme, nonlinear, or floating-point results. Published methods may use different variable-step conventions.

Self-review: passed. Independent audit: not yet performed.
