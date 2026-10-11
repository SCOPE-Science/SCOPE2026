---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Let \(Z=\prod_i(P_i\oplus D_{m_i})\) and \(M=\prod_i m_i\). The \(M\) global maxima have principal opens with maxima, giving \(\operatorname{gcat}(Z)\le M\). If a categorical open contained two distinct global maxima, choose a differing coordinate \(j\) and fix points in all other bases. The resulting slice \(P_j\oplus D_2\) lies in the open. Projection back to the \(j\)-th factor turns null-homotopy of the ambient inclusion into null-homotopy of the slice inclusion; the explicit retraction \(P_j\oplus D_{m_j}\to P_j\oplus D_2\) would then make the slice contractible. That is impossible: reducing \(P_j\) to its nonsingleton Stong core preserves the two added maxima, and the capped core has no beat points. Hence each categorical open contains at most one global maximum, so \(\operatorname{cat}(Z)\ge M\). Since \(\operatorname{cat}\le\operatorname{gcat}\), both equal \(M\). The one-factor identities and reduced two-factor defect follow algebraically.

## originality

PASS

Mosquera-Lois--Tanaka Proposition 3.2 proves exactly the one-factor formula \(\operatorname{cat}(P\oplus D_m)=m\) for noncontractible \(P\), and its proof uses the same two-maxima retraction obstruction in one factor. Resultary also shows a prior SCOPE result giving quadratic topological complexity for one capped space, which already covers the equal-factor twofold category value indirectly. Those cases are not counted as new. The submitted final claim is the strictly broader arbitrary finite heterogeneous product theorem, with unrelated bases and cap sizes, plus the explicit unbounded reduced product-subadditivity defect. No inspected source or Resultary hit states or implies that heterogeneous product lower bound.

## value

PASS

Exact product behavior is a natural LS-category question. This family exhibits a sharp non-Hausdorff pathology: reduced product subadditivity can fail by the explicit unbounded amount \((m-1)(n-1)\). The coordinate-slice/retraction obstruction is structural and reusable, not a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
