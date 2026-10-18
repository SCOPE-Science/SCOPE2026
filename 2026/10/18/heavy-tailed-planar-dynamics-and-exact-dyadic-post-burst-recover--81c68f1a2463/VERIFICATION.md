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

# Verification

The independent-audit channel has not been performed. The following checks are internal reproducibility evidence, not an independent proof audit.

Run `python verify.py` using Python 3 (standard library only). Expected terminal output: `VERIFY_OK`.

The checker verifies the graph-lift identities with exact rational numbers at 32 non-boundary points and verifies that the precritical vertical bound is attained by \(t=1/2\). It then checks the conditional finite-threshold passage formula against explicit angular interval fractions, the exact geometric-tail expectation, and sample angle first-crossing times. Finally it checks the asymptotic stationary-tail coefficient at a large finite threshold.

**Analytic checks:** (i) direct substitution of the rational map into its invariant graph; (ii) logistic reduction and critical-value inequality; (iii) Lebesgue ergodicity of the doubling map and graph pushforward; (iv) beta-integral convergence at moment order \(1/2\); (v) uniform conditional angle and monotone pre-crossing angle doubling; (vi) summing the geometric survival law and constructing all dyadic phase subsequences. All are proved in `RESULT.md`; the checker only cross-tests selected identities.

**Limits:** finite sample runs cannot prove invariant-measure ergodicity, countable exceptional-set claims, or infinite-time asymptotics. No external validation or independent audit is claimed. The primary source already supplied the logistic fold and invariant graph; the new mathematics concerns its previously excluded critical endpoint and post-burst time law.
