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

# Verification record

The theorem concerns the exact map \(T_\alpha(x)=1-\frac34|2x-1|-\frac14|2x-1|^\alpha\) for \(0<\alpha<1\). All infinite claims rest on explicit inverse-branch calculations and functional analysis rather than finite sampling.

1. Invert \(4u=3s+s^\alpha\) uniquely for \(s\in[0,1]\). Verify analytically \(\psi'(u)=4/(3+\alpha\psi(u)^{\alpha-1})\), hence inverse contraction by \(\gamma=2/(3+\alpha)\).
2. Set \(p=1/\alpha\) and \(s=(4u)^p q\). The analytic implicit equation \(q^\alpha+3(4u)^{p-1}q=1\) yields \(\psi'(u)\sim p4^p u^{p-1}\); every needed derivative of \(\psi\) through order \(k+1\) is integrable for \(k<p\). For \(p\) integer, the analytic equation \(4u=z+3z^p\) supplies all orders.
3. Check the highest-order chain-rule coefficient \(|\phi_\pm'|(\phi_\pm')^k\) and the resulting \(\gamma^k\) leading \(L^1\) contraction; use \(\varepsilon\)-truncation of lower-order integrable coefficient functions for the final strict contraction.
4. Standard full-branch expanding uniqueness, compact embedding and invariant integration produce the normalized \(W^{k,1}\) fixed point. A cylinder inside a positive-density interval establishes \(h_\alpha(1/2)>0\).
5. The invariant equation forces \(h_\alpha(1-u)\sim p4^p h_\alpha(1/2)u^{p-1}\), ruling out \(W^{\lceil p\rceil,1}\) for noninteger \(p\). For integer \(p\), analytic inverse branches and compact holomorphic transfer yield analytic density.

Exploratory inverse-asymptotic checks evaluated \(p=2,5/2,3,4\) with high precision. Approximate fixed densities from finite transfer iteration were inspected near the critical value. Neither test is an exhaustive certificate or a substitute for the analytic argument. Full publisher text for one closely related 2026 paper and full HTML for another preprint were not available; their abstracts were distinguished from spatial analyticity. Independent audit: not performed.
