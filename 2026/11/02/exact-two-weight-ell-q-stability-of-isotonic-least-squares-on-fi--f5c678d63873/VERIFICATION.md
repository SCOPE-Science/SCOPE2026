---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The literal original correctness assessment is FAIL at V=∅: the Finding says any finite poset, the maximum has no blocks, max_i is undefined as written, and no distinct data pair exists. Even with the canonical zero-dimensional norm the least Lipschitz bound is 0, not the asserted 1. The complete replacement RESULT.md and SLOGAN.txt in /workspace/repairs/2/ restrict the finding to nonempty finite posets, address the empty case separately, and correct the reported profile description (four fitting choices × three monitoring choices on each of seven orders). In the repaired claim, active Hasse components are connected and order-convex because every saturated path between comparable equal-valued endpoints is constant. Strict external edges permit blockwise variations; stationarity makes each branch a direct sum of weighted means. Weighted duality gives the exact branch norms at every q including the endpoints. Continuity and finitely many affine branch restrictions give the global bound on every segment. Conversely, contracting one convex block yields an acyclic quotient, since a new cycle lifts to a path through an outside vertex between block members. Choose strict levels on this quotient and data with residual equal to the sum of internal edge normals. For a small perturbation z, the weighted residual change M(z−Az) is zero off the block and has zero block sum; internal edge vectors span that space by connectivity. Using a fixed basis expresses the change with small coefficients, preserving positivity of active multipliers and strict external inequalities. This proves local affine attainment for each block, also for singletons. A cover pair is an admissible block, and equality in Hölder (or the maximum bound at q=1) forces h_i/m_i to match across each cover; the sup norm is always preserved on constants and nonexpansive. With m=(9,1), h=(1,1), the two-point block gives 2·9/10=9/5 and 2·82/100=41/25 for q=1 and squared q=2, respectively. The proof applies to all positive real masses and disconnected orders. The frozen verification script was inspected, not executed; its finite diagnostics do not cover the empty order or certify the general theorem.

## originality

PASS

For the repaired nonempty scope, the attainable block maximum and exact two-weight rigidity are not supplied by the closest indexed or published statements inspected. The general piecewise-linear reduction is standard, not an additional originality claim; identification and open-region realization of the possible pools and their exact weighted dual norms are the distinct results being assessed.

## value

PASS

Fitting weights and reporting weights can differ in a finite monotone estimation problem. An exact attainable stability factor, expressed in terms of geometrically characterized pools, measures amplification in precisely that setting. The componentwise proportionality criterion and opposite cover-pair witness give a useful diagnostic rather than just a numerical example or an arbitrarily chosen order. Excluding the empty order leaves this entire scientifically useful domain intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
