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

# Reproducibility

Run `python3 verify.py` (Python 3, SymPy). A successful replay prints:

`VERIFY_OK transfer_states=10 exact_rational_identities=5 direct_supports=87380 direct_lengths=1..8 minimum_profile_lengths=1..44`

The verifier derives the ten state-orbit transfer, checks the exact two-variable rational function over a rational function field, derives the slack function and its first three exact coefficients, exhaustively tests all vertex subsets of the first eight ladders using graph adjacency independently of transfer, and checks 44 further positive lengths using an integer DP.

Finite checks are supplementary: the universally quantified claims rest on the local equivalence, symbolic identity, inequalities, constructions and coefficient extraction in RESULT.md. No independent external audit has been performed.
