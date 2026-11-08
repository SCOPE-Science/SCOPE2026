---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For d_mu(t)=(1+t/sqrt(t²+4mu))/2, scaling x=t/(2sqrt(mu)) reduces barrier shrink to g_sigma(x)=x[1/sqrt(x²+σ)−1/sqrt(x²+1)]/2. Its derivative has unique positive root x²=σ^(2/3)/(1+σ^(1/3)), producing D(σ)=(1−σ^(1/3))/(2sqrt(1+σ^(1/3)+σ^(2/3))) and the stated symmetric equality points. Since d_mu' is even and strictly unimodal, length-|h| intervals integrate maximally when centered at zero, giving H_mu(h)=|h|/sqrt(h²+16mu) with equality at t=−h/2. Differentiation in log(mu) yields max 1/(6sqrt(3)). Only inequality diagonal changes in J_mu(v), so its spectral norm difference is the max coefficient difference and is bounded by min(1,D+max H). The frozen-system residual follows from (J1−J0)J0^-1r and is sufficient, not necessary. Independent 27,030 point checks confirmed separate equality and bounds; proofs establish all real parameters. The joint sum is not claimed sharp.

## originality

PASS

Best-of-knowledge original sharp two independent finite-parameter moduli and a source-specific KKT reuse certificate, not new smoothing or general Newton convergence.

## value

PASS

Provides dimension-independent, attainable worst-case perturbation thresholds for reuse of a nonsingular condensed Newton factorization; reveals a nonzero barrier-independent risk in the moving O(sqrt(mu)) transition layer missed by pointwise small-barrier heuristics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
