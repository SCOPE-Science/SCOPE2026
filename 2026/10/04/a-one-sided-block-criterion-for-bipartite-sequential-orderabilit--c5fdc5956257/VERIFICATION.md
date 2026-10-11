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

Fix an order of the A-vertices and concatenate their incident-edge blocks. Simplicity makes each B-side sequence independent of internal block permutations. At a left vertex of degree d, properness gives d! distinct local sequences while its d neighbours forbid at most d; d!>d for d>=3. The block choices are independent, proving the universal claim.

## originality

PASS

The primary 2026 paper publicly states the connected regular theorem only for degree at least 6 and its current problem page retains degrees 3,4,5. The closest published SCOPE theorem covers regular bipartite d>=5. Neither implies d=3,4 or the irregular one-sided criterion.

## value

PASS

The result resolves the bipartite part of the explicitly remaining low regular degrees and gives a stronger irregular one-sided criterion by a simple deterministic construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
