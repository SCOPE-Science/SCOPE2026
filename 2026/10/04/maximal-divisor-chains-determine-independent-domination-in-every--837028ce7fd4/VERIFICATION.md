---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The proof reconstructs for every composite n. Gcd cells are independent and two distinct cells are completely adjacent exactly when their divisor labels are incomparable. Independence therefore makes the selected labels a chain; selecting only part of any chosen cell leaves the unchosen same-cell vertices undominated, so chosen cells must be whole. Such a full-cell chain dominates exactly when it is maximal in the nontrivial proper divisor poset. Adding 1 and n turns each maximal chain into a saturated divisor chain, hence into a distinct ordering of the prime multiset. The cell-size sum gives the stated polynomial. For adjacent distinct primes a<b before a fixed suffix T, the swap replaces phi(bT) by phi(aT), and Euler's product formula gives phi(aT)<=phi(bT) in all divisibility cases; bubble sorting therefore proves the descending/ascending extrema. The geometric totient sums yield the displayed closed formulas. The bundled finite enumeration was inspected only as corroboration.

## originality

PASS

Originality passes. Rather's 2024 complete primary article gives formulas only for selected factorizations and explicitly closes by saying the general-n polynomial remains difficult. The audited maximal-chain bijection resolves that stated general case, gives the exact number of independent dominating sets, and identifies both extremal exponents. The accessible 2026 follow-up still advertises biprime, triprime and prime-power-times-prime regimes rather than an arbitrary composite theorem.

## value

PASS

The invariant was previously computed only for selected factorizations, with the source explicitly identifying the general case as difficult. A complete all-composite structural classification, exact enumerator and extremal formulas are a natural resolution of that gap and give reusable information beyond another finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
