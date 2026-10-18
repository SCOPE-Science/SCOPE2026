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

Execute `python3 verify.py` using Python 3.9 or later. The included `verify_output.txt` records the program's expected standard output. The script uses only Python's standard library and a fixed seeded pseudorandom test.

The check enumerates all distinct uniform words on \(2\), \(3\), or \(4\) letters in eight specified small parameter combinations (\(4348\) words in total), checks the projection equivalence pair by pair, evaluates another \(2000\) four-letter triple-occurrence words, constructs and checks the \(C_5\) witness, and prints `ALL CHECKS PASS`. These tests were run and completed successfully. The proof for all alphabets and all \(k\ge1\) is the direct uniqueness argument in `RESULT.md`.

This verifies no claim of independent audit or historical priority. The resulting circle-graph multiplicity classification also depends on published theorems identifying the classical \(2\)-uniform class with circle graphs and the two-word \(1\)-uniform class with permutation graphs.
