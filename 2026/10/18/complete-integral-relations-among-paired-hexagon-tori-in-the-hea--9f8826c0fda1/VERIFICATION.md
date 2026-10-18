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

# Reproducible exact verification

Run `python3 verify.py` with the exact versions listed in `requirements.txt` (NumPy 2.3.5 and SymPy 1.14.0). The script takes no arguments and does not read any external data files.

The checker constructs the seven Fano lines \(\{i,i+1,i+3\}\), all twenty-one incidence edges, all simple cycles, and the two-particle Abrams cubical cells. It builds the signed square boundary matrix and all product-torus cycles, then checks their boundaries are zero. The chain matrix has an explicit unit \(14\)-minor (row and column coordinates stated in RESULT.md); the boundary has rank \(154\) modulo \(3\). These jointly establish the complete integral degree-two cycle lattice, not just an experimental lower bound.

The checker constructs the twenty-eight local three-term relations. Its explicit \(28\)-minor has determinant \(-2\), and the relation matrix has rank \(27\) modulo \(2\), certifying index exactly two in the saturation. It verifies coordinatewise divisibility by two of the sum of all local relations, that the half-sum is a chain relation with eleven positive and eleven negative unit entries, and the full graph-automorphism orbit count.

Expected final marker: `VERIFY_OK_HEAWOOD_COMPLETE_TORUS_RELATIONS`. This is a self-contained, finite exact computation. The underlying Abrams deformation-retraction theorem is the cited topological input; the code does not constitute an independent mathematical audit or verify priority against inaccessible publications.
