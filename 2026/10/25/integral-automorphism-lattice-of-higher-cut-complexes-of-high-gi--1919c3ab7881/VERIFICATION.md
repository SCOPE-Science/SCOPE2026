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

Run `python verify_cut.py` with Python 3. The verifier constructs cut-complex faces from disconnected induced \(k\)-subsets, computes simplicial Lefschetz traces with exact orientation signs, computes exact mod-two boundary ranks, and detects a private face in every connected \(k\)-set in selected finite graphs. No external libraries or precomputed tables are needed.

Observed completion markers in the package environment:

```
SIGNED_LEFSCHETZ_COMPARISONS_OK 81
MOD2_HOMOLOGY_CHECKS_OK 7
CUT_COMPLEX_CHARACTER_CERTIFICATE_VERIFIED
PRIVATE_FACET_UNIMODULAR_SATURATION_OK 15 446
```

These tests are finite and do not prove the theorem for arbitrary graphs. The proof in `RESULT.md` supplies the universal topological argument. In particular, the **integral** claim rests on the private-face minor and the integral Alexander duality construction, not on mod-two computations or character traces. The current mathematical review is not an independent audit.
