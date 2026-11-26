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

Re-audited /workspace/repairs/3/RESULT.md. The frozen proof incorrectly asserted that every positive-entropy invariant measure gives zero mass to the countable precritical set; a mixture of the uniform-branch law with a fixed-point atom disproves that assertion. The repaired argument only requires this of maximizing measures and proves it by entropy affinity. The corrected finding also specifies smoothness of the arcsine density only in the interior, not at the endpoints. The precise map and numerical entropy formulas are unchanged. At degree d=2 mod 4 the joined jets have value -1 and first derivative 0. The cosine change of variables gives m/2 and n/2 affine full branches, with inverse widths 1/m and 1/n and N=(m+n)/2. At every depth r there are N^r monotone, full cylinders with disjoint interiors and alternating orientations, giving h_top=log N. Their diameter shrinks geometrically. Branch endpoints map into the endpoints {0,1}, so the countable precritical set E is completely invariant. The uniform branch Bernoulli measure gives at most 2N^(-r) mass to a point, hence avoids E and preserves its full-shift entropy. For a measure with mass a>0 on E the invariant restriction there has zero entropy; affinity bounds total entropy by (1-a)log N. Each maximizing measure thus lifts bijectively off E to the unique full-shift maximizer. Lebesgue cylinder masses are products of their inverse widths, giving the invariant iid branch law and trivial tail. Exactness gives uniqueness of the absolutely continuous invariant probability; the Lipschitz cosine sends null sets to null sets and pushes Lebesgue to arcsine. The two sign probabilities are sums over the left half branches: 1/2 for Lebesgue and (m/2)/N for the uniform branch law. The generating partition yields h_mu=(log m+log n)/2. Different almost-sure sign frequencies prove singularity when m differs from n, and fixing m=2 gives an unbounded gap. The original verifier was read, not run; independent recurrence spot checks of the value and first/second derivatives at the join for (2,2), (2,14), (6,18), and (10,22) agree and are not evidence for the all-degree entropy claims.

## originality

PASS

For the final corrected claim, the recognizable contribution is the explicit C^1 Chebyshev splice realizing all-time fair signs under one fixed arcsine physical law, a different Bernoulli law under the unique maximizing measure, and an arbitrarily large entropy gap. The general full-branch entropy and slope facts are established, as are examples with distinct physical and maximal measures. No inspected source gave the explicit observation-preserving Chebyshev construction or a result implying this whole comparison as a direct specialization. The two most relevant Chebyshev papers could not be fully inspected, so the assessment is qualified.

## value

PASS

The repaired construction is a concrete witness to how little a fixed observation can reveal about the underlying dynamics: the coordinate sign process has the same law at every time scale and the physical density is identical throughout the family, yet the exact entropy deficit is unbounded and sampling from the maximizing measure changes the observed sign bias. Retaining those constraints in an explicit C^1 polynomial splice is the mathematical purpose; re-deriving standard full-shift entropy by itself would not meet the bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
