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
# Verification details

The theorem is established by an analytic proof, not an enumeration. To reproduce its decisive checks:

1. For \(B=I-G^*G\), \(Q_\varepsilon=\mathbf1_{[\varepsilon,\infty)}(B)\), and unit \(x\) with \(\|Gx\|>1-\delta\), verify \(\varepsilon\|Q_\varepsilon x\|^2<2\delta-\delta^2\).
2. Universal equality of the relative and essential norms implies each \(Q_\varepsilon\) is compact, hence finite rank, and \(\|B-BQ_\varepsilon\|\le\varepsilon\). For \(x\in\ker B\), test the rank-one projection \(R_x\) to exclude a nonzero kernel.
3. Conversely, finite rank of \(Q_\varepsilon\), strong convergence \(P_\varepsilon=I-Q_\varepsilon\to0\), and the two-sided near-norming estimates give \(p_G(T)=\lim\|TP_\varepsilon\|\).
4. Check \(\|T\|_{\mathrm{ess}}\le\|TP_\varepsilon\|\) by removing finite-rank \(TQ_\varepsilon\). For arbitrary compact \(K\), verify \(\|KP_\varepsilon\|=\|P_\varepsilon K^*\|\to0\) by uniform convergence on compact sets; infimize over \(K\).
5. The diagonal witness \(Ge_n=\sqrt{1-1/(n+1)}e_n\) has norm one and compact injective defect. Nonseparable spaces cannot admit an injective positive compact defect because its dense range is separable.

These are full universal Hilbert-space arguments. No finite numerical test is treated as a certificate, and no independent audit is claimed.
