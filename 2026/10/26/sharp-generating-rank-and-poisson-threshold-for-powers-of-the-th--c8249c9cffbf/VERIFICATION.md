---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

The accompanying `checker.py` uses Python 3 standard library only; run `python checker.py`. It enumerates the original three-element truth tables \(0,u,1\) via the encoding \(0,1,2\) (so integer \(1\) means \(u\)). For each \(1\le m,k\le3\), it constructs every ordered \(k\)-tuple in \(\mathbf K_3^m\), repeatedly closes it under the two constants, negation, meet, and join, and compares actual full generation to the proposed pairwise-disjoint-subcube criterion. Implication is definable from negation and join and therefore does not enlarge closure. An independent word enumeration checks the generation totals.

Finite passing totals by increasing \(k=1,2,3\) are \(1,5,19\) for \(m=1\), \(0,4,138\) for \(m=2\), and \(0,0,336\) for \(m=3\). The hypercube perfect matching recursion returns \(1,2,9,272\) for dimensions \(1,2,3,4\), with the ordered generating tuple count at capacity checked through dimension three. Independent one-coordinate enumerations return exactly \(7/9\) pairwise compatibility and \(17/27\) overlapping-pair joint compatibility. The terminal success marker is `ALL_CHECKS_OK`.

These are finite exhaustive checks and rational-probability checks only. The non-finite equivalence is proved through term monotonicity and the constructed coordinate selectors; the distributional claim invokes the explicitly stated dependency-neighbourhood Chen–Stein bound. No external verification or independently performed audit is asserted.
