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

# Reproducible finite verification

Run `python3 verify.py` using Python 3.8+ without optional dependencies. The program executes two exhaustive constructions of all 2,048 rooted de Bruijn cycles, two independent algorithms for linear complexity, and two independent algorithms for periodic sidelobe magnitude. It verifies the full 10-row by 6-column joint histogram, both marginals, the three four-element reversal/complement orbits for the 12 best-sidelobe cycles, and the eight cycles attaining both optimal invariants.

The exact required success line is:

`VERIFY_OK cycles=2048 joint_cells=32 optimal=8 best_orbits=3 independent_enumerations=2 independent_invariant_checks=2`

Exhaustiveness depends on the five-window successor-map bijection and independent Euler-tour equivalence proved in `RESULT.md`, not merely the smallness of the tested examples. The verification is finite and conditional on executing the supplied code correctly. No independent scientific audit has been performed; historical-priority caveats remain.
