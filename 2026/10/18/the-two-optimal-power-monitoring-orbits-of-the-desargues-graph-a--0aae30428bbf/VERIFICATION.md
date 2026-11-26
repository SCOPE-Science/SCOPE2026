---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks

In `RESULT.md`, the two displayed propagation traces can be checked using only the 20 masks of weights two and three. Initialize with the seed and all masks at Hamming distance one from its members. For each later round, add all singleton unobserved-neighbor sets of the previously observed masks. To verify the local slide counts, list the nine exchanged pairs at each representative; test the resulting triples against the two allowed minimum-set profiles using Hamming distances. Permutations and complementation carry the two representative calculations to their respective orbits. No claim is made about distances inside the deadline-restricted graph.

The minimum-set census, orbit partition and full-graph metrics used as baseline results are identified in reference [1] in `RESULT.md`. The bundled standard-library programs `desargues_pd_verify.py` and `desargues_pd_independent.py` also reproduce those results with Python 3.10 or newer. Their outputs are included in the corresponding text files. The slide class counts in `desargues_pd_verify.txt` are consistent with the local slide-choice proof.
