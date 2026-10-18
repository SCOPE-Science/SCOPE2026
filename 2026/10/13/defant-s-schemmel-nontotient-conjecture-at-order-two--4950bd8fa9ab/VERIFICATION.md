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

Defant Lemma 2.2 reduces 3^alpha p being a second Schemmel nontotient for all alpha to p != 3^t+2 and all 3^t p+2 composite. Independently checked the ACTUAL ten (exponent residue, order, prime q, progression residue c) rows: all 10 q prime, all multiplicative orders exactly asserted, 48 of 48 exponent residues covered, every modular 3^a*c+2 congruence zero, product modulus M=1620742097628261335, CRT solution C=206033543146003779 and gcd(C,M)=1. The q=41 row forces 3^t !=11 mod41 for every t. Dirichlet supplies infinitely many primes p>M in the coprime progression, each yielding proper divisors of 3^t p+2 for every t. This is a genuine infinite proof, not a finite search or an assertion about arbitrary r.

## originality

PASS

Defant, arXiv:1412.3089, Lemma 2.2 and Conjecture 4.1, explicitly poses all r with r+1 prime. Its Theorem 2.1 requires r+1 non-Mersenne and excludes r=2 because 3 is Mersenne. The submitted cover closes this named excluded case rather than restating Defant result. Indexed published records and Resultary hits discussed other totients or parameters, not this exact all-exponent coprime prime progression; unindexed prior solution remains possible.

## value

PASS

This resolves the first Mersenne-excluded case of a concrete published conjecture by an explicit ten-class covering construction, producing infinitely many primes and all exponent rays. This is a motivated substantive number-theoretic advance, not mere recomputation of finite Schemmel values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
