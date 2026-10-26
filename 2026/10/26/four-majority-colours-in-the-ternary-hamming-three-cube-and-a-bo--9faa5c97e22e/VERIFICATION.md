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
# Verification

Run `python3 checker.py` from the directory containing this file. The script uses only the Python 3 standard library and constructs all Hamming edges independently by coordinate replacement.

Its checks are: all \(\sum_{j=1}^{5}\binom{27}{j}=101583\) nonempty vertex subsets of sizes one through five have induced minimum degree less than three; the four specified colour classes have sizes \(9,6,6,6\) and minimum induced degrees \(4,3,3,3\); lifted maps over the full vertex sets for dimensions \(3,5,7,9\) are surjective onto exactly \(4\cdot3^{(d-3)/2}\) colours, and each vertex has at least \(d\) monochromatic neighbours. The script prints `VERIFY_OK` on success.

The exhaustive finite subset check is not claimed to prove an infinite theorem. The dimension-independent construction is verified algebraically in RESULT.md, and the dimension-three upper bound is proved structurally. The status in front matter does not assert external validation.
