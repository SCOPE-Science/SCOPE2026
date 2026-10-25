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

# Exact reproducibility

Run `python verify.py` in a Python 3 environment with SymPy. The source is self-contained apart from SymPy. It constructs all 28 line vectors in \(\mathbb Q[t]^3\), checks the square-restriction identities for the bitangents, enumerates all 3276 unordered triple determinants, factors them in exact rational arithmetic, eliminates \(t\) by resultants to obtain the parameter polynomials, checks squarefreeness and pairwise disjointness, and reconstructs all intersection multiplicity counts from line pairs. The execution completed and returned `VERIFY_OK: 28 bitangents, 3276 triple determinants, 16 parameter strata, 27 smooth exceptional parameters`.

For each root of every irreducible smooth exceptional factor, the corresponding number of double, triple and quadruple incidence points is compared with the displayed theorem, including every conjugate lift in the parameter \(t\). The code does not use floating-point approximations and does not infer global conclusions from sampled fibers.

**Limits:** The geometric step that a smooth complex quartic has 28 bitangent lines is classical. The exact-arithmetic checker supplies a finite symbolic certificate for the determinant classification but is not a formal proof assistant and has not been independently validated. The work does not address characteristic two, odd positive characteristic, or singular fibers.
