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

# Verification of exact finite-model witness formulas

Execute `python checker.py` using Python 3 with only the standard library. The program directly tests every nonempty relation between each ordered pair of all one-agent models with one to three labelled worlds and one Boolean atom, and four further chosen pairs with four and three worlds. For each relation it independently checks atomic agreement, every forth and back obligation, global projection, and inclusion-minimality under proper subset inclusion. It compares the resulting four counts with independently computed formulas using bipartite inclusion-exclusion, a minimal-cover star recurrence, and explicit compatible-component edge-cover subsets.

The completed execution produced `ALL_CHECKS_OK model_pairs=2504 profile_cases=5`. The five coefficient cases are the complete bipartite sizes \((1,1)\), \((2,2)\), \((2,3)\), \((3,3)\), \((4,4)\). Separate hand-checkable examples give \((15,4,7,2)\) for two singleton classes on each side, and \((7,2,7,2)\) for one two-world class on each side, with identical atomic colors throughout.

The proof of the unrestricted theorem is the class-pair normal-form bijection and the two-level minimality argument in `RESULT.md`. Finite experimentation is not a proof of the all-size statements. No formal proof assistant or independent audit has been used. The method counts fixed labelled one-agent S5 models with a common finite propositional vocabulary; it does not count multiagent frames, automorphism orbits, or modal-depth-bounded simulations.
