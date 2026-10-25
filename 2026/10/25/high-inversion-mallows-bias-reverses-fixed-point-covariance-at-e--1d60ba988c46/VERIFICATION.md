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
# Verification scope

The standalone standard-library program `mallows_fixedpoint_checker.py` was executed after construction and returned `PASS: 393 exact checks; n=2..8; finite checks supplement analytic all-n proof.` It independently enumerates every permutation through eight symbols, verifies the \(q\)-factorial inversion polynomial, and evaluates covariance as both a direct exact moment and a derivative of the fixed-point generating polynomial. It checks the uniform covariance formula, the end-regime signs at the stated rational cutoffs, adjacent-transposition coefficients, coefficient bounds, and exact three-symbol formula at multiple rational biases.

The general all-size theorem is verified analytically by inversion-sequence bounds \(a_k\le n^k\), the adjacent-transposition bound \(|b_k|\le2ka_k\), and the derivative bound \(|Z^2(d\mathbb E F/dx)-b_1|<1\) for \(0<x\le 1/(100n^2)\). Exhaustive enumeration through eight symbols alone would not establish any statement for arbitrary \(n\). No independent scientific audit is claimed.
