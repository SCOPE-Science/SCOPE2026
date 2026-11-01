---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Q=(10^6-1)/9=111111=3*7*11*13*37, and R_(m+6)-R_m=10^m Q give rigorous periodic reduction for every positive padding m and t modulo 6. Prime-wise inverse residue roots modulo the five prime factors produce an exact OR-of-primes test for each of 24 digit/length pairs. Independent full enumeration of 6Q=666666 modular states using both direct arbitrary-precision gcd and CRT-root logic reproduces (60,10121,111,10121,60,10101) and the specified div3/div11 counts. For nonmultiples of 3, digit-3/9 reduced Q/3 candidates and digit-1 obstructions exclude odd-length candidates and force 11 for even t. Since all lengths/centers map into the full finite state space, this is a complete finite certificate, not finite sampling extrapolated to an infinite assertion.

## originality

PASS

Best-knowledge PASS for the all-residue six-period fixed-Q classification, not the known symmetric padding conjecture or Wu 2015 individual covered examples.

## value

PASS

The divisor set of 111111 is a canonical six-period repunit covering mechanism used in the first symmetric-padding counterexamples. A complete modular classification and strict 3/11 obstruction characterize the limitation of that natural proof method, including twenty exceptional even-digit classes. This is an exact natural finite-state invariant with unbounded conditional scope, not a prime-existence claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
