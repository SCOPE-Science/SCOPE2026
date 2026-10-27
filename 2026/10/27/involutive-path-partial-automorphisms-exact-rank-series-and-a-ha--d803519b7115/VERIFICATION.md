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

The direct checker is `check_path_involutions.py`. Run `python3 check_path_involutions.py` in a directory containing that file; only the Python standard library is required. It independently enumerates all partial permutations of each vertex subset of the paths on one through nine vertices. It rejects maps unless the permutation squares to the identity and preserves every edge and non-edge of the induced graph, then compares each rank count with the interval-run formula. The input is generated deterministically; there are no precomputed answer tables. The checker prints a single success line and the rank profiles if all tests pass.

The finite range \(1\le n\le9\) examines \(1{,}112{,}082\) raw candidates in total and verifies \(9\) complete rank polynomials. It does not verify the general asymptotic bound experimentally; that bound is established in the mathematical proof. As an independent presentation of the exact formula, it implements coefficient convolutions rather than the permutations used on the direct side. The ordinary graph path definition, not a metric-isometry interpretation, is used throughout.
