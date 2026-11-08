---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For k>=4 and q>=k, follower grounded Laplacian on K_(2,q) with h selected hubs has block [[q I_(2-h),-11^T],[-11^T,2 I_(q-k+h)]]. Its within-class eigenspaces and two-dimensional block yield exact trace J_h=(1-h)/q+(q-k+h-1)/2+(q+2)/(2q-(2-h)(q-k+h)); verify empty class by cancellation. Independent symbolic arithmetic checked J1-J2=(3-k)/(q+k-1)<0 and J0-J1=P_k(q)/(2kq(q+k-1)), P cubic as RESULT. P(k),P(2k)<0, P(3k)>0, P'' positive q>=k: unique transition τ between 2k and3k. Leading k-asymptotic root (1+sqrt(2))k-3/2+O(1/k). Boundary k=q+1 h0 impossible. Independent numerical substitution k=4,5,8,10 confirms signs. The actual verify.py contains rational grounded inversions of class reps, all subsets q=4..8, and exact objective comparison. K_(2,8) k=2 has both hubs optimum, k=4 no hubs optimum, valid non-nesting example.

## originality

PASS

Fitch-Leonard joint centrality provides the inverse-grounded-Laplacian objective and explicit leader placement on paths/cycles; Patterson et al. address weighted paths/cycles, not complete bipartite K_(2,q) arbitrary k>=4. Published Resultary search found a discounted hitting domination biclique result, different objective, and a reported k=3 biclique special case does not cover the stated range. The exact two-hub cubic threshold is a specialized new explicit classification within prior general theory.

## value

PASS

Complete optimizer class for all budgets k>=4 and q>=k on a natural network family, with sharp cubic transition, integer tie behavior, asymptotic threshold and a non-nested lower-budget witness. These give an interpretable control-design boundary that generic combinatorial leader selection methods do not themselves state.

The dated certificate retains the supplied scientific assessment, sources and limitations.
