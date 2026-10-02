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

The equivalence between binary 2-frameproof codes, (2,1)-separating systems and general-position sets in Q_8 is exact. A size-ten witness is explicitly checked. For any hypothetical eleven-word code, minimum distance 1 is impossible and minimum distance at least 5 contradicts the coordinatewise pair-distance sum bound, leaving d=2,3,4. After translating/permuting a closest pair to 0^8 and 1^d0^{8-d}, the stabilizer S_d x S_{8-d} makes (alpha,beta) a complete orbit invariant for a third word; the verifier enumerates every feasible orbit. Its branch-and-bound candidate graph enforces distance and triple separation against the base pair, then tests the full three-word condition at every recursive extension; greedy coloring is used only as a valid clique upper bound. Every orbit has maximum at most ten. The finite computation is exhaustive after a proved symmetry reduction, not a timeout-based impossibility claim.

## originality

PASS

Korže--Vesel's 2023 full article identifies the hypercube problem with (2,1)-separating systems and says their computed values are exact only through dimension seven; dimensions above seven are reported as lower bounds. A 2026 general-position survey likewise records exact hypercube values only through Q_7. Resultary search found no earlier exact Q_8 / binary length-eight result. Thus the matching upper bound at Q_8 survives the prior-implication comparison.

## value

PASS

This closes the first hypercube dimension beyond the previously certified exact range and simultaneously fixes a standard finite separating/frameproof-code parameter. An exact finite cutoff obtained by a symmetry-complete certificate is a natural motivated classification, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
