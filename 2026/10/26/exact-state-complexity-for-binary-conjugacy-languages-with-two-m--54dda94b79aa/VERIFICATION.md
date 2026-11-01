---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For the finite language C(w) of distinct conjugates of w=10^a10^b, a complete minimal DFA has one dead quotient and nonempty quotients segregated by prefix length and number of consumed ones. Let ell=min(a,b), h=max(a,b), d=h−ell. All-zero prefixes contribute h+1 quotients, two-one prefixes another h+1. One-one prefixes 0^i1 0^j are feasible exactly in the union [0,ell]×[0,h] ∪ [0,h]×[0,ell], cardinality (ell+1)(2h−ell+1). Quotient collisions can only pair singleton A-only and B-only continuations, requiring i'=i+d, j'=j−d in min(d,ell+1)² distinct disjoint pairs. Thus the exact Myhill–Nerode quotient count is (2ell+4)h+4−ell²−min(d²,(ell+1)²), including equal gaps and adjacent ones. Independently enumerated complete right-quotient sets for 91 pairs 0≤a≤b≤12; every result matched. This checks finite instances only, with all-parameter proof from the rectangle and collision argument.

## originality

PASS

Best-of-knowledge PASS for a complete per-word two-marker conjugacy state-complexity formula. Jirásková–Okhotin 2008 addresses worst-case complexity of cyclic shift as an operation on arbitrary regular languages; Gabric–Holub–Shallit 2019 studies global maxima and generalized de Bruijn equality, not this fixed two-marker quotient collision census. Known descriptional-complexity upper bounds do not determine the exact grid-collision regime.

## value

PASS

Exact complete DFA state count over every binary two-one cyclic-word language is a natural sharp descriptional-complexity classification. It tracks the nontrivial quotient mergers at h−ell=ell+1 and covers periodic degenerate equal gaps, supplying information not entailed by global extremal bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
