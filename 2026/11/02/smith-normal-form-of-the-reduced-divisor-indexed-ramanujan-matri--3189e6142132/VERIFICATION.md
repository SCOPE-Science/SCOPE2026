---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For all n>=2 and rows/columns indexed by divisors d,e>1, Ramanujan gcd/Mobius identity and integral divisor-incidence matrix E give integral equivalence B_n~D-1b^T (b_d=-mu(d)). Over the local DVR Z_(ell), generators x_d obey d x_d=w=sum b_d x_d. Eliminating ell-unit divisors then higher ell-power generators gives the precise exponent multiset: for ell|n=ell^a m, T=tau(m), h=v_ell(phi(m)), start T copies 1..a, remove one 1 and raise one a to a+h if h>0; for ell outside n only v_ell(phi(n)) survives. Padding and multiplying sorted local exponents yields full integral Smith factors; determinant and mod-ell ranks follow. Independent implementation of Ramanujan sums as sum_{t|gcd(d,e)} t mu(d/t), with SymPy Smith normal form computed separately, matched the formula for every modulus n=2..100 (99 cases), including primes dividing phi(n) but not n. The finite test is independent corroboration of the infinite local module proof.

## originality

PASS

Schlage-Puchta 2021 computes the determinant for the full divisor-indexed Ramanujan matrix; it is not the reduced d,e>1 submatrix and gives no integral SNF. Fowler–Garcia–Karaali and Shareshian–Sundaram present established supercharacter and full-divisor Ramanujan tables. The known squarefree reduced specialization is acknowledged. The assessed all-moduli local exponent recipe is strictly finer than any determinant or rational rank statement.

## value

PASS

The complete invariant-factor classification of a naturally arithmetically indexed integral matrix captures torsion group structure unavailable from determinant or modular ranks alone. It covers every composite modulus and gives explicit boosted local exponents, so it is an independently reusable exact arithmetic fact rather than a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
