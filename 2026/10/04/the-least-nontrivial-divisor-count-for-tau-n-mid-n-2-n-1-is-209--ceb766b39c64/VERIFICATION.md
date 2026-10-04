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
The finite arithmetic replay is `verify.py`.

It checks:
- among primes \(3,5,7,11,13,17\), only \(11\) admits a quadratic-residue root of \(x^2+x-1\);
- the divisor-count shapes for \(11\) and \(121\) force residue \(1\) modulo \(11\), contradicting the required divisibility;
- the explicit congruences modulo \(11\) and \(19\) for the \(209\)-divisor family;
- several concrete primes \(p\equiv4\pmod{19}\), including the first family member \(23^{10}31^{18}\).

The proof of infinitude uses Dirichlet's theorem on primes in arithmetic progressions. The code does not replace that theorem.
