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

Execute `python3 checker.py` using Python 3 with only the standard library. The script:

1. Generates every restricted-growth-string representation of a set partition of the labeled \(2n\) cells, for \(1\le n\le5\).
2. Computes every class product's structure constants directly from the rectangular-band multiplication, checking closure against constancy on every output class.
3. Checks that the accepted cases separate into predicted row-balanced and row-separated counts, and confirms the weighted-Bell enumeration independently.
4. Constructs permutations from the stated automorphism subgroup in every accepted case and verifies that their orbits coincide with the given classes.

Expected totals for \(n=1,2,3,4,5\) are respectively \(2,5,13,48,184\). The largest exhaustive stage traverses \(115975\) partitions of a ten-element set. All arithmetic is exact integer arithmetic; these finite checks support but do not replace the general proof.

The proof establishes an all-width structural classification, rather than an extrapolation from the exhaustive tests. The principal literature and scope limitations are stated in `RESULT.md`.
