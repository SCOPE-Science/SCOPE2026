---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For each prime p and power p^e, the set S_e of indices with p^e dividing U_j is upward-closed under multiples and gcd-closed under strong divisibility; its least index r_e divides every element. The ranks form a divisibility chain as e increases. Thus v_p(U_j)=sum_e 1[r_e|j], and the factorial quotient valuation is sum of nonnegative carry indicators floor(n/r_e)-floor(k/r_e)-floor((n-k)/r_e), proving all generalized binomials integral. Levels with r_e=n contribute one to every interior column. Setting k_p to the largest proper rank r_e<n dividing n, or 1 when absent, kills every other carry level because ranks above k_p are its multiples and n modulo such ranks is zero or a positive multiple of k_p. Therefore the minimal valuation equals the number of levels r_e=n, which is the valuation jump in lcm(U_1,...,U_n). The known strong-divisibility factorization gives the Mobius product. Independently evaluated complete interior row gcd and lcm jumps for the first 20 rows of ordinary, Gaussian q=2,3 and Fibonacci sequences. These finite cases corroborate, not replace, the all-sequence proof. The minimizing k can depend on p.

## originality

PASS

The successive-lcm-factor/Mobius formula is established by Nowicki and is explicitly credited; the separately claimed content is its identification with the unweighted gcd of all interior generalized-binomial entries, plus an explicit prime-wise minimizer. Bousla–Farhi (2020) proves an entire-row LCM and a *weighted* row gcd, which do not algebraically equate to the unweighted interior gcd without another argument. Ando–Sato (1991, 1999) addressed exactly the same strong-divisibility generalized coefficients and gcd/lcm problems, but full chapters were inaccessible; abstracts and available secondary descriptions do not identify this precise row-content theorem. That is a significant unresolved priority risk, not a proof of distinctness. Best-of-knowledge PASS is qualified by it.

## value

PASS

The theorem supplies an exact universal row-content invariant and an explicit minimizing interior column for every prime for arbitrary positive strong-divisibility sequences, a natural meeting of binomial integrality, arithmetic row gcds and primitive sequence factors. It extends familiar binomial/Fibonacci/Gaussian special cases to all such sequences without recurrence or normalization hypotheses. The constructive carry-rank proof explains the arithmetic mechanism, rather than simply retabulating known specific rows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
