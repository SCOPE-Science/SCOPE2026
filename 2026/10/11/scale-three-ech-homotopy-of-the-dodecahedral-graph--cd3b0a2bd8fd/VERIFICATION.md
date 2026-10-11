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

# Reproducing the calculation

Execute `python3 verify.py` using Python 3 and its standard library; no other files or network access are needed. The script prints `VERIFY_OK` only after all required assertions pass. It deterministically constructs the 20-vertex dodecahedral graph, generates all 30 closed-neighborhood-union facets, enumerates the entire face poset (1,170 nonempty faces), and matches 578 face pairs. It checks every one of the 4,160 Hasse incidences and topologically sorts the full oriented diagram to prove the matching acyclic. Exact signed integer gradient elimination verifies all twelve critical dimension-three to dimension-two Morse coefficients are zero. Separately, modular simplicial boundary reduction over primes 2 and 3 verifies ranks 19, 131, 248, 150, 30 and reduced Betti sequence 0, 0, 1, 12, 0, 0. The alternating face sum is -10.

The script is a complete finite certificate for this exact complex. It does not establish unproved generalizations, exhaust literature, or independently substitute for the cited combinatorial Čech facet lemma, standard discrete Morse theorem, or the degree classification of maps into the 2-sphere.
