---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Choose a unit center on one unused coordinate and average \(m\) slices supported on distinct other coordinates. Slice membership forces each selected vector's off-coordinate tail to have norm at most \(\eta_\delta=(1-(1-\delta)^p)^{1/p}\). The average of the disjoint main coordinates has \(p\)-norm at most \(m^{1/p-1}\), and disjointness from the center gives distance at most \((1+m^{1-p})^{1/p}+\eta_\delta\). Letting \(\delta\downarrow0\) proves the finite bound; choosing arbitrarily large finite \(m\) inside an infinite index set gives the limit one. No norm attainment is assumed, since every norm-one functional has points arbitrarily close to its supremum.

## originality

PASS

Best-of-knowledge originality passes. Haller et al. provide the two-summand \(2^{1/p}\) upper scale, while Oja's complete three-page paper proves only that the arithmetic mean of two coordinate slices has diameter below two for a uniformly convex two-dimensional absolute norm. Neither gives the finite \((n-1)^{1-p}\) radius bound or the infinite-index limit \(1\). No stronger published SCOPE hit was found.

## value

PASS

The result reveals a genuine cardinality effect for a standard thickness invariant: averaging more coordinate slices improves the two-summand scale and in infinite sums forces a universal bound of one, without any Daugavet hypothesis on the factors. This is a natural structural bound rather than an arbitrary estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
