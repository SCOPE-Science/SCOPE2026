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

The result for every dimension is derived from the spectral gap of the bipartite hypercube adjacency operator and the equality classification of a Boolean linear form of constant absolute value. The two finite checkers are supplementary; their output does not stand in place of the infinite proof.

Run `python verify_cubes.py` and `python verify_vertices.py` from the directory containing those files. The first checks dimensions 2–5 by exhaustive induced-matching enumeration through edge conflict masks. The second checks dimensions 2–4 by independently enumerating half-size vertex sets and testing that each selected vertex has exactly one neighbor in the selected set.

Expected census counts of maximum induced matchings for dimensions 2, 3, 4 and 5 are respectively 4, 6, 8 and 10. The scripts also assert equality between the computed matchings and all coordinate-parity templates rather than checking the counts alone. The machine output saved with this result documents executed checks. No verification beyond the finite ranges is attributed to those scripts, and no separate external audit has been performed.
