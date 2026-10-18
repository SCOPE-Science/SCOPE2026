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

# Verification of the normalization-hole theorem

The bundled Python standard-library `verify.py` reconstructs the exact twelve integer exponent vectors from the definition. It checks the unique missing lattice generator \(m=(1,1,1)\), that every sum of \(m\) and another degree-one lattice point equals a sum of two original generators, and that the chosen four central-octahedron tetrahedra and lattice difference basis each have determinant of absolute value one.

It enumerates semigroup sums and lattice points for every degree \(1\le d\le8\), verifying equality from degree two onward and the single deficiency in degree one. It verifies the Ehrhart expression and Hilbert numerator through degree eight. Successful execution prints `VERIFY_OK`.

These are finite independent checks. The all-degree and all-characteristic assertions require the human-readable proof in `RESULT.md`: unimodular triangulation, algebraic rewriting of all missing-generator factors, and the exact normalization sequence. The checker does not independently establish Hochster's theorem or verify the entire published literature; no independent audit has been performed.
