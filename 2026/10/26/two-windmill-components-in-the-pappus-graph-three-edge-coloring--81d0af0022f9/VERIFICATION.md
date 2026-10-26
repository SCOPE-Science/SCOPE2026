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

# Reproduction

Run `python3 verify_matchings.py --certificate` followed by `python3 verify_colorings.py` from one directory containing the two scripts. Neither uses third-party Python libraries. The first independently enumerates forty-two perfect matchings and twenty edge-factorizations, constructs the thirty-six exchange edges and writes the complete certificate; the second enumerates colorings via direct edge-constraint backtracking and separately builds the same exchange graph. Compare the new certificate bytes against `classification_certificate.json` and both printed `full_graph_sha256` values against `56ffa0b44d5b539ae41cc4056f5b6ca8821b12eaae1cad70608a02a36680ada6`. Stored replay outputs are `matching_run.txt` and `coloring_run.txt`.

The finite exhaustive checks cover the **specified Pappus graph** and precisely the quoted global-color-permutation quotient. They do not independently audit external publication priority, establish extension to any other graph, or attest to an independent external review.
