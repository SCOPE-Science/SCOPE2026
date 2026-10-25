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

Run `python verify.py` with the accompanying `verify.py`, requiring Python 3 and no third-party packages. It enumerates all rooted labeled trees of sizes two through six with root label zero, totaling 1,441 Prüfer-coded trees. For each tree it exactly computes full final-size distributions with rational coefficients for constant transmissibility one-half and for a two-point transmissibility distribution with mass one-half each at one-quarter and three-quarters. Assertions test normalization, the shared exact mean, the lowest-common-ancestor variance increment, the sharp branching-index bound, and all stop-loss inequalities at integer thresholds. Three extra assertions verify the four-vertex center-rooted-star example. The program reports `PASS: 1441 rooted labeled trees, 15684 exact rational checks`.

The finite enumeration cannot prove the results for all rooted trees or arbitrary infectious-period laws; those rely on the analytic arguments in `RESULT.md`. This package contains no empirical estimate, no claim of computer-assisted infinite certification, and no independently performed scientific audit.
