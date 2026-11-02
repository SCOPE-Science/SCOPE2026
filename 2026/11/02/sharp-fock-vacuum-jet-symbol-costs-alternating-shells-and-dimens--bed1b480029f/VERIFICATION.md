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
# Reproduction and verification

The attached `verification/check_vacuum_cost.py` uses Python 3 standard libraries, NumPy, and SciPy. Execute `python verification/check_vacuum_cost.py` from the extracted package directory. It reports 330 exact rational checks of binomial and Laguerre coefficient identities and 102 numerical checks of dual polynomial roots, signed Gamma moments, and bounds; 432 checks passed at packaging. The analytic proof in `RESULT.md` is necessary for all integers \(d,N\ge1\), global uniqueness, operator-theoretic dimension reduction, and smooth nonattainment. The program does not certify infinitely many indices or scan the literature. Recompute in a fresh environment if changing dependencies. No independent audit has been performed.
