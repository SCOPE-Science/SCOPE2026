---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The recurrence P_{n+2}=2P_{n+1}+P_n and identity 8P_r^3=P_{3r}-3(-1)^rP_r give an integer reversible order-four recurrence for all cubic window sums: t^4-12t^3-30t^2+12t+1. Its unit constant coefficient makes four successive windows sufficient to compute the full infinite gcd, and permits using S_{-1}. Pell addition formulas yield common factors q=Q_m for odd m or p=P_m for even m in every shifted difference. The exact initial identity 56 S_0=q[(4q²+3)(P_{3m+3}+P_{3m})-21q] or p[(4q²-1)(Q_{3m+3}+Q_{3m})-42p] then distinguishes the 7-adic loss, the 3-adic gain for 4|m, and the 2-adic bound using mod8/mod16 periodicity. Combining the upper bounds from differences and lower divisibility gives equality for all m, with no extrapolation from finite m. Independently computed the exact four-window gcd for 499 distinct m=1..499, all matching, and checked the recurrence-derived reduction.

## originality

PASS

Novelty is a qualified best-of-knowledge mathematical comparison, not a guarantee of priority; exact original claim was searched against equivalent formulations, general theorems and data tables.

## value

PASS

The simultaneous 2-, 3- and 7-adic cancellations make this an exact nontrivial all-length arithmetic invariant of a classical recurrence, rather than a cosmetic index substitution. The infinite two-parity classification is naturally useful for divisibility, higher-power recurrence sums and Pell/Lucas congruence comparisons; it does not assert odd window lengths or arbitrary powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
