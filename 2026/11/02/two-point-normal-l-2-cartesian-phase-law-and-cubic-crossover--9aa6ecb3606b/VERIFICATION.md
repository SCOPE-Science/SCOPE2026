---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

For \(T=aP+bQ\), the proof requires no numerical approximation. The spectral theorem for the two orthogonal projection ranges gives the exact angular norm, and splitting the absolute value of \(A+R\cos u\) at its two zeros gives the elementary closed formula. The derivative and the exact integral representation of \(x-\arctan x\) establish the sharpness of the two global phase coefficients. For \(r=1-\varepsilon\) and \(\beta=\varepsilon t\), the uniform convergence of the scalar components on bounded \(t\)-intervals proves the crossover.

Run the standard-library-only checker from these embedded files with `python3 verify_two_point.py`. It reports **909 consistency assertions passed**. It compares 78 direct angular quadratures to the exact formula, verifies monotonicity and endpoint consistency, samples upper and lower sharp cubic bounds across 240 interior phase/radius combinations, and probes the cubic and crossover asymptotics. Quadrature, sampling and asymptotic probes are not exhaustive and are not used as infinite proofs.

The result covers only two nonzero unequal-modulus spectral values of normal operators, with optional zero spectrum. The equal-modulus limiting law and a projectively orthogonal special case were previously known, and no independent novelty review or mathematical audit has been performed.
