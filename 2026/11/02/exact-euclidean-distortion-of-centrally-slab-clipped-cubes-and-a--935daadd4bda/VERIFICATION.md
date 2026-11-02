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

The mathematical proof in `RESULT.md` covers every integer \(n\ge2\), real \(t\ge1\), and every invertible real linear map to Hilbert space. It requires no external certificate. The upper and lower bounds coincide because the permutation average of every arbitrary quadratic sandwich is again a valid sandwich and the one-parameter objective is minimized exactly at its dual-branch crossing.

The bundled script `artifacts/verify_slab.py` is standalone Python 3 standard-library code; running `python3 artifacts/verify_slab.py` from the extracted package root produced:

```
CHECK_OK exact_parameter_cases= 72 exact_assertions= 8530 vertex_sets_explicit=yes parity_monotonicity=yes
```

It enumerates vertex-orbit representatives for the selected small dimensions (the free coordinate is fixed by symmetry), computes the proposed Hilbert form and its ratios in exact fractions, compares nearby invariant forms, and verifies several parity-monotonicity evaluations. The finite range is only a transcription and stress check, not a replacement for the algebraic proof over the infinite parameter domain.

The originality comparison distinguishes the signed coordinate sum from an absolute coordinate sum, and compares relevant primary full-text definitions to the exact claimed object. No exhaustive historical novelty certification is possible. There has been no independent mathematical audit.
