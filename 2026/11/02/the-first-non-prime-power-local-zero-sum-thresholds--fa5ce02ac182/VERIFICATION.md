---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Coprimality to 6 means a unit modulo 36, and gcd(s,36)=6 gives precisely the residues 6 and 30. Multiplication by a unit preserves that gcd and subsequence length; after normalization and sorting, any counterexample is a nondecreasing multiset starting with 1. Each recurrence state records sums of exactly j selected positions; the update takes old j−1 sums to account for inclusion of the new position, so repeats of a residue are handled correctly, and a pruned prefix cannot have a bad extension. An independent 36-bit-mask search with no depth cap reproduced all 3944 admissible prefixes, with counts 1,10,47,141,322,560,638,639,633,566,315,72 by length and no length-13 state. For the lower bound, d+13e with −5≤d≤5 and e∈{−1,0,1} cannot equal ±6 modulo 36, even without any length restriction. Thus 13 suffices for the short version and is necessary for the unrestricted version, proving both equalities.

## originality

PASS

The prior exact-gcd problem and the twelve-term witness are verified in Gao–Jiang–Mu. The supported distinct claim is the matching upper bound at n=6. The strongest numerically similar same-day finding and the published weaker-predicate theorem neither guarantee a sum with gcd exactly 6 nor imply this upper bound.

## value

PASS

The first modulus with two distinct prime divisors is the natural boundary of the known prime-power theorem and the first instance of the cited problem, not an arbitrary experimental choice. A sharp upper bound for the more restrictive short-subsequence invariant shows that the general lower construction is attained already at this boundary and settles both thresholds there.

The dated certificate retains the supplied scientific assessment, sources and limitations.
