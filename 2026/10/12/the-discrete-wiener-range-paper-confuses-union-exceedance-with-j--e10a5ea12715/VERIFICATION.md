---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For independent R_i with CDF F_i, 1-prod F_i = P(union_i {R_i>r_i}) by de Morgan, whereas simultaneous strict upper survival P(intersection_i {R_i>r_i})=prod_i(1-F_i). Inclusive lattice survival replaces r_i by r_i-1. For two identical tails s the first is 2s-s^2 and second is s^2, so their ratio 2/s-1 diverges as s->0; for n the ratio~n s^(1-n). Componentwise rectangular truncation preserves independence. The source Eq 3.6 p_joint/(1-Fjoint) measures a different union-conditioned construction, not the Prop.1 joint-cell hazard with a product of inclusive marginal survivals. IMPORTANT precision: the authors explicitly acknowledge directly after Eq.3.6 that the latter is a different multivariate hazard construction, so the defect is misleading co-exceedance interpretation rather than an unacknowledged algebraic identity in that paragraph.

## originality

PASS

Best-of-knowledge PASS for a specific documented source correction, NOT novelty of de Morgan or general survival definitions. The inspected February 2026 paper calls the complement a joint survival and interprets it as simultaneous thresholds in its discussion and Figure 16; 2025 precursor apparently shares convention. No published source-specific erratum located by exact title/DOI targeted search. Short publication lag and possibly alternate max-risk convention are explicit risks.

## value

PASS

This corrects interpretation of multivariate extreme-risk figures for a published model. In the tail the reported at-least-one exceedance risk exceeds true all-component exceedance by an unbounded factor, with direct relevance to risk and reliability inference. The substantive use case makes this source-specific elementary event correction valuable, while union exceedance is itself a legitimate statistic under correct labeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
