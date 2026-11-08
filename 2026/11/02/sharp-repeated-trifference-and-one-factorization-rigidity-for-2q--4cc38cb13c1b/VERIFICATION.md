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

For every integer q>=3 with exactly 2q distinct q-ary codewords of length 2q-1, each coordinate separates at most e3(a_1,...,a_q)<=8*C(q,3) triples; Maclaurin/AM-GM is sharp only at symbol occupancies 2 each. Averaging gives min trifference <=2q-4. At equality every triple is nonseparated in exactly three coordinates, so for induced matching edge counts m_uv, m_uv+m_uw+m_vw=3 and sum_w m_uw=2q-1. Summing over w yields (2q-4)(m_uv-1)=0, whence every pair occurs once: all coordinate matchings form a one-factorization. Odd-modulus cyclic round-robin construction is a converse for all q. For q=3 explicit K6 enumeration gives 15 matchings, 6 factorizations in one relabeling orbit and 6*5!*(3!)^5/6!=7776 fixed-position unlabeled-message codebooks. The classification is not a claim about maximum code size for arbitrary q or single-separation codes.

## originality

PASS

The numerical trifference T(5,2)=6 and the underlying generalized multiple-separation setting are pre-existing results. The claim adds equality-case one-factorization equivalence for every q and a complete ternary optimizer census. No inspected source implies these particular structural results, but older perfect-hash and edge-design classification literature may implicitly contain them.

## value

PASS

A natural sharp boundary in q-ary repeated triple separation becomes a complete combinatorial structure theorem; exact optimizer census and equivalence classification give useful information not supplied by a maximum cardinality alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
