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

# Reproducible verification

Run `python3 verify_antipodal_rips.py` using Python 3.9 or later and the standard library only. Compare the printed dictionaries with `verified_output.txt`. All simplex lists, complement-orbit identifications, signed integral boundary maps, binary elimination and Alexander–Whitney products are regenerated from the metric definitions. No external files, tables, graph packages or prior results are consulted by the checker.

The verification for \(n=4\) finds \(392\) cover simplices, quotient cell vector \((8,40,80,60,8)\), boundary ranks \((7,32,47,8)\) and mod-two Betti vector \((1,1,1,5,0)\). The verification for \(n=5\) finds \(1776\) cover simplices, quotient cell vector \((16,120,320,320,96,16)\), boundary ranks \((15,104,215,80,16)\) and mod-two Betti vector \((1,1,1,25,0,0)\). For both, every applicable consecutive integral boundary product vanishes exactly. The covering class is verified to be a nontrivial one-cocycle. Its square and cube are independently evaluated and shown nonboundaries by rank augmentation (all four increases equal one).

The sphere-wedge theorem for the covering complex is an external established mathematical premise, not reproved by the standalone checker. The free-action covering argument, transfer, UCT and low-degree cohomology ring deductions are mathematical proof steps rather than raw program outputs. The finite checker is exhaustive only for \(n=4,5\); no general-dimensional proof or external independent audit is asserted.
