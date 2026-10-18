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

The accompanying standalone `verify.py` uses Python standard-library exact rational arithmetic to check the two-period matrix identity, the characteristic polynomial discriminant, and the threshold witness via Sylvester's criterion for every interior rational test fraction on a grid. It also performs high-precision numerical checks of the switching direction for examples with migration survival below and above the exact threshold.

The universal claims for all real parameters do not follow from enumeration. They follow from diagonal similarity, Rayleigh's largest eigenvalue identity, strict Euclidean norm convexity, and the exact second-derivative formula in `RESULT.md`.

Scientific limits: fixed complementary period-two environment, constant migration survival, two patches, deterministic density-independent growth; no prediction of fixation, competition, or finite-population extinction. Independent audit has not been performed.
