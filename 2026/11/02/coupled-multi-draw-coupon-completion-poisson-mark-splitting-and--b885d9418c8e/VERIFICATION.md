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

# Reproducible verification

Run `python verify_multidraw_joint.py` using Python 3 standard library only. The standalone script asserts exact count-kernel probabilities against enumerated labeled masks, exact rational marked-factorial-moment identities, an exact two-offer equality-of-completion identity, and numerical convergence of finite-population coupled probabilities to the derived critical CDF. The output saved in `verification_output.txt` was reproduced from the embedded code during packaging.

The finite checks do not imply an infinite-size limit. The analytical proof in RESULT.md supplies the geometric holding-time bounds, tagged identity, factorial-moment limit and marked process argument. The source publication date and model are checked against arXiv:2607.01463. The proof does not provide convergence rates for growing group size.
