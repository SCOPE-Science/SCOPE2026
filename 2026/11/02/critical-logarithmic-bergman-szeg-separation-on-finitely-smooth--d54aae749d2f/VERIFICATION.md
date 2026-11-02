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
# Verification and limits

The algebraic scale identities are exact: \(a_k=e^{1-T_{k+1}}\), \(N_k=T_{k+1}-T_k-1\), \(G_ka_k^{-(m+1)}=e^{-(m+1)}\), and \(\log((N_kG_k)^{-1})=(m+1)T_{k+1}-\log N_k\). The limit \(N_k/T_{k+1}\to1\) follows from \(T_{k+1}=\lceil e^{T_k}\rceil\) and \(T_k/T_{k+1}\to0\).

The radial moment formula and estimates were independently checked step by step against Xing (2026) pp. 11–13, equations (4.3)–(4.11). Replacing \(G_k=e^{-kT_{k+1}}\) by \(G_k=e^{-(m+1)T_{k+1}}\) leaves monotonicity, plateau bounds, exponential integral majorants, and \(N_kG_k\to0\) intact. Derivative bounds were separately checked for all integer orders \(0\le j\le m\) and the explicit non-vanishing order-\(m+1\) radial derivative.

All assertions concerning arbitrary \(k\) use inequalities and limiting arguments rather than a finite numerical extrapolation. The result is subsequential and does not imply a globally sharp upper bound or a smooth-boundary endpoint realization. Independent external mathematical validation has not been performed.
