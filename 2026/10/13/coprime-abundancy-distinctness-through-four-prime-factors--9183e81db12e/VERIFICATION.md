---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The universal proof was reconstructed symbolically. The critical checks are:

1. If \\(I(n)=a/b\\) in lowest terms, then \\(b=n/\\gcd(n,\\sigma(n))\\), so \\(b\\mid n\\).
2. Equal abundancy for coprime \\(x,y\\) therefore has denominator \\(1\\).
3. Every input with \\(\\Omega(n)<4\\) can be multiplied successively by fresh primes to reach total multiplicity four while strictly increasing abundancy, so maxima at \\(\\Omega=4\\) dominate all lower layers.
4. Exact rational comparison of the five exponent partitions of \\(4\\) gives global maxima \\(31/16,5/2,91/36,14/5,96/35\\), all below \\(3\\).
5. Restricting to odd primes gives \\(121/81,16/9,403/225,208/105,768/385\\), all below \\(2\\).
6. Hence a nontrivial common integer abundancy must be exactly \\(2\\), and each input must be even, contradicting coprimality.

The bundled `verify.py` recomputes these maxima with exact `Fraction` arithmetic and performs a finite regression scan through \\(100000\\). The finite scan is not used to justify the infinite claim.
