---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Rank reversal maps W→−W and R→R, proving Cov(W,R)=0 without independence. Conditioning J_t=1 selects one of the adjacent two ranks with probability 1/2 and leaves a uniformly random (a−1)-subset among N−2 others; finite-population variance of this subset plus independent pair orientation yields exactly the displayed local quadratic correction in (t−N/2)². The exact identity sum_{t=1}^{N−1}(t−N/2)²=(N−1)N(N−2)/12 cancels the local correction, leaving −ab(ab−1)/(3N). The case N=3 is checked by direct three-word enumeration, with −2/9. Since ab>=2 for N>=3, strict negative sign holds. Independently enumerated every composition N=3..11 with exact rational arithmetic (54 composition cases) and all J_t local profiles N=4..11; all match. Finite enumeration is corroboration only.

## originality

PASS

Best-knowledge PASS for the *exact finite null mixed covariance of squared rank sum with number of runs plus complete location-resolved J_t profile*, not the individual Wilcoxon and Wald–Wolfowitz tests. The closest published two-sample paper analyzes asymptotic comparisons and marginal covariance structures, not this finite mixed second-moment formula in material read. An older joint generating function for ranks and runs may imply it and remains a concrete risk.

## value

PASS

The exact dependence of two widely used distribution-free two-sample statistics under the shared permutation null is a natural finite-sample calibration fact. Despite zero linear covariance, the squared rank departure has strictly negative runs association and a nontrivial position-dependent local cancellation; this distinguishes joint test behavior and may guide combined diagnostics without claiming optimal power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
