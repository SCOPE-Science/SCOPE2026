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

# Reproduction and scientific limits

Run `python3 verify.py` from this directory using Python 3 (standard library only). The packaged script was run successfully and reported:

`PASS: exact rational ranks (6,9,10), 720 angular identities, eight extremizers, and sqrt(2) residual ratio`

The code constructs exact rational matrices for the absence of angular frequency two in three coordinate planes, for frequency three in those planes, and for the extra diagonal-plane test. Exact-rational ranks are 6, 9, and 10. The proof itself supplies the symbolic forms of the two-dimensional and cubic kernels; these are not inferred from floating-point numerics. The sampled trigonometric identities and extrema are additional diagnostics and not proofs of all-angle or global statements.

Critical all-parameter proof steps appear in `RESULT.md`: harmonic decomposition; binary cubic divisibility; harmonicity; the exact fourth-plane basis identity; signed-diagonal extremizers with zero-sum quartets; and the nonzero nullspace for at most three prescribed plane restrictions. The standard smooth support-function curvature condition justifies the strict-convexity perturbation. No computational search is used as an infinite proof. All cited references are independent literature, not external validation of this new claim.

Scientific limits: finite support harmonic cutoff ≤3 is essential. The chosen fourth plane is not universal for all placements of four observations. A nearest-ball discrepancy identity applies under exactly three coordinate disk hypotheses, not to arbitrary noisy measurements. Some related full historical technical texts were unavailable for comparison. Independent external auditing has not been performed.
