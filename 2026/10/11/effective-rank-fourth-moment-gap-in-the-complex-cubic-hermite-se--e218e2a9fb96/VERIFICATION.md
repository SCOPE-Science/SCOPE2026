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
The proof was checked directly from the exact identities in Section 8.3 of arXiv:2609.25462v1. The source gives \(\kappa_4=1296(s+3h/2)\), with \(s=\operatorname{tr}(G^2)\) and \(h\ge0\), and for normalized \(q\in\mathcal H_{2,1}\) gives \(\kappa_4=(3/2)(\mathbb E|q|^4-2)\). It also records \(1=3!\,\|f\|^2\).

The trace normalization was replayed symbolically: \(\operatorname{tr}G=\|F\|_{\mathrm{HS}}^2=\|f\|^2=1/6\). Therefore \(\operatorname{tr}(G^2)=1/(36r_{\mathrm{eff}})\), giving the factor \(864/36=24\). For positive semidefinite \(G\), Cauchy--Schwarz gives \(r_{\mathrm{eff}}\le\operatorname{rank}G\), and realification places \(G\) on \(\mathbb R^{2n}\), so \(\operatorname{rank}G\le2n\).

No computation or finite experiment is used as a substitute for proof. The result does not establish sharpness, equality cases, or a dimension-free improvement.
