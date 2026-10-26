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

# Verification record

The included `verify.py` uses only the Python standard library. Run `python verify.py` from the folder containing that file. It directly checks whether every candidate factor has least period \(p\), factor length at least \(2p\), and cannot be extended on either side while retaining period \(p\). Its output is `VERIFY_OK full_run_sets 1330 ...` on success.

All 1,330 words with exactly two ones and at most eighteen zeros were covered, with **equality of full run sets**, not only total counts. For each of the resulting nineteen zero-count levels it checked the bivariate formal-series coefficients at five integer specializations of \(u\). It independently compared two formulas for the four-run count through length \(149\), and checked the extremal maximum for lengths \(2\) through \(19\).

These are bounded computational checks. The claims for all nonnegative zero gaps and the limiting density are established by the four mathematical proof steps in `RESULT.md`. No external or independent mathematical validation is asserted.
