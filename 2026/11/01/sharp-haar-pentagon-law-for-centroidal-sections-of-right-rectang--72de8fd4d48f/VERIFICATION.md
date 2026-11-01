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

# Verifiable calculations and analytic scope

The exact formula is derived in `RESULT.md` by counting face-edge crossings of a central plane, converting the pentagonal event to a trivariate Gaussian orthant, and using a proved Gaussian sign identity. The global optimizer follows from strict pairwise smoothing of the normalized positive shape parameters; no finite test is used to assert an infinite claim.

Run `python3 verify.py` with Python 3 and its standard library only. The verifier independently counts section-edge crossings directly from randomly oriented planes for seven explicit positive shape triples, using 120,000 Gaussian normal vectors per triple (840,000 total); the largest observed difference between sampled frequencies and the theorem's predictions is about 0.00262851. It checks a separate spherical-triangle formula and global upper bound on 4,000 additional predetermined random triples and tests nonmaximal nearby shapes. Exact identities in the proof are not computer-certified by the samples, and no independent mathematical audit has been performed.

Known scope restrictions: the section plane always passes through the volume centroid; pyramids are right with rectangular bases; orientations are Haar-uniform; all side lengths and heights are strictly positive. The square optimal value coincides with a previously published orthogonal-projection constant; novelty assessment concerns the full section law, not that scalar alone.
