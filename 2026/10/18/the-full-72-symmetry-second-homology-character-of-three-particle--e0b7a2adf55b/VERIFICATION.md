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
Run `python3 verify.py` with standard Python 3.8 or newer. It regenerates the complete 3-particle discretized cubical model of the once-subdivided complete bipartite graph, checks disjointness and signed integral boundaries, verifies both boundary compositions are zero, obtains modular boundary ranks (454 mod 2, 946 mod 3, 432 mod 2), and enumerates all 72 automorphism actions on oriented cubes. It checks the complete nine-conjugacy-class table and evaluates all nine irreducible character inner products as exact rational numbers.

The finite modular rank calculations establish lower bounds on rational ranks; the proof supplies the necessary upper bounds from augmentation, column count and the four independent square loops with parked particles. No integral torsion classification is attempted. The cubical-model validity uses the Prue–Scrimshaw sufficient-subdivision theorem. The resulting exact rational homology character is a finite, reproducible computation, not a claim about configurations on other graphs. Independent scientific audit has not been performed.
