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

Running `python verify.py` in the extracted package requires only Python's standard library and the supplied `classification.csv`. The program enumerates all 8192 possible radius-two rules on the 13 legal five-blocks and exhaustively checks their 21 preservation constraints. For each of the 229 surviving rules it closes the finite subset predecessor automaton and returns either an exhaustive no-omission certificate or the shortest omitted legal word.

The executable checks the exact distribution of obstruction lengths, the unique mask `4132`, the 11 surjective rules, the five coordinate shifts, all six periodic collisions establishing noninjectivity, and the radius-one baseline. Independently of the subset closure, it directly generates all 196418 valid input words of length 25 and verifies the exact two excluded 21-blocks for the extremal mask.

Scope limits: these checks prove only the finite-state statements formulated in the accompanying proof. Completeness at every output length follows from the fully explored finite subset graph, not from extrapolating the direct 21-block enumeration. No independent human audit or external certification has been performed.
