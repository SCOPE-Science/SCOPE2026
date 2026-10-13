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

The standalone `branch_strata_verify.py` was run using SymPy and returned `BRANCH_COLLISION_EXACT_OK`. It checks exact polynomial equations over \(\mathbb Q\): Jacobian determinant; equality \(S^3-T^2=1024Q\); quartic discriminant; restriction of \(Q\) to \(B=0\); factorizations on both intersection curves; the triple-root derivative condition on the cusp line; and specializations at \(u=0\).

The proof independently explains finite flatness, radical branch support, irreducibility and singular lines, the exhaustive fibre partition, and intersection multiplicity at generic points. No numerical finite sampling is used to infer the geometric theorem. The embedded script does not check a full singular scheme or any property of the Bernstein–Sato ideal.
