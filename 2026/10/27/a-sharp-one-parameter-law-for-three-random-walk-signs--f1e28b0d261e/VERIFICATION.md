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

The exact-rational verifier uses only Python standard-library functionality. It checks the polynomial integral yielding 19/90, the complete eight-word table against all 720 relative orders of six numbers, all 32 simple symmetric five-step walks, normalization and symmetry across six test parameter values, and the exact total variation 7/720. The program was run at the packaged source path. Its output was:

`PASS: triangular dominance 19/90; 720 permutation cases; 32 walk cases; TV 7/720; 6 family checks`

The continuum and strict endpoint assertions are proved analytically in the result; finite enumeration is not a proof of those quantified statements. One historical classical source had abstract-only access; no exhaustive literature exclusion or independent audit is claimed.
