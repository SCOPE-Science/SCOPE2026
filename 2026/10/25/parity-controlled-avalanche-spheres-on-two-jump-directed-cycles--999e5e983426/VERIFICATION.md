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

From d_i=2−c_i and nonfiring h_i=1_{d_i>0}, the exact recurrence d_i(t+1)=d_i(t)−2h_i+h_{i−1}+h_{i−2} yields B0={0}, moving pairs Bt={2t−1,2t}, and the final odd/even-q-specific wrap block. The explicitly calculated repeated state establishes that these supports exhaust all future firings. The complements are simplex generators. A good-cover nerve is the boundary of a k-simplex for odd n or even q=1, and the even q=0 final simplex is redundant leaving a common-vertex cone. Every t<k prefix is a cone. The integral homotopy and all field-persistence barcodes therefore follow from a nerve argument, not finite mod-two samples.

## originality

PASS

Best-of-knowledge original exact parity-sensitive homotopy and persistence classification for a two-jump circulant and two near-threshold initial configurations, using a complete orbit-to-nerve reduction.

## value

PASS

For a canonical two-jump directed circulant, changing exactly one grain produces an unbounded-dimensional sphere rather than a contractible complex on even sizes, while odd sizes are insensitive; the exact persistence birth is a sharp structural phase transition for a natural dynamical-topological invariant. This substantially refines the new avalanche-complex program beyond examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
