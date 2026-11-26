---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Exact full Newton cancels x, hence positive finite-time energies satisfy F_(n+1)=W_n F_n^p, p=2α. For p<1 the reversed weighted log series converges absolutely in expectation, and a two-sided stationary ergodic realization couples to the forward process with error p^n times its initial error. The marginal has full support because it includes an independent full-support log innovation, so thresholds of either sign are visited unboundedly. For the Mellin domain, direct upper and lower constant multiples of χ²_d bound W, giving the cutoff q>−d/2 without requiring the density assertion from those bounds. Independence and a finite slightly higher absolute moment of the weighted products give uniform integrability and the stated product; for q≤−d/2 the first factor already diverges. At p=1 the ordinary strong and iterated-logarithm laws give the three behaviors, and conditioning yields exactly F₀(tr A/2)^n. At p>1 the rescaled log series converges absolutely and convolution with its first independent innovation gives an atomless full-support limit; both signs occur and determine the outcome. Strict symmetric concavity follows from the negative second directional derivative, with dominated logarithms also at the rank-one limit. In d=2 the angular mean of log|a+b exp(−2iθ)|² is 2 log a by the zero constant coefficient of log(1+(b/a)exp(−2iθ)); the radial log mean is −γ. The common vector gives F₀=2 exactly at trace 4. Independent Laplace-transform quadrature gave 0.1159315157 and −0.3054725200; the rank-one limit was −0.5772156649. Replay: OPENBLAS_NUM_THREADS=1 python /workspace/independent_checks.py (NumPy/SciPy); quadrature is not evidence for a pathwise limit. ‘Rearranging’ means redistributing eigenvalue sizes, not merely permuting them. There is a non-substantive citation numbering error: arXiv:2609.10465v1 uses Theorem 2.1, Lemma 2.5 and Remark 2.4 for the relevant points; the substantive scope comparison holds.

## originality

PASS

The distinct finding is the exact unbounded-quadratic Newton stability classification and the explicit same-trace separation of almost-sure outcomes with the same expected objective trajectory. The algorithm/noise model, affine-recursion machinery, and fixed-trace expected-log bounds are not original ingredients. The combined critical stability criterion is not a parameter specialization of the motivating torus theorem or of a result on Gaussian quadratic forms alone.

## value

PASS

At the exact exponent where local deterministic scaling no longer dominates the multiplicative noise, the theorem provides a checkable Hessian-allocation boundary. Even with the same start and identical expected energy at every step, positive-definite quadratics can exhibit opposite almost-sure stability. This supplies a motivated limit case and counterexample to reliance on mean energy, with a classification across exponents for the ideal method. It does not advertise compact-domain or general nonquadratic behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
