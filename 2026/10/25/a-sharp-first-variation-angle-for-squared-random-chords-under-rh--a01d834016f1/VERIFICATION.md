---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS. Since iid squared distance equals twice variance, the unit rhombus starts with Var(B)=1/3, Var(I)=1/6. Removing area O(t²) leaves interior first derivative zero; deleted boundary length 2t and new length h t, h=sqrt(2-2c), give perimeter 4+(h-2)t and unnormalized centered second moment 4/3+(h-2)(1+c)t/2+O(t²). Quotient derivative is (h-2)(1+3c)/4, with precise threshold c=-1/3 (no higher-order assertion). Independent exact-rational Green and segment moments of specified 5 integer vertices reproduce ratio 3586477854403938963/1792478301783239474>2, all consecutive turns convex.

## originality

PASS

PASS best knowledge. Lotnikov 2026 central-symmetric exact second moments and lower comparisons do imply rhombus baseline ratio2, but no asymmetric pentagon perturbation derivative; its general projective-boundary formulas use different sampling when not circumscribed. Tokmachev 2026 accessible abstract studies lower convex-order comparison, not an upper ratio. Risk inaccessible full Tokmachev paper/unindexed earlier upper-ratio examples.

## value

PASS

PASS. The precise first-variation threshold distinguishes symmetry breaking that improves versus worsens a natural squared-chord statistic. An explicit strictly convex rational upper-bound counterexample has qualitative force: disproves plausible factor-two bound for all planar convex bodies. No global maximum or behavior at zero derivative asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
