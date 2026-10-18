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

# Exact finite verification

Run `python3 verify.py` with Python 3 and sufficient RAM. Only the Python standard library is used. Optional command-line integers restrict verification to specific cases (for example `python3 verify.py 6 7`). The full run defaults to 6, 7, 8, 9, 10.

For each case the program enumerates every subset of each closed-neighborhood generating facet, including the empty face; builds the ordered-coordinate matching on the complete augmented face set; asserts pair coverage and exact critical cardinalities; computes the directed V-path graph on all paired lower faces and verifies it is acyclic by a complete topological sort; and evaluates every oriented integer Morse differential from critical dimension four to three using exact unit-pivot substitutions. This is a full finite proof certificate, not a homology inference from timeouts or sampled faces.

Verified outputs:

| Base size | All augmented faces | Matched pairs | Critical 3-cells | Critical 4-cells | Integer differential |
|---:|---:|---:|---:|---:|---|
| 6 | 5,142 | 2,561 | 5 | 15 | exactly zero |
| 7 | 34,308 | 17,129 | 15 | 35 | exactly zero |
| 8 | 202,141 | 101,018 | 35 | 70 | exactly zero |
| 9 | 1,099,624 | 549,714 | 70 | 126 | exactly zero |
| 10 | 5,673,836 | 2,836,750 | 126 | 210 | exactly zero |

The proof of acyclic ordered-coordinate matching also appears independently in Goyal–Shukla–Singh, arXiv:1905.06926, Proposition 3.1. The reduction from Čech nerves to closed neighborhoods comes from Adams–Shukla–Singh, arXiv:2212.05871, Lemma 2.2. The suspension consequence uses Matsushita, arXiv:2511.12608, Theorem 1.2.

These are exact finite checks for the five stated instances, not a validation of the same pattern for any larger base size. No independent audit or external certification is asserted.
