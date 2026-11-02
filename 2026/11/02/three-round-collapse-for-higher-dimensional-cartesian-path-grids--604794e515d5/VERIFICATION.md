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

# Verification details

The graph products are built directly on coordinate tuples with edges changing exactly one coordinate by one. `check_profiles.py` computes ordered-pair atomic extension patterns for every first/second vertex and forms complete three-round graph types. It tests 123 parameter tuples with dimensions three to six and vertex counts up to 300, distinguishes the binary three-cube, independently evaluates the dominating-pair sentence, and confirms the smallest admissible nonexceptional product order is twelve. Run with `python3 check_profiles.py`; compare stdout with `profile_output.txt`.

`check_game.py` independently computes the nested rank-three tuple Hintikka types by exhaustive third-round atomic-diagram enumeration. It tests the seven-cycle against seven nonexceptional products and separates the exceptional cube. Run with `python3 check_game.py`; compare stdout with `game_output.txt`.

These checks are finite and do not establish the universal quantifiers. The infinite part is proved in `RESULT.md` by minimum degree, Manhattan-distance common-neighbour classification, strict product-size inequality, and a complete extension-pattern game argument. The exact independent audit channel remains unperformed.
