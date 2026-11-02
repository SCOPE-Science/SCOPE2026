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

# Verification and scope

Reproduce with `python3 verify_cycle_game.py` using Python 3 and its standard library. The script independently generates each colored placement with one empty vertex for \(m\) from 1 through 7, evaluates utility before and after every permitted unilateral jump, checks the run characterization, and compares observed welfare multiplicities with the explicit binomial formula. It also verifies the social optimum and prints the number of configurations examined at each size. All programmed assertions passed on the prepared source.

The checker verifies only the finite cases \(1\leq m\leq7\); no claim of machine certification for larger sizes or of independent external validation is made. The proof in RESULT.md provides the all-size theorem by characterizing deviations and counting finite compositions algebraically. The formally claimed domain starts at \(m\geq2\), avoiding the degenerate three-vertex edge overlap in the general welfare argument. Interpret numerical/finite output only as corroboration of the written proof.
