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

# Reproduction and checks

Execute `python3 checker.py` from the directory containing the supplied standalone script. It needs only the Python 3 standard library. The formula implementation enumerates subsets, extracts maximal selected runs, and multiplies integer-polynomial factors. A structurally separate direct implementation enumerates all permutations of each selected domain, retaining only square-identity maps preserving induced fence order. Their complete fixed-point/two-cycle coefficient dictionaries agree for each size \(1\le n\le8\).

The script also checks the rank-two coefficient \((n-1)^2\), the three parity cases for rank \(n-1\), the full-rank count, and the total rank profiles through \(n=12\). Successful output includes `VERIFY_OK`. These are exact finite computations; the proof of the infinite formula is the run-decomposition and wreath-involution argument in `RESULT.md`. The existence of an unindexed equivalent result in earlier literature is not computationally decidable from these tests. Independent audit has not been performed.
