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

# Verification

Run `python3 verify.py` after extracting all files in the same directory. The script needs only the Python standard library and produces a PASS line after all exact assertions succeed.

An actual run passed 20,321 integer assertions, of which 10,192 compared direct finite-permutation covariances against the theorem for all windows, patterns and inverse-descent indices at \(2\le n\le8\) and \(2\le k\le\min(n,5)\). Further checks cover distinct signatures and a length-three peak cancellation. These are consistency checks, not an exhaustive proof across all \(n\). The exact proof in `RESULT.md` supplies the all-size argument.

No independent audit or external certification has been performed.
