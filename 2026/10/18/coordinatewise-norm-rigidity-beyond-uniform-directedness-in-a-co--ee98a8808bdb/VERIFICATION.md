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

# Verification scope

The proof in `RESULT.md` establishes the infinite-dimensional theorem by exact tail capture, a norming-anchor lemma, convergence of finite seminorms, the two-block directedness obstruction and explicit norm-one projections. No finite computation is used as an infinite proof.

The accompanying `verify_local_capture.py` is standalone and uses only the standard Python library. Execute `python verify_local_capture.py` in the directory containing the included artifacts. It verifies admissibility and weighted capture for 420 sampled finite pairs (95 with nonempty eligible tails), 250 finite block-window isometry checks, 24 finite dynamic-programming anchoring checks, and four representative directedness-separation parameters. The observed success marker is `LOCAL_CAPTURE_LACUNARY_BLOCK_FINITE_CHECKS_OK capture=95 block_tests=250 anchor_checks=24`.

Every bound required for the main theorem is justified symbolically in `RESULT.md`; the checker covers finitely many cases and does not test arbitrary sequences or all parameter values. No independent mathematical or bibliographic audit has been performed.
