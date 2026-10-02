---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

From the source paper's fibre quadratic, direct algebra gives discriminant H(z)=1-4 gamma z+12 alpha z^2-8 beta' z^3, so membership in the rational value set is equivalent to H(z) being a square or zero. Fresh symbolic expansion reproduced this polynomial. Smoothness of the elliptic curve makes H squarefree. For fixed nonzero a, two translated cubic factors can share a root for at most six a-values per coordinate pair; hence at most 3m(m-1) exceptional a. For the others the product over any nonempty subset is squarefree of degree 3|S|, so the quadratic Weil bound gives (3|S|-1)sqrt(q). Expanding the membership indicators and separately charging root hits yields the stated q^2/2^m +(3/2)m q^(3/2)+3m^2 q bound. Summing prefixes to L=ceil((log_2 q)/2) gives the claimed deterministic runtime. The finite verifier independently matches direct value sets and survivor bounds at q=101,251,509; it is supporting, not the proof.

## originality

PASS

The primary attack paper proves only a deterministic O(n q^2) enumeration bound and then obtains O(q^2) average cost under an explicit heuristic independence assumption that it says is not a consequence of the preceding statements. The audited character-sum argument removes that heuristic and supplies a different worst-case bound. Searches found no prior deterministic affine-value-set pruning theorem with this cubic character-sum estimate.

## value

PASS

Replacing an acknowledged heuristic by a deterministic character-sum estimate in a concrete structural-attack bottleneck is a meaningful mathematical and algorithmic improvement. The bound is reusable for affine filtering through low-degree value sets, not merely a finite benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
