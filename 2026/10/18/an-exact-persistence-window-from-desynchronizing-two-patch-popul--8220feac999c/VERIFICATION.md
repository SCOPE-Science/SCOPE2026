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

# Reproduction instructions

Run `python3 verify.py` with Python 3 and the standard library. The program proves the exact rational example by integer-fraction matrix arithmetic and checks four independently chosen asymmetric generators across eleven phase points each. The printout verifies the characteristic determinant and principal-root ordering as well as trace excess. All parameter-uniform claims rely on the symbolic argument in `RESULT.md`; a finite set of numerical calculations does not constitute a universal proof.

# Proof-to-check mapping

The key algebra is the closed exponential \(e^{At}\), constancy of \(\det Q_	au\), and positivity of \(Q_	au\) for strictly positive interpatch exchange. The determinant of \(I-Q_	au\) then controls the extinction transition only under the stated synchronized-stability assumption. The code independently reproduces the rational midpoint matrix, its trace \(6169/5000\), determinant \(144/625\), and negative \(\det(I-Q)=-17/5000\) using exact fractions. Synchronization instead gives principal multiplier \(24/25\).

# Known limits

The independent-crowding, stochastic, seasonally heterogeneous, delay-structured, and multi-stage cases are not proved. Complete text for Xie et al. (2014) was inaccessible, so the originality review does not claim a definitive exclusion of that source. No independent audit or external validation has been performed.
