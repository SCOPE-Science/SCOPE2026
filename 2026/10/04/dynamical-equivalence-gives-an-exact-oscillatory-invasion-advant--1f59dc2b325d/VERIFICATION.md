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

The scientific check reconstructed the result from equations (27)–(29) of the cited open-access article rather than from a numerical fit. The decisive steps are: (i) the source transformation \(x=r_0h/(1+h)\); (ii) the source recurrence \(h_{n+1}=e^{-p_n}x_n\), hence \(\log x_n=p_n+\log h_{n+1}\); (iii) invariance of the resident measure; and (iv) scalar first-order alien factors \(\alpha h_n\) and \(\alpha x_{n+1}\).

For a period-\(k\) resident cycle, the finite-product check is exact: \(\prod_jx_j=e^{\sum_jp_j}\prod_jh_j\). The accompanying `verify.py` tests both the one-step identity and the product/threshold identities on deterministic positive data and prints `VERIFY_OK` when they agree to floating-point tolerance.

No finite computation is used as a substitute for the infinite-time statement. The invariant-measure conclusion follows analytically from invariance and integrability on a compact positive invariant set. The result is limited to local rare-invader growth and does not certify eventual nonlinear establishment or coexistence.
