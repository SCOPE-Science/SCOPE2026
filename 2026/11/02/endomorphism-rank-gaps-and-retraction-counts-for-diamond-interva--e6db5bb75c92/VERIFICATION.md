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

All elements are square-zero under multiplication, so f(0)=0. Flat addition then forces two distinct source elements to have distinct nonzero image values. If f(w)=w, products force simultaneous permutations of n matching pairs; if f(w)=0, the nonzero images of short intervals are exactly partial injections into zero-product subsets choosing at most one endpoint of every pair, optionally w. Their subset enumerator is (1+2z)^n(1+z), with assignments (2n)_m and image size m+1; units contribute n!. Idempotents either identity or projections onto pairwise zero-product short subsets: 3^n+1. Independent full operation-table enumeration n=1,2 confirms n=2 rank vector (1,20,96,96,0,2), idempotents ten, total 215. The proof, not this census, establishes all n.

## originality

PASS

Gao–Ren 2025/2026 define flat graph semirings, including the isomorphic directed-matching object, and analyze 3-nilpotent variety structure. Gao–Zhou 2026 define interval semirings and study generated identities/varieties. Neither primary passage inspected provides the full endomorphism rank/retraction count. Older general semigroup transformation enumeration might imply this easy-to-state matching subclass; not found in targeted Resultary or source search, acknowledged as priority risk.

## value

PASS

S_n contains a canonical six-element generator of a studied bounded-height ai-semiring variety. Endomorphism ranks, rank gaps and idempotent retractions are natural monoid invariants; the formula classifies these for an entire branching family rather than isolated examples, including exactly missing rank five for S_2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
