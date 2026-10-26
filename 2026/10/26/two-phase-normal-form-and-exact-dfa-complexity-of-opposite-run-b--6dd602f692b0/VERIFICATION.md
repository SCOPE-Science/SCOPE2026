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

# Reproducible finite checks

Execute `python3 verify_opposite_shuffles.py` using Python 3.9 or newer. No third-party libraries are needed.

The checker independently enumerates the distinct shuffle language, composition-language candidates, and every non-dead right-language quotient for the 256 quadruples with parameters between 1 and 4. It then constructs the original nondeterministic interleaving grid, determinizes the subsets reached, and identifies equivalent DFA states through accepted-suffix signatures for 4096 quadruples with parameters between 1 and 8. The expected output is:

`VERIFY_OK explicit_languages_and_residuals=256 independent_grid_DFAs=4096`

The two constructions do not rely on the formula to generate their languages or reachable states; the formula is used solely for assertions. Finite runs cannot verify the all-integer statement or establish novelty. The separate mathematical argument in `RESULT.md` provides the infinite proof.
