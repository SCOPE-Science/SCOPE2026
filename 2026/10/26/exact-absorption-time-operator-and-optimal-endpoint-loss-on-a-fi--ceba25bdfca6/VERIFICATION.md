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

# Verification and scope

The dimensional proof in `RESULT.md` establishes strict stability of the effective generator and solves its Lyapunov equation explicitly. The numeric and rational finite checks below are supporting reproducibility tests, not an extension of the proof's quantifiers.

## Reproduction

Install the three dependencies listed in `requirements.txt`, then execute `python verify_path_lifetime.py` from the directory containing this file. The script overwrites `verification_report.json` with counts and maximum entrywise numerical differences. No external accounts, datasets or network access are required.

## Checks performed

The embedded `verification_report.json` records 7,475 symbolically exact Lyapunov matrix-entry checks for lengths from 2 to 16 and five positive rational loss values, plus 110 independent complex Lyapunov matrix solutions and 1,375 diagonal time comparisons for lengths 2 through 23. The observed largest absolute discrepancy between complete matrices was approximately \(3.35\times10^{-10}\). All displayed numerical loss values and the tested finite generators passed the associated stability comparisons.

## Scientific limits

Exact rational checks at finitely many sizes cannot establish the all-size theorem alone; the explicit symbolic cancellation and stability argument provide that proof. Numerical equality was assessed at tolerance \(2\times10^{-9}\), with the stated largest observed entrywise error. No independent audit, proof-assistant certification, priority certification, or experimental verification has been performed.
