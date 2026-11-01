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

# Verification details

The exact verifier `verify_icosidodeca_rips.py` is a standalone Python 3.9+ program using only the standard library. Its graph construction uses the canonical \(GP(10,2)\) edge families, then constructs their line graph and computes all-pairs shortest-path distances by breadth-first search. Its increasing-tuple recursion enumerates all cliques exactly once. It checks all **468** scale-two and **7940** scale-three elementary free face–coface pairs, including uniqueness and maximality when removed. Both reduced complexes are verified to be connected closed orientable simplicial surfaces of Euler characteristic two, with circular links at every vertex. The scale-two oriented generator is sent through the scale-three chain-collapse maps and matches the oriented scale-three generator with unit integer coefficient. The scale-four complement's fifteen antipodal pairs and the diameter-five terminal stage are also checked exhaustively.

Execute `python verify_icosidodeca_rips.py`. The supplied `verification_output.txt` is the exact output observed for the supplied source program. Successful execution ends with `VERIFIED_OK`. The integer transfer check is not replaced by a characteristic-two rank computation. These reproducible calculations are not independent external audit; no outside mathematical review was performed. Publication-priority and results for other graph metrics remain unverified.
