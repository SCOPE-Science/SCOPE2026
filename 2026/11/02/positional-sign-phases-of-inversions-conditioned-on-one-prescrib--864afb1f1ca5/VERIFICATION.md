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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 (standard library only). The program checks, using exact integer/fraction arithmetic, every prescribed two-cycle conditional mean for all permutations up to size eight, reconstructs the same means by a separate pairwise-expectation calculation, checks the global cancellation identity through size 150, and tests exact sign proportions at four further sizes. Output from the recorded execution: `PASS 405 independent exact and sign checks`.

The script only inspects finite cases. The infinite family of equalities and asymptotics are proved in `RESULT.md`; the script is not an independent audit or an exhaustive infinite proof. The main remaining uncertainty is historical priority of the local conditional formula, not a missing finite computation.
