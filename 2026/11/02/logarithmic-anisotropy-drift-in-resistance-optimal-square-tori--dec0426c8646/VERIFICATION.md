---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and proof boundaries

Execute the unchanged `python3 verify.py` from the record package using the Python 3 standard library. The package records the replay output `VERIFY_OK 100 checks; exact traces, Fourier-resolvent identity, finite-size constant, optimized drift`.

The checker constructs weighted toroidal Laplacians at \(n=3,4\) and rational conductances, computes the exact trace of the inverse of \(L+\mathbf1\mathbf1^T/n^2\) minus one using rational Gaussian elimination, and compares to the Fourier formula. Additional checks compare the finite-cycle resolvent at seven sizes and seven anisotropies, measure the constant-term error at three larger sizes across seven anisotropies, and check numerically the directional optimizer for five price choices at selected sizes. The numerical optimizer searches within a finite interval; it does not certify localization for unbounded \(n\).

The proof localizes the true minimizer by strict convexity in the horizontal budget share, using the fixed-anisotropy expansion at three points. It then uses the uniform endpoint-layer estimate with two parameter derivatives and evaluates the differentiated expansion at the stationary point. No finite test certifies those asymptotic steps. The unordered-pair resistance sum is \(n^2\) times the trace of the Laplacian pseudoinverse.
