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

# Verification instructions

Run `python3 verify.py` in the package directory with Python 3 and its standard library. The code reconstructs the triangular-prism graph, all 18 primitive vertex-edge matchings, both independent descriptions of its 1,728 simplices including the empty simplex, the complete 831-pair acyclic matching of the nonempty face poset, and the full twelve-element action on the resulting simplicial complex.

The deterministic pivot order is `1,9,2,13,14,8,16,17,15,12,4,0,3,7,10,5,6,11`. The checker visits every one of 1,727 nonempty faces and verifies acyclicity across 6,606 Hasse incidences. It computes the class traces \((64,0,1,-4,-8,-1)\), verifies the six irreducible multiplicities \((3,7,10,8,4,11)\), checks total representation dimension \(64\), and finds three full-symmetry invariant rational classes.

Success is signaled by `TRIANGULAR_PRISM_MORSE_64S4_FULL12_CHARACTER_OK`. Exhaustive finite verification plus Forman's discrete Morse theorem and ordinary character theory prove the stated finite graph result. The program does not independently certify the cited literature's global completeness, identify an integral group-representation lattice, or provide external mathematical auditing.
