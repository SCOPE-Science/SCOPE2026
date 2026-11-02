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

The accompanying `verify.py` is a complete standalone Python 3 program. Running `python verify.py` gives 20,000 passing exact assertions. The checks enumerate all Prüfer codes for trees of sizes 2 through 8; every conditional binomial moment is checked for every feasible distance and moment order. Rational arithmetic independently checks the finite-difference identity up to size 200 and its positive-step consequence from distance two to three up to size 50. The proof of the infinite theorem is given in `RESULT.md`; these finite checks cannot replace it. No independent audit has been performed.
