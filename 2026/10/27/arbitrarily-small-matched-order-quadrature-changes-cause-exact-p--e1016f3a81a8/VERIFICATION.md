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

Pass on the corrected RESULT.md, not on the frozen universal one-update assertion at a tie. The frozen pointwise policy and distinct LHS/RHS nodes permit control 0 at the midpoint and 1 at both shifted left nodes when a=1; then a'=(3−ε²)/2 is neither cycle point (e.g. 3071/2048 at ε=1/32). The repair proves the sharp entry bound, clarifies matching midpoint assembly, and phrases the general two-fixed-point classification off the switch. For every allowed ε, set t=ε². Direct nodal summation gives p=2+t, q=1−2t; the cutoff construction makes these equalities exact. A tied update is (p+β)/(2+α(1/2)) with 0≤β≤q: midpoint policy 0 makes it >1; policy 1 makes it <1. It enters the exact primitive cycle at the next update, or immediately for either uniform tie. The generic strict branch images are p/2 and (p+q)/3, with neither equal to 1; a cycle cannot include the switch and the sign tests give the announced off-switch basins. In the residual case the t bias is independent of ties; from a≤1 the next value is >1, where the slope is 2t/3 and the fixed point is 1+t/(3−2t). With both sides at the midpoint the two affine residuals vanish at 1 with slopes 2 and 3. The symmetric Taylor bound and positivity give arbitrarily small discrepancies in the specified C² test norm. Independently enumerated all pointwise tie assignments for three exact-rational offsets (python3 /workspace/audit-work/independent_checks.py 2); this supplements the all-parameter inequalities. The frozen checker was inspected, not run.

## originality

PASS

The surviving result is a fixed smooth-coefficient one-hat construction with arbitrarily small positive symmetric rule perturbations of the same affine exactness, exact global period two, exact residual-form bias and rate, and the strict moment criterion. Nonmatching quadrature, the two implementation forms, and qualitative nonconvergence versus slow convergence are already known and are not credited as new. Fixing the pointwise tie handling preserves the distinct result.

## value

PASS

The counterexample gives a concrete zero-tolerance boundary: fixed data, positive rules with identical affine exactness, a strongly monotone midpoint Bellman equation and arbitrarily small discrepancy do not ensure convergence across the policy tie. The exact amplitude, consistent residual floor and alternative biased contraction distinguish genuine cycle dynamics from numerical stagnation. This is worth retaining without a claim that it applies at strictly complementary solutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
