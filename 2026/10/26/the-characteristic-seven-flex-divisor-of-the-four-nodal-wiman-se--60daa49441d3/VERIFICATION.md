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

The standalone `verify_wiman7.py` ran and printed `VERIFY_OK`. Reproduce with `python verify_wiman7.py` in an environment containing SymPy. Its exact assertions cover the Hessian determinant/resultant identity modulo \(7\), special-fiber gcds, the cubic unique-root substitutions and irreducibility, norm-one squares in the cubic extension, the infinity chart, and the order-six tangent restriction.

Proof obligations checked analytically: étale pullback of simple intersections for nonzero \(X,Y\), ramified squaring at zero coordinates giving multiplicity four, ordinary node multiplicity six, and Bézout exhaustion of the full intersection length \(72\). The Hessian criterion is valid because \(7>6\). Independent external validation has not been performed. The exact upload date of the 2005 institutional preprint is not established from the inspected records.
