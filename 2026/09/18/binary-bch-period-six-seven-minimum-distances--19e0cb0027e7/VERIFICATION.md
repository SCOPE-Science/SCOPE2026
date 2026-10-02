---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
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

Read assigned RESULT and exact C++ source blob 5252ae27d29e4dae35e13fed6b35d1d9e271d079, compiled the original source using WSL g++ 13.3 -O3, and reran it: all irreducibility, primitive/order, relation, coset, and exhaustive tests returned true, VERDICT=PASS. Source-code inspection confirms the 8,650,720 unordered pairs from nonzero coordinates 1..4160 are all generated; for each syndrome pair it binary-searches its complement to v_0 and rules out disjoint pairs. Every hypothetical weight-five cyclic word can be shifted to include coordinate 0, then its other four distinct coordinates partition into such complementary disjoint pairs, so this is exhaustive rather than sampling. The displayed six-support vector vanishes at beta,beta^3, and the BCH bound excludes weights below five, proving d=6. Cyclotomic cosets of 1 and 3 are disjoint size 18, hence dimension 4125. For s=7, exact field arithmetic confirms theta order 16513 and five distinct exponents with zero first/third power sums; cosets size 21 give dimension 16471. For s=7k, 3 does not divide k, N_s is divisible by N_7 because 2^s modulo N_7 is 2^7 or 2^14; the order-16513 subgroup embeds since 21 divides 3s. The lifted five-support word has distinct exponents and meets the BCH roots, proving d=5 for every stated s. The lift from a chosen primitive N_s root onto the designated theta is valid by CRT avoiding prime divisors of N_s/N_7.

## originality

PASS

Read the full relevant Wang--He--Yi--Zheng primary text including Section III-B Lemma 16 and its complete two-case proof, not merely the abstract. Its exact distance-five condition is s=2 or 4 modulo 6, or 5|s and 15 does not divide s. This does not cover s=6 or odd values such as s=7,49,77,91; even 7-multiples with s=14 are covered by the earlier 2 mod 6 class, so the proposed class honestly overlaps rather than falsely claiming all-new parameters. Exact targeted web and Resultary searches found the same assigned item but no distinct table/theorem giving [4161,4125,6] or the entire seven-family. Best-of-knowledge caveat remains for poorly indexed code tables.

## value

PASS

Exact distance for a natural norm-one BCH family determines error-correction capability where the designed bound is not tight (s=6), and the new period-seven subgroup witness adds an infinite sufficient class beyond the immediately preceding paper. The finite [4161,4125,6] fact is naturally motivated before computation and not a parameter substitution from its existing conditions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
