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

# Verification record

Run `python verify.py` with Python 3, SymPy and SciPy. The checker evaluates exact symbolic incidence, affine slack inequalities on all integer parameters \(h\geq2\), the complete eighteen-edge table, lattice-index and class-group determinant identities, saturated rank-two bases for the \(A_3\) transverse model, and both edge lengths. It additionally checks convex hulls for six representative values; these sample hull checks are corroboration only.

The expected result is `VERIFY_OK: symbolic ten-cone and eighteen-edge fan certificate`. The primary geometric proof of the all-parameter claim is contained in `RESULT.md`; the checker certifies its finite symbolic reductions, not an independent proof of the cited source's very ampleness or hole enumeration.

The scheme-theoretic Jacobian singular structure, local equations at the nonsimplicial endpoints and the parameter \(h=1\) are not verified or claimed. No independent audit has been performed.
