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
# Verification of the six-symbol Ulam equality census

The supplied program `enumerate_lcs.cpp` computes the longest common subsequence of each relevant pair directly and exhaustively lists size-four codes containing the identity, rejects any extending fifth word, and calculates canonical equivalence classes. The separate program `enumerate_triples.py` represents each word by its exact 120-coordinate directed-triple incidence mask; it independently enumerates candidate cliques and canonical keys using those masks. The third program `verify_labeled.py` expands normalized codebooks under all 720 relabelings and deduplicates the resulting labeled four-word sets.

These programs were executed against their actual bundled source files and reported:

```
VERIFY_OK permutations=720 neighbors=132 normalized=298 labeled=53640 classes=57 no_five=1
INDEPENDENT_VERIFY_OK permutations=720 ordered_triples=120 admissible_neighbors=132 normalized=298 labeled=53640 classes=57
LABELED_VERIFY_OK codes= 53640 anchored= 298 symbols= 720
```

The independent method names in program output refer solely to distinct algorithms; no external or independent scientific audit was performed. Canonical representatives and orbit sizes are in `CLASS_REPRESENTATIVES.tsv` (57 rows, orbit sizes summing to 53640). The proof of pairwise distance four uses the Erdős–Szekeres theorem; the finite check alone is not presented as an all-length theorem. Claims of bibliographic priority remain subject to the limits described in `REVIEW.md`.
