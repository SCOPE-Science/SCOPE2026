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

The finite proof certificate is `checker.py`. Run with `python3 checker.py`; it requires no external libraries and checks all 6,561 normalized ternary words, 78,125 integer potential choices with basepoint zero, their equality, the 13 symmetry orbits, and the facet/tight-edge distributions. Graph diameter two and the rank criterion mathematically guarantee that this finite list contains every possible facet.

The check makes no inference of novelty from successful arithmetic. Literature overlap and residual uncertainty are discussed in `REVIEW.md` and the accompanying structured assessment. Independent scientific audit has not been performed.
