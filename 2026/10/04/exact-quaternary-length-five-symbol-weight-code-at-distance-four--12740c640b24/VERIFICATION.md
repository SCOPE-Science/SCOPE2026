---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Distance four makes every two-coordinate projection injective, so a hypothetical size-16 code would project bijectively onto all 16 ordered symbol pairs for each of ten coordinate pairs. That forces 40 equal-coordinate incidences. But a length-five word of symbol weight at most two has composition \((2,2,1,0)\) or \((2,1,1,1)\), contributing at most two equal-coordinate pairs, so 16 words contribute at most 32, contradiction. The displayed 15-word witness was independently checked for symbol weight and all pairwise distances. At size 15 each projection misses one pair and therefore contains at least three diagonals, yielding at least 30 equal-coordinate incidences; the per-word upper bound is also 30, forcing every word to type \((2,2,1,0)\) and each missing pair to be diagonal. A fresh independent witness/projection replay confirmed all ten projections.

## originality

PASS

Chee--Kiah--Purkayastha introduce the exact symbol-weight-code invariant and give general bounds and examples, but inspection found no quaternary \((5,4,2)\) value. The later generalized balanced tournament work uses exact finite symbol-weight code questions at different parameters. Resultary search found no exact value 15 or equivalent two-coordinate incidence theorem. The upper bound here is not a lookup from a general bound: it exploits the special equality geometry at length five.

## value

PASS

This is a natural smallest boundary where the unrestricted Singleton size 16 is ruled out specifically by the symbol-multiplicity constraint, and the exact one-word deficit comes with a complete forced local projection structure for every optimum. That makes the finite result a useful benchmark for symbol-weight packing/design theory rather than a bare brute-force datum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
