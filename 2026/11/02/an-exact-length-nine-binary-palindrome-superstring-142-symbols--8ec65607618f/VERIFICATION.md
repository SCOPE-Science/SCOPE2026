---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For the exact set of 32 binary length-nine palindromes, use symmetric minimal suffix-prefix overlap shifts c_ij. Any circular containing word gives a tour of distinct chosen palindrome start positions, so its length bounds below a Hamiltonian-cycle overlap cost. Independently regenerated all 496 unordered pair shifts from 32 explicit palindromes, verified symmetric costs, sum of integer vertex potentials 81 and exactly seven positive edge deficits summing 20. Since a Hamiltonian cycle uses degree two at each vertex and any unordered edge at most once, its cost is >=2*81-20=142. Independently scanned all 134 non-wrapping windows in the supplied 142-character binary witness and found all 32 distinct palindromes; thus linear and circular minima both equal 142. This is a complete finite dual certificate, not solver optimality or partial search.

## originality

PASS

Best-of-knowledge original as a certified optimal 142 length-nine all-palindromes superstring, not as first discovery of an upper-bound construction. OEIS A330022 explicitly records a(9)<=142 as a greedy upper bound and says it is probably tight, rather than furnishing a matching lower bound. General shortest common superstring with reversals concerns a different target set and does not supply this exact lower-bound certificate.

## value

PASS

The smallest unresolved exact palindrome-cover length at order nine is a natural discrete extremal invariant explicitly listed as an upper bound. An independently checkable dual feasible potential certificate proves exact optimality, converting an existing construction into a sharp benchmark for short-superstring algorithms. Its fixed finite nature is mathematically motivated by the exact target family and tabulated open boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
