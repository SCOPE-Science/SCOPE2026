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
The claim was checked directly from the quantitative estimates in arXiv:2609.31779v1. The critical steps are: equation (6.19) for exponential concentration of the normalized coefficient \(\ell^{q_m}\)-norm; Proposition 6.5 for the uniform mean asymptotic and Gaussian concentration of the supremum norm; Lemma 3.1 for \(R_m\le N_{m,n}^{1/(2m)}\); and Section 6.5 for \(N_{m,n}/H_{m,n}\to\infty\) uniformly.

For fixed \(s\ge1\), the good-event contribution to \(\mathbb E|Y_{m,n}-1|^s\) is arbitrarily small by choosing the concentration window small. On the bad event, \(0\le Y_{m,n}\le\sqrt{H_{m,n}}\), while the bad-event probability is bounded by a sum of terms exponentially small in \(N_{m,n}\) and \(H_{m,n}\). Since \(H_{m,n}\to\infty\) uniformly and \(N_{m,n}/H_{m,n}\to\infty\) uniformly, the bad-event moment tends to zero uniformly in \(n\).

The argument proves only fixed finite moments. It does not provide uniform control when the moment order depends on \(m\), and it does not prove exponential integrability.
