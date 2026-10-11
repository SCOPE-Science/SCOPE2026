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

A minimal zero forcing set represents exactly \(k-1\) legs. Before the center turns blue, each represented leg must use one of the three inclusion-minimal path seeds: an eligible root singleton, a leaf singleton, or an adjacent nonleaf pair. Trigger necessity and the shallow-pair redundancy rule give the noncentered classification; center-containing minimal sets force precisely the stated root pattern. Maximizing the number of doubled deep-pair legs and comparing with the centered extra vertex yields the formula. An independent brute-force reconstruction over 281 spider profiles of order at most 10 matched every minimal set and the upper formula exactly; this finite check only corroborates the symbolic proof.

## originality

PASS

Fresh comparison confirms substantial prior spider work but not the claimed full classification. Brimkov–Carlson explicitly construct the adjacent-pair mechanism and classify a special spider family; the well-forced literature classifies the equality boundary. Resultary found no prior all-leg-profile upper formula or all-minimal-set theorem.

## value

PASS

The upper zero forcing number is a named invariant introduced specifically to measure the largest inclusion-minimal forcing set, and spiders are a canonical family in that literature. The exact value for every arm profile plus all minimal sets materially refines prior special constructions and the binary well-forced boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
