---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For uniform m-of-n sampling, indicators I_i of total neighborhood loss satisfy E[I_i]=a_m and E[I_iI_j]=B_m(t_ij), t_ij=|N_i∩N_j|; hence Var(Z)=n a_m+2 Σ_{i<j}B_m(t_ij)-n²a_m². Column-regularity gives Σ t_ij=n d(d−1)/2. Put s=n−m; B_m(t)=C(n−2d+t,s)/C(n,s), with second finite difference C(n−2d+t,s−2)/C(n,s)≥0, so endpoint chord dominates B_m(t). Summing the chord gives n d a_m+n(n−d)b_m−n²a_m² and the exact 2Σδ_m(t) deficit. For d≤m≤n−2 (2≤s≤n−d), distinct endpoint slopes force strict chord at every integer interior 1≤t<d. Equality therefore means all plant neighborhood intersections are zero or complete; d-regular columns imply every common-neighborhood class contains exactly d plants, giving the unique disjoint K_{d,d} block graph. For m<d, m=n−1 and m=n, Z is identically 0, n−d and n. No claim for d=1 or n=d. An independent exact enumerator checked all 90 4×4 and 67,950 6×6 d=2 labeled incidence matrices, all deletion stages, direct subset moments, exact deficit and equality (finite corroboration only).

## originality

PASS

Best-of-knowledge PASS for the unrestricted sharp fixed-size coextinction variance and exact overlap-defect identity. Fully inspected primary ecological sources use the same loss mechanism or robustness themes but study empirical means or integrated scores; Zhao gives a regular-graph independent-set polynomial bound with the same biclique shape but a different observable. Relevant published mathematical search results concern other variance functionals. No inspected theorem mathematically implies the exact all-stage hypergeometric second-moment envelope, strict equality or overlap gap. Residual possibility of a general extremal incidence U-statistic theorem under different names remains.

## value

PASS

Uniform fixed-count species loss is a natural ecological-combinatorial random process. Degrees fix the mean a_m, yet dispersion depends on neighborhood overlaps. Determining a SHARP global variance envelope for every n multiple of d and every m, identifying its unique informative-stage structural maximizer, and expressing an exact positive deficit for partial overlaps is a meaningful all-parameter extremal classification with diagnostic stability information. The theorem is not merely enumerating tiny examples, renaming an old independent-set inequality, or asserting that modularity is ecologically desirable. It applies only to simple binary balanced regular incidence graphs and one-step topological extinction with exact uniform sampling, not dynamical persistence or independent failures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
