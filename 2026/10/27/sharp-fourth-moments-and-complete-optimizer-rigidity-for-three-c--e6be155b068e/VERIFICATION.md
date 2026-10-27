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

# Verification of the sharp three-character fourth moment

Run `python3 check.py` in the directory containing this file. The calculation requires SymPy; `checks.txt` records the output of an actual local run. The checker independently constructs products of \(SU(2)\) characters in the representation ring and compares fourth moments with polynomial integration against semicircle measure. The latter uses the Catalan even moments of \(2\cos\theta\), rather than the same representation-ring formula.

The checker also performs parameter-symbolic comparisons of the rational elimination and derivative factorization, along with sample maximizer checks for weights \(0,1,2,3,4,5,10,50,100\). Finite sample testing is not a proof that these formulas hold at every integer weight. The universal claims rely on equations (1)--(3) of `RESULT.md`, positivity of the one-variable optimizer, and Descartes' rule of signs.

The novelty assessment cannot replace external expert bibliographic review. The finite-weight results were not independently audited.
