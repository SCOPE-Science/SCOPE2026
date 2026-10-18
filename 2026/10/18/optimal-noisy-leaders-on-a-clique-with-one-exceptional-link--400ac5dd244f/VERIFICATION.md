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

# Reproducibility and verification

Run `python3 verification.py` with Python 3 (standard library only). This computes all grounded inverses from scratch with exact rational Gaussian elimination rather than using the rank-one inverse as the matrix-construction method.

The checked finite ranges are \(3\leq n\leq8\), \(1\leq q\leq n\), \(\kappa\in\{1/2,3,10\}\), and \(w\in\{1/3,1,7/3,19,27/22\}\). All subsets of each size are checked, comprising 495 parameter instances and 7470 actual leader sets. Each result is compared with the predicted exact common baseline and endpoint-type increments. The selected minimizer orbit(s), including ties, are checked against the analytical rule.

An additional exact-rational check establishes \(D=-1/675\), \(H=22/3375\) when \((n,q,\kappa)=(5,3,10)\), yielding the transition \(w=27/22\). The tests are finite and do not certify all real parameters; the accompanying proof gives the unrestricted result by algebraic matrix identities and strict inequalities. Independent audit remains unperformed.
