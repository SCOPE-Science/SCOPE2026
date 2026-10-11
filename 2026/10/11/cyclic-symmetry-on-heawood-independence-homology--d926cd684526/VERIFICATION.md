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

Run `python3 verify.py` with a standard Python 3 interpreter. The program uses only the standard library and reconstructs every object from the Fano-plane incidence rule.

The exhaustive checks are: 14 vertices and 21 edges with degree 3 at every vertex; preservation of all edges by the order-seven rotation; all 457 nonempty independent sets; face vector \((14,70,154,147,56,14,2)\); all 1568 Hasse covers; a 225-pair acyclic matching with critical vector \((c_0,c_3)=(1,6)\); signed chain traces for all seven group elements; Lefschetz vector \((-5,2,2,2,2,2,2)\); and degree-three character \((6,-1,-1,-1,-1,-1,-1)\).

A successful replay ends with `VERIFY_OK`. The verifier is exhaustive for this finite complex; it does not claim a computation for the full automorphism group or for integral representation structure.
