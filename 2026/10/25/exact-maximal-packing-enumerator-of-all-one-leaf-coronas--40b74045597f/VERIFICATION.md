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

# Reproducible computational checks

Run `python verify.py` with Python 3.9 or later, in the same directory as the supplied script. The expected terminal log is provided verbatim in `verify_output.txt` and ends in `VERIFY_OK`.

The script uses all labelled graphs on one through five vertices and seeded pseudorandom edge masks for another 120 six-vertex and 30 seven-vertex graphs. It constructs each corona, computes graph distances, enumerates all vertex subsets, tests the closed-neighborhood packing criterion, and independently tests maximality by trying to adjoin every omitted vertex. It then compares the exact family of maximal vertex sets with the candidate sets constructed from all base packings; comparison is set equality, not just coefficient equality. The script also checks the complete-graph corollary for orders two through six.

Actual recorded output: 1,249 graph instances tested; 10,647 maximal packing sets agreed with the bijection. The complete-graph polynomial checks passed for all five orders from two through six, displayed individually in the log. The final machine status is `VERIFY_OK`.

Only finite graphs were computationally enumerated. The universal bijection, degree-weight polynomial, regular-base support, and cyclic enumeration are justified by the mathematical proof in `RESULT.md`; they are not extrapolated from the computations. No third-party or independent mathematical audit has been performed.
