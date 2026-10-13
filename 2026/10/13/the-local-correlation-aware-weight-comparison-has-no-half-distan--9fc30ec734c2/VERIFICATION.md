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

The exact domain is the source's on-chain two-class model: odd \(d\ge3\), packet size \(1\le n<d\), a contiguous packet error \(E\) on a minimum-weight logical \(\bar X\) chain, and the complement \(E'=E\bar X\) on the remaining \(d-n\) sites.

The critical checks are analytic:

1. \(E\) and \(E'\) have the same syndrome because their product is the logical operator \(\bar X\).
2. The anchor assigns \(E\) the single correlated-edge weight \(w_{\mathrm{net}}=-\log p_{\mathrm{net}}\).
3. The anchor's reduced comparison assigns \(E'\) the cost \((d-n)w_{\mathrm{gate}}\), with \(w_{\mathrm{gate}}=-\log p_{\mathrm{gate}}\).
4. Under \(p_{\mathrm{net}}\ge p_{\mathrm{gate}}\), monotonicity of \(-\log\) gives \(w_{\mathrm{net}}\le w_{\mathrm{gate}}\).
5. Since \(d-n\ge1\), positivity of \(w_{\mathrm{gate}}\) gives \(w_{\mathrm{gate}}\le(d-n)w_{\mathrm{gate}}\).
6. If \(d-n\ge2\), the second inequality is strict. If \(d-n=1\), strictness is equivalent to \(p_{\mathrm{net}}>p_{\mathrm{gate}}\).
7. At \(n=d\), the packet is the full logical operator and the syndrome vanishes, so the two-defect comparison is no longer available.

No numerical certificate is required. Finite simulations in the anchor are not used to prove the statement. The unresolved limitation is global: another syndrome-equivalent matching can be cheaper than both displayed classes, so the result is not a theorem of full MWPM fault tolerance beyond \(\lceil d/2\rceil\).
