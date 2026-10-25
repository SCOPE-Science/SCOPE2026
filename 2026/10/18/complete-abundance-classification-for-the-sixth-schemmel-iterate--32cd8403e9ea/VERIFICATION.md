---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Let t=p-6 for p>6. Immediate deficiency holds if p<=5 or a small divisor 3 or 5 divides t. Exact elementary trajectories show primes 7,13,17 deficient for all powers and 19 abundant only at exponent1: D6(19^a)-19^a=(53-17*19^(a-1))/18. For p>=23 with gcd(t,15)=1, h=L6(t) is >=7 except t=77 (p=83): if h<7, the possible prime factors 7,11 and absence of repeated factors force t in {1,7,11,77}. For t>=37, th>=7t>6(t+6), while for 17<=t<37, t is prime and t(t-6)>6(t+6). Thus D6(p^a) exceeds p^a by the first two iterates for all a>=1, except p83: D6(83)=82, and for a>=2 D6(83^a)=83^a-113*83^(a-2). All inequalities strict: no perfect prime powers. Independently factored every p<=1000, exponents1..8: exactly 961 abundant, 383 deficient, no equality, reproducing special 19^2 and 83^2 cases. This is bounded corroboration; the rough-cofactor lemma proves all p and a.

## originality

PASS

Defant's 2015 primary article defines D_m and Theorem 18 proves infinitely many primes whose every power is abundant for each even m. Its full text, especially pages 7-10, does not furnish the exact sixth-parameter prime-power dichotomy or isolated primes 19 and 83. The present all-prime classification is strictly sharper than that existence theorem. OEIS trajectory sequences named in the record concern other m; unindexed tables remain possible.

## value

PASS

Complete sign classification for a natural family singled out by Defant's Schemmel iteration, including an isolated 83 exception and 19 exponent transition, is a mathematically motivated exact boundary. It is not simply reprinting known values or checking a tiny slice: a structural lemma proves the infinite prime and exponent range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
