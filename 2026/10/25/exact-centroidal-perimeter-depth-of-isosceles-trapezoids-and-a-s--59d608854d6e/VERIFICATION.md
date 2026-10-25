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

# Reproducibility and verification
The symbolic proof in `RESULT.md` gives all hypotheses and the exhaustive angle partition needed for infinitely many real parameter triples. The independent direct-intersection checker `trapezoid_depth_checker.py` is Python-3-standard-library-only and was executed from its actual packaged bytes. Its successful marker is `TRAPEZOID_DEPTH_OK shapes= 204 direct_rays= 367404 triangle_fraction=19/64`.

The checker tests a finite set of instances and directions and cannot establish the theorem independently. Every source-dependent premise needed for the trapezoid result is reconstructed in the proof; the cited source's triangle lower-bound assertion is not used as a premise. Independent audit has not been performed.
