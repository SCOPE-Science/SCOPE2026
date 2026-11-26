---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the symmetric nonnegative fixed-row-sum class with m>=2, positive L_i and H>=sum L_i, put h=H-sum L_i and Q=sum L_i^2. The star's positive eigenvector v=(Lambda,L_1,...,L_m) has eigenvalue Lambda by Lambda^2=h Lambda+Q, so Lambda is its Perron root, also at h=0. For D=M-M_star, D1=0 by the row constraints and symmetry. Thus v^T D v = (Lambda 1-v)^T D (Lambda 1-v) = g_per^T M_per g_per with g_i=Lambda-L_i>0, because the hub coordinate is zero and the star's peripheral block vanishes. Dividing by Lambda^2+Q via Rayleigh–Ritz proves both reported defect inequalities. Any nonzero peripheral block makes the defect strict; a zero block forces the star by the row sums. Evaluating the quadratic at 1 proves Lambda<=1 iff h+Q<=1; this is a condition for existence of an admissible matrix at or below threshold, with only the star at equality. The exact example's Rayleigh defect is 3/55. The universal decision is analytic; the submitted script was inspected and not executed.

## originality

PASS

Credit is for the closed form and unique minimizer for arbitrary, including unequal, peripheral totals and the quantitative defect. The optimization problem itself is established, and a distinct same-day record already gives the full minimizer/value in the equal-peripheral subfamily. Neither the matched general optimization formulation nor the two-rate result states or implies the arbitrary heterogeneous formula and defect by direct specialization.

## value

PASS

This is an exact answer to a natural constrained minimization previously posed in general SDP form. In the heterogeneous dominant-row regime it replaces optimization with an explicit feasibility threshold, identifies the only minimizer, and bounds the loss away from the minimum by an interpretable peripheral mass defect. These are substantive beyond repeating the equal-peripheral example or a generic spectral estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
