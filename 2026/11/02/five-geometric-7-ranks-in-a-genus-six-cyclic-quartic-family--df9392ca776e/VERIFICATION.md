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

# Reproducibility and limits

From this directory, run `python3 verify_symbolic.py` (requires SymPy) and `python3 verify_fields.py` (Python standard library). The symbolic program checks the exact required coefficient identities, rank-block determinant, and restricted quintic discriminant. The field program builds the six-dimensional Cartier operator by independent polynomial multiplication and iterates the semilinear map for eleven steps, checking its stable rank against the claimed formula. It exhausts all \(343\) triples over \(\mathbb F_7\) and checks \(3500\) deterministic triples over \(\mathbb F_{49}\) represented using \(i^2=-1\). Two explicit rank-one witnesses are checked over the extension field.

Expected final status lines: `GENUS6_CHAR7_SYMBOLIC_CARTIER_AND_RANK_ONE_GEOMETRY_OK` and `DIRECT_GF7_GF49_SEMILINEAR_CARTIER_STRATIFICATION_OK`.

The rank-one curve parametrization, irreducibility, and scope over the full algebraic closure are established by the proof, not the finite enumeration. No Newton-polygon, isomorphism-class, or external independent-audit claim is made.
