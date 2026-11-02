---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The two-step killed walk has b=2 sole even state, giving s_t=(pq)^t. At b=3 a 2×2 substochastic kernel has s_t=p(2pq)^(t−1) for t>=1, so first hazard comparison requires p>=1/2. At b=4 its two eigenvalues ((3±sqrt5)/2)pq yield s_t=A λ+^t+B λ−^t with A>0 and log-concavity determinant −AB(λ+−λ−)^2(λ+λ−)^(t−1). This is >=0 exactly when p >=(sqrt5−1)/2, with equality all ages at the boundary. For b>=5, no upper absorption in four steps and exact Catalan-prefix enumeration gives s1=p and s2=p²(2−p), hence h2−h1=−p(1−p)<0. At b=1 absorption first step. Independent exact fractions checked b<=8 and five biases; analytic arguments handle all 0<p<1, all b.

## originality

PASS

Liang 2026 establishes parity-skeleton IFR for symmetric absorbing intervals and explicitly describes asymmetric barrier IFR as an extension problem. The present one-step lower barrier is asymmetric, and the conclusion is a full discrete hazard phase diagram, not just a stochastic drift order. Geng–Markowsky 2025/2026 same-walk full indexed article concerns stochastic dominance of exit time on symmetric [-k,k] when changing drift; its Theorem1 does not imply fixed-p ageing classification for {-1,b}. A broader general finite birth-death reliability theorem could hide the sharp classification, so literature priority remains a bounded risk.

## value

PASS

A complete natural asymmetric boundary family exhibits distinct constant, half-drift, golden-ratio, and universal failure phases. The exact threshold and failure after four raw steps answer a motivated gap of the symmetric first-passage ageing theory, without asserting arbitrary intervals or other censoring rules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
