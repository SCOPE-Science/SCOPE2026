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

# Reproduction and limits

With Python 3.10+ and the listed requirements, run `python3 verify.py`. The script checks exactly the derivative minimization and optimizer equation with SymPy. It then checks the explicit inverse-phase construction, negative radial derivative, and three scalar roots at contraction factors \(u=1/5,\,1/2,\,9/10\), as well as 27 illustrative phases below the threshold for each.

The proof in RESULT.md establishes the infinite, parameter-wide conclusions analytically; this finite numerical sampling alone does not prove uniqueness for arbitrary phase. The equality case \(|\eta|=E(u)\), stability, orbit counts beyond fixed points, and historical-priority certification are not claimed. Independent validation has not been performed.
