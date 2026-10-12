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

The infinite theorem is proved symbolically in `RESULT.md`; finite computation is used only as a consistency check.

`verify.py` performs two independent finite checks. First, it enumerates every labeling in \(\{-1,1,2\}^{V(B_n)}\) for \(n=3,4,5\), evaluates the signed Roman definition directly from the graph neighborhoods, finds the minimum weight, and checks that every minimum labeling is captured by the stated classification. Second, it runs a page-state dynamic enumeration derived directly from the same neighborhood conditions for \(3\le n\le12\) and compares the exact number of minimum functions with the closed formula.

Replayed output:

`VERIFY_OK brute_n=3..5 labelings=597051 dp_n=3..12 minimum_functions_summed=5604`

The computation does not certify the statement for arbitrary \(n\); that role belongs to the exact proof. The cases \(n=1,2\) are intentionally outside the theorem.
