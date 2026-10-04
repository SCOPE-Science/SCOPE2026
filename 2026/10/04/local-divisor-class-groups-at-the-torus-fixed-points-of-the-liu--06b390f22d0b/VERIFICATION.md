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
The finite checker `artifacts/verify_lz_fixed_classgroups.py` was executed on the packaged source.

It verifies, for every \(2\le n\le8\), the published vertex count \(n(n+1)\), the lower-facet ray count \(n\), the upper-facet ray count \(n(n-1)\), the lower determinant \(\lvert\det(2J-I)\rvert=2n-1\), the exceptional upper determinant \(8\) when \(n=2\), and the explicit root-lattice difference identities used in the uniform \(n\ge3\) proof.

The recorded run ends with `VERIFY_OK`. These finite checks do not replace the uniform proof: the infinite statement follows from the sum-map lattice argument written in `RESULT.md`.
