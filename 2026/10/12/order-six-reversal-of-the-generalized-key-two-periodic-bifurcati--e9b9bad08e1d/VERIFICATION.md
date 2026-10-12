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
The analytic verification starts from the three positive boundary-law equations on the generalized-key invariant set \(I_2\). Eliminating the parity ratio gives the geometric-sum formulas in `RESULT.md`; substituting them back into all three equations verifies sufficiency, while the derivation from an arbitrary nontrivial positive solution verifies necessity.

The positivity-domain proof is infinite and analytic, not an enumeration. It uses strict convexity of \(H_s(u)=u\coth(us)\) to prove strict decrease of the scalar function \(\Phi_k(s)\). The endpoint signs then give one and only one positive endpoint \(s_k\) for every integer \(k\ge4\).

The local coefficient follows from the second-order expansion of \(\sinh(ns)/\sinh s\). Its denominator is positive for \(k\ge4\). The numerator is checked directly at \(k=4,5\); for all \(k\ge6\), the logarithmic inequality in `RESULT.md` proves it is negative. The conclusion for at least four non-translation-invariant solutions uses only continuity, the strict local descent at the merger, divergence at the positivity endpoint, and parity swapping.

`verify.py` is a supplementary floating-point replay. It checks direct residuals in the source equations, reciprocal parity swapping, endpoint uniqueness on a grid plus bisection, the exact sign pattern of the analytic coefficient for many orders, and the second-order expansion. Numerical success is not used as proof for unbounded \(k\).
