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

The packaged `artifacts/verify.py` is a standard-library exact verifier. It constructs the full ternary word space, derives forbidden triples directly from the descendant definition, and checks the 12-word witness.

For the upper bound it normalizes the first two selected codewords by the full coordinate/symbol automorphism group to four second-word Hamming-weight cases. Engine A performs a fixed-order exhaustive include/exclude traversal. Engine B uses a different branching order plus a safe partition of remaining candidates into classes that are pairwise incompatible relative to the current selected set. Both rule out a size-13 extension in every canonical case.

Run `python artifacts/verify.py`. The expected terminal line is `exact_M_4_2_3 12`; the preceding line `upper_bound_no_size_13 True` records the exhaustive upper-bound result.

Limits: this certificate proves only the finite parameter \(q=3\), length \(4\), coalition size \(2\). It does not certify a general formula in \(q\).
