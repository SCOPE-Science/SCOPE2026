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

An unmixed greedy output fills the first vertex's side; in a mixed output each side lies in the deleted-edge neighborhood of any accepted vertex of the other side, so the count is between 2 and 2D and is less than n for n>2D. Conditional on first vertex x, mixed occupancy occurs iff some deleted-edge neighbor y precedes all its initial-side blockers: such a y must be accepted if it beats all blockers, and before the first opposite-side acceptance all previously encountered initial-side vertices were accepted. In the uniform residual order x is not a blocker, and the single-event chance is 1/(n−deg_H(y)+1). A two-event intersection requires both candidates to precede at least n−2D common blockers and is bounded by 2/[(n−2D+1)(n−2D+2)]. With at most D candidates Bonferroni gives deg_H(x)/n+O_D(n^−2). Averaging over the 2n possible first vertices yields m_n/n²+O_D(n^−2). The deficit is zero off that event and n−O_D(1) on it, so its first and second moments are m_n/n+O_D(n^−1) and m_n+O_D(1), with squared mean O_D(1). For fixed r≥2, on the mixed event the centered count is −n+O_D(1), off it O_D(1); splitting the rth moment verifies the stated signed limit, also when c=0. For the C4-free 2-regular family, the two candidates have distinct extra neighbors. The common-blocker count is n−3. Ordering the candidate priorities as u≥v, the intersection integral is 2∫_0^1 (1−u)^(n−2)(u−u²/2) du = 1/(n−1)−1/(n+1). Subtracting from 2/(n−1) gives 2n/(n²−1), and all mixed maximal bicliques are 3-vertex stars. The n=3 size coincidence is properly excluded; the matching has one candidate when x is matched, chance 1/n given that, giving k/n² and mixed count 2.

## originality

PASS

The checked earlier results do not give the uniform mixed-event coefficient and linear variance for arbitrary deterministic bounded-degree deletion graphs. A later indexed exact law genuinely includes the 2-regular special case, but is restricted to a regular C4-free class and does not supply prior coverage of the arbitrary bounded-deletion result. The greedy algorithm and description via maximal independent sets are classical.

## value

PASS

In this natural dense perturbation model the typical count is unchanged, yet rare mixed configurations induce linear variance and macroscopic centered moments. The exact leading coefficient depends only on the number of deletions, uniformly over the different local arrangements allowed by fixed D. This explains behavior that a normalized jamming law or a typical-case concentration estimate cannot resolve. The two-point law provides a transparent benchmark across disconnected and connected deletion families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
