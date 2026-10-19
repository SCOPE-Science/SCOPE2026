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

# Verification

The finite-dimensional assertion follows from the exact polynomial identity \((t-s)(t-A)^2\) and its factorial-weighted Gaussian moment. In particular \(s=1,A=3\) has coefficient vector \((-9,15,-7,1)\), whose factorial pairing is \(-2\). The standalone `verify.py` checks those coefficients, evaluates the factorial pairing exactly, and checks additional rational choices \(s\in\{1,2,4,9\}\). It also independently validates coefficient-sign realization for those explicit polynomial inputs.

The all-radius assertion is analytic, not computational: weighted polynomial completeness plus Cauchy--Schwarz guarantees a strictly negative signed integral for each real \(s>0\). Orthogonal coordinate splitting converts it to an actual finite vector-polynomial witness. No numerical approximation proves the density lemma. Historical-priority and independent external validation remain open.
