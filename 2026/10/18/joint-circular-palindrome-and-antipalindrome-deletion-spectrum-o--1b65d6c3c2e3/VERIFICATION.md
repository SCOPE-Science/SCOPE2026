---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

A binary order-five de Bruijn cycle is an Euler tour of the 16-vertex/32-edge order-four de Bruijn directed graph. Each local vertex has two incoming and two outgoing edges, hence 2 choices of pairing; all 2^16=65,536 local pairings exhaust all Euler tours via the one-cycle test, uniquely rooted at 00000. This gives exactly 2048 rotation classes. For every one of the 32 cuts per class, independent recurrence on subintervals gives optimal palindromic subsequence length when endpoints match and antipalindromic length when endpoints differ, with correct empty and singleton cases. A fresh separately written C++ exhaustive enumerator (not the submitted verify.cpp or CSV) confirmed all 2048 cycles, all 65,536 rooted cuts, every one of the 20 joint frequency cells, exactly 19 occupied cells: A=26 row (4,16,284,52,32), A=28 row (52,80,860,180,136), A=30 row (12,16,192,44,24), A=32 row (8,2,44,10,0), 32 two-cycle and 496 four-cycle reversal/complement orbits. For this exact finite domain the enumeration is exhaustive, rather than an empirical extrapolation.

## originality

PASS

The preceding Guo–Shallit–Shur study treats palindromic/antipalindromic contiguous factors or conjugates, and Müllner–Ryzhikov treats general longest circular scattered-subsequence questions, not a complete order-five de Bruijn-conditioned joint distribution. Chang–Wang reverse-complement-symmetric cycles may cover the perfect antipalindromic boundary, explicitly excluded as a separately novel claim; they do not give the remaining joint cells. Best-of-knowledge PASS with risk of an older unindexed census.

## value

PASS

Order-five binary de Bruijn cycles form a canonical natural finite population of 2048 rotation classes; the complete two-observable deletion tradeoff and forbidden extremal pair distinguish circular palindrome and antipalindrome geometry that neither marginal or known perfect-boundary existence result determines. A finite classification can be valuable without an all-order formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
