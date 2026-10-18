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

# Reproduction and limits

Execute the attached standard-library Python 3 program from a directory containing the file:

```sh
python3 verify_dense_chains.py
```

The program exhaustively enumerates all strong prefix-closed finite-chain relations through seven worlds by their incoming-column vectors, checks literal relational density independently of the algebraic criterion, and compares the two predicates on every vector. For each surviving dense frame it independently computes reflexive worlds, seriality, all upward-closed-event modal outputs, Stirling ranks and fixed-root fibre cardinalities.

Expected final line: `VERIFY_OK`. The full candidate populations at sizes one through seven are respectively 2, 6, 24, 120, 720, 5040, 40320; the density-admissible totals are respectively 2, 5, 15, 52, 203, 877, 4140. The exact proof for arbitrary sizes is given in RESULT.md, and no claim of infinite formal certification or independent external validation is made. The checks depend only on Python's standard library; no network fetch, external dataset or runtime-specific path is needed.
