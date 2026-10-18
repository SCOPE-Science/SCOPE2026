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

The all-order theorem is proved in RESULT.md by the valuation description of Zimin words, uniqueness of the largest symbol in every linear factor, and a Parikh-vector obstruction for off-center cyclic factors. These arguments cover every integer order \(n\ge1\), every circular start, and every admissible half-length (total length at most the circumference).

The complete standalone verifier is `verify.py` (Python 3 standard library). Run `python3 verify.py`. It constructs \(Z_n\) at levels one through eight, checks two independently implemented Abelian-square tests for every circular start and admissible half-length, directly scans every rotation for the exact predicted count, and directly searches all admissible circular Abelian cubes. It also confirms the ruler representation. A separate counterexample check confirms that palindrome and linear Abelian-squarefreeness alone do not imply the claimed circular uniqueness.

These finite checks do not prove the unrestricted claim; the written argument supplies the all-order proof. Unindexed prior literature remains a historical-priority risk. Independent scientific audit has not been performed.
