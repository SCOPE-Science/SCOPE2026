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

# Scientific verification

The primary proof is written in `RESULT.md`, including the exact matrix Schur states, rate-race equivalence, finite hypoexponential integral, two-maxima rare-event independence calculation, and \(o_p(r)\) count-transfer bounds. Run `python CHECK.py` with libraries declared in `requirements.txt` to replay finite-state recursions, quadrature against the exact integral, direct-matrix Schur residual spectral norms, and seeded numerical stress tests. The direct spectrum and finite-state checks use the actual formulas; no external log or older run serves as proof.

Numerical tests do not certify infinite-index limits. The asserted asymptotic result follows from the analytical proof. Accessible primary mathematical sources were inspected for overlap; a September 2026 related source was available only as an abstract, so some bibliographic uncertainty remains. No independent audit has been performed.
