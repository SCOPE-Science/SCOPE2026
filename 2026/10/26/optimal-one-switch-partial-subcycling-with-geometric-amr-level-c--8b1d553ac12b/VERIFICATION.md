---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For fixed finest update count nu_L=r^L, each adjacent inversion (1,0) to (0,1) changes modeled cost by T w_i[h(rho-1)-(1-1/r)]. Below h_c all inversions strictly improve; above the threshold telescoping C(b)-C_global=sum_i b_i nu_i w_i(h-theta_i) excludes any active boundary, even at h=h_c because theta_i<h_c at finite i. For suffix schedules, C_(k+1)-C_k=r^(k+1)w_(k+1)(theta_(k+1)-h); strictly increasing theta_i gives the exact first-crossing, unique minima off thresholds, and exactly adjacent ties on a threshold. r>=2,L>=1,c>0,rho>=1,h>=0, with no real-runtime implication. Independent rational enumeration checked 482 combinations through L=7; this is corroboration, not the unrestricted proof.

## originality

PASS

The geometric weighted-cost optimization is distinguished from published formulas for a prescribed subcycling schedule and from application-level AMR partial-subcycling selectors. No retrieved primary statement gives the all-binary-pattern suffix optimizer under this specific fine-side overhead; best-of-knowledge originality is qualified by unindexed scheduling analyses.

## value

PASS

A full sharp and finite-depth classification for an intrinsically motivated choice—whether, and where, to subcycle a geometric hierarchy under coordination charge—answers a natural optimization question and provides an exact threshold benchmark for comparing heuristics. The model is explicitly not an empirical performance law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
