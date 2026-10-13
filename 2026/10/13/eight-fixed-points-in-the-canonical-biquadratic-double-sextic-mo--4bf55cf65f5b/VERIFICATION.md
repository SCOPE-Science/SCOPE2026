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

The proof uses the published canonical equation and its stated geometric properties as premises. The bundled script checks the algebraic local consequences for every \(n\in\{1,\ldots,8\}\): preservation and order two of \((U,V,z)\mapsto(V,U,-z)\) on \(UV=z^{2n+2}\), reversal of the \(A_{2n+1}\) exceptional chain, uniqueness of its central component, two simple fixed values of the induced central Möbius involution, and the final count \(6+2=8\).

Run:

`python3 artifacts/verify.py`

Expected final line:

`VERIFY_OK n=1..8 smooth=6 exceptional=2 total=8`

The script does not re-prove the source's classification of canonical double-sextic models or the published \(A_{2n+1}\) branch-singularity statement. Those are cited premises. The local normal-form argument in RESULT.md explains why the source's even plane-curve germ may be chosen equivariantly.
