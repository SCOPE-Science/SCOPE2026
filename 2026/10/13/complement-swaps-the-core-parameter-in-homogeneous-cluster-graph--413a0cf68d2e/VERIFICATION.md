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
The proof is structural; the executable checker tests finite analogues without being used to extrapolate the infinite theorem.

Run:
`python artifacts/verify.py`

The checker:
- exhaustively enumerates all self-maps for \(mK_n\) and its complement at \((m,n)=(2,2),(2,3),(3,2)\);
- verifies that cluster-graph endomorphism image sizes are exactly \(n,2n,\ldots,mn\);
- verifies that complement endomorphism image sizes are exactly \(m,m+1,\ldots,mn\);
- constructs every permutation in the finite wreath product and checks that it preserves both the graph and its complement;
- brute-force counts injective ordered tuple orbits through arity \(4\) and compares them with the restricted set-partition count.

Observed output:
`VERIFY_OK 3717 exact assertions`

Limits: these finite computations are consistency checks only. The countably infinite image-cardinality and model-complete-core statements are proved in RESULT.md by direct structural arguments.
