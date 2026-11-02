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

# Computational reproducibility

Execute `python3 verify_duad_syntheme.py` and `python3 verify_symplectic_cliques.py` from the extracted artifact directory; both use Python standard library only. Both programs were run successfully against the package content. The first exhaustively checks all \(\binom{15}{9}=5005\) candidate nine-duad graphs and counts their perfect matchings; the second independently builds the symplectic model and enumerates all 8,950 maximal induced matchings via exact clique search. Both independently verify the ten nine-edge maxima, pairwise one-edge intersections, and the incidence multiplicity two for each flag.

Finite programs verify the particular thirty-vertex graph, and provide no general theorem about arbitrary cubic cages. The formal mathematical proof of the exact classification is given in RESULT.md; no independent external audit has been performed.
