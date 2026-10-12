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

The theorem's complete proof is in `RESULT.md`. This package includes two independently structured corroborating programs with recorded outputs.

Run `g++ -std=c++17 -O2 verify_latin.cpp -o verify_latin && ./verify_latin > reproduced.txt 2> examples.txt`; compare the output with `verification_output.txt` and `verification_examples.txt`. The search fixes the first row via a column permutation and traverses all subsequent rows satisfying the Latin column condition and partial ascent excess at most two. It does **not** enumerate every unrestricted square of order six, only all squares potentially contributing to the required near-boundary coefficient.

Run `python3 verify_construction.py` and compare output with `construction_output.txt`; it constructs every divisor/residue-class witness with first row fixed to the identity for \(3\le n\le50\), verifying Latinness, ascent count, and distinctness. The count of labeled squares multiplies each identity-first-row witness by \(n!\), since first-row column permutations preserve the statistic and act freely.

The sources contain no randomness, external dependencies beyond a C++17 compiler and Python 3 standard library, or unprovided data. Finite computational checks cannot certify arbitrary orders. No independent audit has been performed.
