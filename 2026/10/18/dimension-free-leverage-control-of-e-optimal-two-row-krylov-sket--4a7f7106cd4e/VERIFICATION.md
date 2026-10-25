---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

From pinned RESULT.md a61db65fdd840e40ab4ceaf0f3920a40619f1112, for two singular values m=sigma_min^2,h=sigma_max^2, ||SQ||_F^2=m+h gives kappa^2=F/m-1. E optimality increases m while maximum/minimum two-row Frobenius mass ratio is <=rho; divide by kappa_D^2>=1 to get sqrt(2rho-1). At rho=1 fixed F makes the objectives equivalent including ties. Constructed u_n,v_n orthonormal with disjoint supports and leverage ratio n; all full-rank selections have diagonal magnitudes (sqrt(n),2),(sqrt(n),1),(1,2),(1,1); unique E pair has kappa sqrt(n)/2, D pair one. A=u v^T+v u^T+2(I-uu^T-vv^T) yields A u=v and a genuine symmetric two-step Krylov basis. Independently checked 150 random frames and the exact family n=5,6,9,15; computation corroborates, does not prove all n.

## originality

PASS

The known global sqrt(n) separation for E versus K row selection is prior published material, explicitly excluded. The new component is deterministic bound depending on local leverage imbalance and equality of solution sets for exactly uniform leverage. Potential source Ucinski/Patan 2022 could contain a general implication and remains inaccessible.

## value

PASS

Leverage imbalance is a natural measurable feature of practical row sketches; the theorem supplies a dimension-free reason when an E-optimal surrogate is distortion-safe, an exact uniform-leverage equivalence, and a genuine Krylov-realizable boundary example. This is a motivated quantitative stability criterion despite its short trace proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
