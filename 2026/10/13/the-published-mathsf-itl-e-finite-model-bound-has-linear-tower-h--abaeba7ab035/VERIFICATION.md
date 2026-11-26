---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The published Lemma 30 and its displayed phase counts give the frozen E,Q product for B(s); s here is |Σ|, and Theorem 31 uses B(|φ|). For n≥2 set D_k=T_(k−1)(3n). E_1=n, and E_(k+1)≥2^(E_k), giving the lower tower. The bound E_k≤D_k/2 propagates because E_(k+1)≤(n+1)2^(E_k) and (n+1)²≤2^(3n−2); the latter holds at n=2 and its left-side growth ratio is less than 8. Q_1=1 and Q_k≤D_k propagates via 1+D_k²/2≤2^D_k: for integers D≥6, D²+2 grows by a factor at most two per step, and the base case holds. For s≥1 and N=2^(s+1), sQ_(s+1)^(2^s) and Q_(s+3)^N are at least one, giving the lower bound by E_(s+3)^N. Every E and Q factor in the expression for B is bounded by X=T_(s+2)(3N). As X≥s+2 and X≥32, X(2X+sX²)≤X^5≤2^X (5 log₂ X≤X at 32 and its derivative is less than one thereafter). Applying log-star strips the stated number of tower layers, and shifting the remaining argument from s to s+1+log₂3 changes log-star by a bounded amount (for s≥3 the shifted argument is ≤2^s). This proves the sandwich and asymptotic for the displayed bound, not a lower bound on necessary model size or decision complexity. VERIFICATION.md and verify_tower_height.py were inspected, not executed. The finite checks do not construct B(s) on the general range; the named log-star checks use floating-point logarithms. The uniform proof is decisive.

## originality

PASS

The source's exact recursive upper bound and qualitative non-elementary classification are prior work. The distinct claim is the explicit two-sided tower comparison for that function, which quantifies its growth and does not reinterpret it as a lower bound on the logic.

## value

PASS

The printed bound is central to a published constructive decidability result, and merely calling a scale non-elementary permits far faster growth as well. Pinning its iterated logarithm to a leading coefficient of one with the stated additive correction is a useful quantitative benchmark for comparing model constructions, without claiming that actual instances require this size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
