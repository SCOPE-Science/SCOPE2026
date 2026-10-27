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

# Reproducibility record

A C99 compiler and Python 3 standard library suffice. In the directory containing these files:

```sh
cc -O2 -std=c99 -Wall -Wextra census.c -o census
./census extremizers.tsv
python3 check_orbit.py extremizers.tsv
```

Both commands were executed on these package sources. `run_output.txt` records their exact observed output; the supplied `extremizers.tsv` has one heading and 48 exact rows. The C program uses two passes through all 9,691,375 unordered four-element supports, computes four integer \(3\times3\) minors per support, and counts positive primitive circuits. The Python script recomputes each accepted relation via a separately written determinant routine, checks row uniqueness and positive primitive length 79, then establishes exact equality with the orbit under all 48 signed coordinate permutations.

Exhaustive finite computation is part of a complete proof because of the primitive-kernel and rank-reduction lemmas in `RESULT.md`. The result does not assert an unproved all-radii theorem or independent validation.
