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

The proof uses the explicit orthonormal monomial basis of standard complex Hardy space, exact gcd arithmetic, orthogonal chain decompositions, von Neumann's polynomial inequality, and Fredholm singular sequences. The accompanying `checker.py` runs using Python 3 standard library only and verifies 90,377 finite integer assertions across eleven monomial exponent pairs.

These diagnostics test coefficient actions and orbit partitions only; no finite computation certifies an infinite-dimensional spectrum. The infinite assertions rest on the proof in `RESULT.md`.
