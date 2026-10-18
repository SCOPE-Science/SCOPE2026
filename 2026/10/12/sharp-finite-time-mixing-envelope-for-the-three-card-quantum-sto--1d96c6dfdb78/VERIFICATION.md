---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For every t>0, γ>0, α≥0, H equal the central average of the 3 left transpositions on C[S3], and Φ the corresponding conjugation-average channel, their commutation yields classical convolution with the unitary central spectral distribution. S3 characters give ξ=e^(−2γt)(1+2cos²αt)/3, η=e^(−γt)(1+2cosαt)/3; exact inversion gives D=(|ξ+4η|+3ξ+2|ξ−2η|)/12. Piecewise derivatives on c∈[−1,1] have signs negative, negative, positive, so unique optimal cosine c*=(2−sqrt(4+4x−2x²))/(2x)∈(−1/2,0), min D=x²(1+2c*²)/6, asymptotic coefficient 1/4, no exact mixing since ξ>0. Infinitely many α map to that cosine. Independent 6×6 spectral classical/quantum propagation matched 24 (x,c) cases (finite corroboration, not continuum uniqueness proof).

## originality

PASS

The original He–Hutsalyuk–Mussardo–Stampiggi source establishes the quantum-stochastic permutation model, character convolution, and qualitative speedup. The full primary text could not be independently inspected; its arXiv abstract and the package describe a two-card worked instance. The explicit full S3 globally optimized cosine/time-dependent TV bound is an additional nontrivial piecewise calculation, best-of-knowledge uncovered with a significant documented primary-access risk.

## value

PASS

A sharp six-state fixed-observation optimum gives the exact coupling-controlled mixing envelope, residual prefactor, and no-finite-time-mixing boundary, not just the generic previously known speedup. It is a natural smallest nontrivial permutation group; no all-S_n generalization claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
