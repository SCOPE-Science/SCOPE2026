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

# Reproducibility and verification

Use `python3 check.py` (standard library only). It exhaustively lists the 5,282 augmented independent faces and checks the exact dimension counts. An acyclic matching with 2,638 nonempty pairs is certified by a global topological ordering of all 25,221 nonempty Hasse incidences. Its remaining CW cells are \(0,3,4,4,4\). The signed integral cochain recurrence is evaluated on all 1,554 original four-simplices, not merely selected faces, proving a zero three-to-four integral Morse boundary. A 16-term integral three-cycle has zero original simplicial boundary and unit pairing with the degree-three coefficient cochain. All 84 natural \(D_7\times S_3\) graph automorphisms, signed cycle actions and fixed-face Lefschetz traces are checked, producing the stated representations and zero invariant dimensions.

Expected terminal line: `VERIFIED`. `check_output.txt` is the exact reference output captured from the supplied program.

Scientific limits: this is an exhaustive finite 21-vertex calculation only, not a general symbolic theorem in cycle length or color count; no independent external verification or exhaustive worldwide literature guarantee is asserted.
