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

# Verification details

The finite checker `artifacts/check.py` reconstructs each avoidance histogram by exhaustive word enumeration and independently by the stated internal-gap generating construction for \(2\le A\le7\), \(0\le B\le7\), and \(1\le r\le B+2\). It asserts every coefficient and endpoint identity, direct palindrome symmetry, and the explicit two-\(a\) parity cutoff. It prints a deterministic transcript stored in `artifacts/check_output.txt`.

To reproduce: run `python3 artifacts/check.py`. No external packages, downloaded sources, or databases are required for this computation. The complete proof of the universal parameter claim is in `RESULT.md`; finite checks are not claimed as infinite certification. The mathematical literature comparisons are summarized in `REVIEW.md` and `AUDIT.json`. Independent scientific audit has not been performed.
