---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Write E(n)=sigma(n)-n-1 (nonunit proper divisors) and cototient C(m)=m-phi(m), so A=E(n)+C(n+2)-1. If n composite and A<5, E<=4; n=p² forces p=2,3 while non-square prime-factor pair p and n/p gives E>=2+3=5. Directly n=4 has A=5, n=9 A=3. Prime n=2 gives A=1. Odd prime n implies m=n+2 odd; for composite m with A<5, C(m)<=5 and C(m)>=m/r>=r for least prime divisor r; r=3 gives m=9 (not 15, C15=7), r=5 gives m=25; hence n=7,23. If m prime, A=0 exactly twin primes. Independent direct exact sigma/totient values for every 2<=n<10000 agreed.

## originality

PASS

The exact OEIS A078119 records shifted expression, nonnegativity and twin-prime zero fiber plus first appearances of small values, but the inspected entry does not state uniqueness of all four positive fibers or universal sharp 5 floor. Pomerance/Yang study separate unshifted components, not this coupled shifted function. The theorem upgrades initial numerical terms to unrestricted classification.

## value

PASS

A(n) is an established natural arithmetic sequence combining divisor sum and shifted totient, with an unresolved twin-prime zero fiber. Exact *entire* first four nonzero fibers and a sharp stability gap provide a motivated number-theoretic classification that prevents sparse database terms from being mistaken for an unbounded theorem. Its proof is elementary and its range narrow, but the exact unbounded cutoff is mathematically substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
