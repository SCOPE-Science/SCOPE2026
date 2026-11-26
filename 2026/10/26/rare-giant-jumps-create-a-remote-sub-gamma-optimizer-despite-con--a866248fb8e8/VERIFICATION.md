---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For fixed true variance V, put M=2K/(Vt²), with K the centered log-MGF. Rearranging the defining inequality below 1/c gives c≥(1−1/M)/t; at and above 1/c this comparison holds automatically by (1−1/M)/t<1/t. The compound-Poisson log-MGF gives the stated Beta(1,2) mixture and cumulants λ(1−q+qb^m), so the convergence holds exactly for the asserted integer orders 2≤m<κ. Put w=κ−2. For t≤(w−ε)log(b)/b, L(z)−1≤ze^z/3 bounds the profile uniformly by O(1+b^(1−ε))=o(b/log b); above that window use 1/t. At t=(w+ε)log(b)/b, the large-jump contribution to M grows like a positive constant times b^ε/(log b)². This gives both sharp asymptotic constants as ε tends to zero. Taylor expansion gives derivative (3AC−4B²)/(36A²), uniformly tending to −1/36 on the full q interval since κ>4. A superior positive peak exists by the asymptotic and the 1/t tail bound. Between the origin and that peak a minimum is attained in the interior, so there are at least two distinct positive stationary points. For onset, the coefficient comparison with (1−t/3)^−1 gives strict global dominance of the origin at q=0, including t≥3 via the tail bound. The jointly analytic extension near zero and uniform derivative sign for each large fixed b give a q-uniform excluded neighborhood for competing maximizers. The tail beyond 4 is below every origin value. Continuity of the resulting compact maximum and a subsequential maximizer limit at first strict superiority prove coexistence at an interior q_c, without monotonicity or uniqueness.

## originality

PASS

The distinct claim is the growing-positive-jump rare-contamination asymptotic at fixed true variance, jointly with low-cumulant convergence and coexistence while the local slope stays negative. The canonical profile and fixed-law interior examples are prior; the closest transition and inverse-log examples have materially different regimes or conclusions.

## value

PASS

This quantifies a failure of finite-cumulant and local-profile diagnostics for true-variance sub-gamma optimization: an unbounded optimal scale with a sharp coefficient despite convergent low cumulants, and a positive global optimizer that enters without a local instability. The rare/support regime and coexistence provide structural information beyond an isolated interior witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
