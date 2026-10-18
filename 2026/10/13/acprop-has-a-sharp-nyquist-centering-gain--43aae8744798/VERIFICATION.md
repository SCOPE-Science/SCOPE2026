---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

On alternating g_t=(-1)^{t-1}G, the exact first moment unrolls to m_t=(-1)^{t-1}aG[1-(-beta1)^t], a=(1-beta1)/(1+beta1). Thus g_t-m_t=(-1)^{t-1}G[c+a(-beta1)^t] with c=2beta1/(1+beta1). The centered second-moment EMA s_t=(1-beta2)G^2 sum_{j=1}^t beta2^{t-j}[c+a(-beta1)^j]^2 tends to c^2 G^2 for 0<=beta2<1. One-step delay preserves the limit. Uncentered comparator v_t=G^2(1-beta2^t) tends to G^2, so update gain is (|G|+epsilon)/(c|G|+epsilon), and for epsilon=0 becomes (1+beta1)/(2beta1). Correct edge conditions beta1>0, beta2<1, G!=0, epsilon>=0; beta1=0 with epsilon=0 is singular. Independent exact rational 180-step recurrences verified transients and limiting residual/denominator for selected rational decay rates, supplementing the geometric proof.

## originality

PASS

Best-of-knowledge original sharp Nyquist-frequency centered-versus-uncentered gain for the paper-form ACProp recurrence; related algorithm response results have different denominators and different formulas.

## value

PASS

The Nyquist/period-two signal is the natural highest frequency for a discrete-time gradient stream. The exact centered denominator attenuation, beta2-independent asymptotic amplification and divergence for small beta1 expose a concrete tradeoff in an established adaptive optimizer; this is a sharp design diagnostic, not a merely arbitrary numerical test or claim of objective convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
