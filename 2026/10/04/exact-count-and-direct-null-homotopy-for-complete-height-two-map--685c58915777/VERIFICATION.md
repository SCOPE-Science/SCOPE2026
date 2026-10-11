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

The four image-shape cases are exhaustive for an order-preserving map from the complete height-two poset. They contribute respectively \(n(3^p-2^p)\), \(n(3^q-2^q)\), \(n2^q\), and \(n(2^p-2)\), summing to \(n(3^p+3^q-2)\). For \(n\ge3\), two distinct target minima have a common upper neighbor only when they are consecutive, and then that upper neighbor is unique; this is the only nontrivial crown incidence fact used. Every case gives a pointwise comparison with a constant map, hence a finite-space homotopy to a constant. An independent brute-force replay for \((p,q,n)=(2,2,3),(2,3,3),(3,2,3)\) recovered counts \(48,102,102\) and a comparable constant for every monotone map. The \(n=2\) sharp boundary is consistent with the rigidity of the four-point crown core.

## originality

PASS

The inspected finite-space literature supplies the order/continuity and homotopy framework, while the closest enumerative literature located is explicitly about fences and crowns. A general \(P_{p,q}\) source is neither a fence nor a crown except at the isolated \(p=q=2\) case. Resultary returned the assigned theorem as the exact hit; nearby published findings concern the reverse direction, self-maps, or weak-order targets. No implication-equivalent theorem covering the complete-height-two-to-longer-crown family was located.

## value

PASS

The source and target are canonical finite graph models, and the theorem gives both a closed hom-set count and a sharp direct-realizability obstruction despite the source order complex having nontrivial first homology. The failure at the four-point crown makes the target-length boundary mathematically meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
