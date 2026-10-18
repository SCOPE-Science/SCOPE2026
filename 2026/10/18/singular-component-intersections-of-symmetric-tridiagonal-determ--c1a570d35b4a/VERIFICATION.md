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

Execute `python checker.py` with Python 3 and SymPy installed. The script is standalone and requires no source papers or network downloads. It deterministically prints exact finite-field full-enumeration counts for orders three through five, checks each nonempty component-subset intersection for those sizes, samples orders six and seven over \(\mathbb F_5\) with fixed seed, factors the symbolic determinant through order six, verifies exact cut determinant identities, tests ordinary-node slices through order nine, and terminates with `VERIFY_OK` on success. The finite-field checks cover nonzero affine coefficient tuples (so each projective point appears by its nonzero scalar representatives); they verify finite instances and do not prove the general theorem. The exact identities underlying the general theorem are proved in `RESULT.md`.

The candidate classification describes the reduced singular support and intersections of reduced components. It does not assert that the Jacobian singular scheme is reduced, nor that its nongeneric analytic germ is nodal. No independent audit or external machine certification has been performed.
