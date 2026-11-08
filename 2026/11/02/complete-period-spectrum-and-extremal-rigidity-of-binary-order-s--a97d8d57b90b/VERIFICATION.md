---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The 128 seven-bit edges of binary de Bruijn graph have 16 palindromic forbidden edges and 56 nonpalindromic reversal pairs. A valid necklace bijects with a directed closed trail containing at most one edge per reversal pair, and its distinct windows imply primitivity. Depth-first recursion from all eligible start states is exhaustive because each move marks a previously unused pair; crucially root revisits do not terminate extension. Two independently implemented exhaustive enumerations use different rooting rules. Independent compiled C++ search in this run reproduced all 29 positive-length table counts, total4788, maximal336, 90 symmetry orbits and all extremal local frequencies. This is an exhaustive finite proof for n=7 only, not a general theorem for other orders.

## originality

PASS

The maximum length 36 is already known from Mitchell and the Gabrić–Sawada constructions; these are specifically excluded from novelty. The primary CPM2024 paper supplies construction and bound, not a count of every orientable closed cyclic trail. Mitchell abstract reports maximum but not the full period profile; its uninspected body and older 1993 paper leave explicit priority risk. The exhaustive period census and extremal rigidity are distinct exact claims.

## value

PASS

The enumeration is a complete natural finite classification at first nontrivial near-extremal order 7; the full length spectrum and 336 extremizers refine the single known maximum, and the three-window rigidity constrains candidate orientable sequence constructions and benchmark search algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
