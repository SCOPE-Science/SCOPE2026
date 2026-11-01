---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For a six-periodic positive word a_i, every output is a 5-adic unit. The exact B_i=[[-1,5^e_i],[1,0]] product has eigenvalue 1, hence tr(P)=1+det(P); independent symbolic multiplication reproduces the claimed 6 singleton + 9 pair + 2 triple trace polynomial. Reduction modulo 5 over all 63 nonzero exponent-support patterns leaves only 13 patterns, precisely the rotations of 001011, 001101 and 111111. The all-positive case contradicts 6/5^5+9/5^4+2/5^3<1 after division by the product. For the remaining cases, the two exact multilinear equations f/g(A,B,C)=0 have f(5,5,5)=g(5,5,5)=0 and all partial derivatives negative for A,B,C>=5, forcing all three actual divisions to be by five (not higher powers); this is the essential unbounded step. Linear recurrences for each support have rank five and unique positive rational rays with primitive representatives as claimed. Exact independent substitution verifies both six-cycles. Mod-two Fibonacci dynamics excludes a positive primitive period-three orbit and periods not divisible by three. This is an all-positive classification; the finite support enumeration alone is not an arbitrary-entry proof.

## originality

PASS

Best-of-knowledge comparison of the complete asserted mathematical implication against actual primary material read and documented searches. Original 2014 primary literature lists two examples but explicitly does not prove completeness.

## value

PASS

Exhaustively classifies the first possible positive cyclic stratum of the five-free Fibonacci map, an object originally known from two examples but not an all-starting-pair theorem. Excluding arbitrarily large six-cycle entries and higher five-adic division exponents is a nontrivial exact structural result; no longer-cycle classification is suggested.

The dated certificate retains the supplied scientific assessment, sources and limitations.
