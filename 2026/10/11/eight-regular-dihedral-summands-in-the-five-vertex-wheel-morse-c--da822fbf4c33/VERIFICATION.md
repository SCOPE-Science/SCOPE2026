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

# Reproduction and evidence

Run `python3 verify_wheel.py` from the extracted directory. Python 3 standard library suffices. It must terminate with `VERIFY_OK` and print a face vector, Hasse-cover count, matching/critical profile, five modular boundary-rank cross-checks, and the eight symmetry-specific signed simplex trace vectors. The expected key values are \((16,94,240,225)\) faces, \(1808\) Hasse covers, \(255\) matched pairs, one critical vertex and \(64\) critical three-cells, and boundary ranks \((15,79,161)\) over each of the primes \(2,3,5,7,101\).

The signed traces for the identity, quarter-turn, half-turn, two-rim-fixed reflection and no-rim-fixed reflection classes are respectively \((16,94,240,225)\), \((0,0,0,-1)\), \((0,-6,0,5)\), \((4,0,-12,-9)\), and \((0,-4,0,3)\). The program tests every automorphism, not merely a representative class, and verifies all nonidentity \(H_3\)-traces vanish. The acyclic matching certificate establishes the wedge homotopy type over the integers; modular ranks are supplemental consistency checks only. The Hopf trace/Lefschetz theorem transfers the signed chain traces to rational homology, and the regular-character identification is a standard semisimple representation argument.

The existing nonequivariant \(64\)-sphere result is prior work. This verification supports only the new equivariant rational module statement; it neither checks all wheels nor constructs an integral lattice decomposition.
