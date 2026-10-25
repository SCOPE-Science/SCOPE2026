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

The proof reduces the tail to a uniformly distributed angular simplex. The three exact checks are: direct inclusion-exclusion for the strips with one half-angle below \(\operatorname{arccot}t\); a uniform middle-edge root expansion for \(\eta=t^{-1/3}\); and the exact corner integral \(J_T=1+2\log(T-1)\). Their cutoff-dependent logarithms cancel, leaving the stated coefficients.

The included `verify.py` uses independent normal-line intersection geometry for 1,000 samples, compares 524,288 conditional angular-simplex draws against the exact one-dimensional conditional-tail integral at three thresholds, and compares that integral against the two-term expansion at seven large thresholds. It uses a fixed seed for reproducibility. The numerical checks do not establish the asymptotic, and no independent audit has been performed. The historical-priority comparison remains limited by the unavailable full text of a 2015 circumscribing-polygon paper.
