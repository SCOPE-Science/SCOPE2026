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
# Reproducibility and limits

Execute `python3 verify.py` from the directory containing the extracted files. No third-party modules or datasets are required.

The checker performs an independent finite factorization search in dimensions two and three, not just a graph comparison. It checks rank-preservation via all possible subsets of alphabet letters and tests every nontrivial pair of elementary word morphisms whose composition has generator-image length two. It also enumerates every set of distinct oriented edges on four or five vertices, independently checks the induced edge-count inequalities and the spanning-cycle strict inequalities, and checks the labelled unicyclic exponential formula via a separate cycle-plus-rooted-forest recurrence.

Expected end marker: `VERIFY_OK`. Computations are finite corroboration and are not a proof for all alphabet sizes. The arbitrary-size conclusion follows from the mathematical proof in RESULT.md. Independent audit: not performed.
