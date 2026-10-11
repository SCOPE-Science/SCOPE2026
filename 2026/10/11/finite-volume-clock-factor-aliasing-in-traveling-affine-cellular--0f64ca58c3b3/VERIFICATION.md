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

## Checks performed
The identity for iterates and the spatial-cycle count were reconstructed for both signs of the shift and for all ring sizes. The finite-permutation factor criterion was proved in both directions, and the prime-adic implication was checked using the exact maximum identity. The infinite fixed configuration and rotation-invariance argument independently establish absence and full-coordinate necessity. These arguments establish the theorem at all parameters.

The embedded Python standard-library `verify.py` exhaustively checks all states and iterates through the permutation order for clock modulus 2 through 6, ring length 1 through 5, and the six signed shifts of absolute size at most three. It compares exact fixed-point counts and independent orbit decompositions to the formulas, and checks the normalized sum construction and full support where their hypotheses apply. It reports 59,926 finite assertions. Finite checks are diagnostics only, not an infinite proof.

## Reproduction
Run `python3 verify.py` from the extracted package directory. No external software or network access is needed.

## Limits
The result does not claim that finite rings factor onto the full spatial clock cellular automaton. Searches of published records cannot establish universal priority. There is no independent audit or external validation.

