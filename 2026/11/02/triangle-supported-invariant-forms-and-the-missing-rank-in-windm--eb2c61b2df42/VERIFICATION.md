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

The standalone Python 3 program `check_invariant_forms.py` uses only the standard library. Run it with `python3 check_invariant_forms.py` from a directory containing the extracted file.

The checker constructs ad-invariance linear equations from all ordered triples of basis generators for the empty four-vertex graph, three-vertex path, triangle, four-cycle, two-triangle windmill, and complete four-vertex graph over prime fields of size two and three. It compares their kernel dimensions with the graph-triangle formula, giving twelve checked instances.

It then directly enumerates every symmetric vertex matrix and every choice of triangle coefficients for \(F_1\) over fields with \(2,3,4\) elements and \(F_2\) over the binary field, computes the full matrix rank by finite-field elimination, and compares rank-by-rank counts against both the parameterization formula and independently implemented closed symmetric-matrix counts. Additional small-dimensional symmetric counts are checked against their orthogonal/symplectic-group expression. The extension field \(\mathbb F_4\) uses the irreducible polynomial \(x^2+x+1\).

Successful execution prints `TRIANGLE_INVARIANT_FORM_RANK_ENUMERATOR_OK 12 4`. The checks are finite corroboration: no infinite-rank or all-field result is inferred from them. The analytic proof is given in `RESULT.md`, including a characteristic-independent matrix reduction and exact standard finite-field symmetric-form enumeration.
