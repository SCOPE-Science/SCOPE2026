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
# Reproducibility and boundaries

The theorem is established by the explicit formulas and unbounded pebble strategies in `RESULT.md`; finite computation is supplemental. Two Python 3 standard-library programs were executed from their package paths.

`verify_pair_extensions.py` exhausts the two-variable atomic-extension patterns at each anchor for alphabet sizes 3 through 12, the two sharp low-width formulas for 1 through 12, and exact first- and second-coordinate equality interpretation for 1 through 8. It also checks small symbolic distinct-coordinate existential diagrams for widths 3 through 5. Expected stdout is stored in `verification_pair.txt`.

`verify_three_pebble.py` computes all initial three-variable atomic types and repeatedly refines each ordered triple by the sets of types obtainable by replacing any one of three pebbles. It stops at the full fixed point, which is unrestricted-depth three-variable equivalence. For alphabet sizes 1 through 7 the fixed point takes five refinement rounds and has respectively 1, 32, 122, 187, 202, 203, 203 realized triple colors; only alphabet sizes 6 and 7 share their color supports. Expected stdout is in `verification_three.txt`.

Re-run with `python3 verify_pair_extensions.py` followed by `python3 verify_three_pebble.py`. No network access or external packages are required. The scripts do not verify arbitrarily large alphabet sizes or all variable widths computationally; those infinite quantifiers rely on the formal game and definability arguments in the proof. No independent mathematical audit has been performed.
