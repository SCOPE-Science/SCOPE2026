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

# Verification instructions and limits

Run with Python 3.9 or later (standard library only):

```sh
python3 exhaustive_prefix_dp.py
python3 square_block_bfs.py
```

`exhaustive_prefix_dp.py` generates every overlap-free binary word through length 48 by checking the newly appended suffix. For each word, an exact integer dynamic program counts the factorizations into each of zero through nine nonempty square blocks. The output reports 7,867 words including the empty word, 416 length-48 words, no shorter nine-square products, and exactly two length-48 products with one nine-square factorization apiece.

`square_block_bfs.py` uses a separate global overlap predicate and explores products of individually admissible square blocks. The root-length cutoff 16 is forced by the target length 48 and the eight other blocks of length at least two. It finds 74 admissible square blocks and precisely two depth-nine products, each with a single decomposition.

The supplied `prefix_dp_output.txt` and `block_bfs_output.txt` contain the actual recorded outputs, including the asserted witness strings and `PASS` checks. Computation is finite and exhaustive within the specified domain; neither program certifies statements about arbitrary lengths or supplants external scientific review.
