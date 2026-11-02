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

# Verification instructions and limits

The complete proof is given in `RESULT.md`. Its two critical ingredients are (i) the ruler representation of letters at one-based positions and (ii) the fact that the aligned doubling map preserves and reflects the Lyndon suffix test. These ingredients are proved there and are not assumed from experiment.

To replay the finite checks, extract the embedded `checker.py` alongside this document and run `python checker.py` with Python 3. No external datasets or packages are needed. The checker performs full enumeration of contiguous factors and Lyndon comparisons for ranks 1 to 9, and additional cyclic-rotation tests for ranks 1 to 6. Output includes all checked rank counts. All tests passed at preparation. This is a finite regression check, not a certification of the unrestricted theorem.

The exact theorem applies only to rank-dependent finite Zimin words with their alphabet in increasing order. Published half Zimin Lyndon examples predate the theorem; historical-priority uncertainty about the full classification remains. Independent audit has not been performed.
