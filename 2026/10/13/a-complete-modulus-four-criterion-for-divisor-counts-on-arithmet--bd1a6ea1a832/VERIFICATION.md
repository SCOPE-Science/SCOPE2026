---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For p^a||A with valuation e_p(B)<a, exponent e_p is fixed. Multiplicativity gives J|tau. If J odd, all forced exponents are even; the explicit auxiliary square E (fixed exponents e_p and 2a at nonfixed p|A), CRT and Dirichlet yield a prime q outside E with E*q=B (mod A), so tau(Eq)=2 (mod4), disproving universal divisibility. If J=2 (mod4), exactly one forced exponent is 1 (mod4), all other forced exponents even; a term with tau=2 (mod4) is exactly p*t^2, giving the stated solvability iff. For A=8p^2,B=8beta+1, p||B supplies p-1 candidates; odd t has t^2=1 (mod8), so p!=1 (mod8) precludes exception, otherwise half the units fail quadratic solvability mod p. This proves cardinality for all odd primes; independently checked all A<=42 against positive terms and p=109 exact 108, with direct finite checks distinguished from infinite proof.

## originality

PASS

The comparison must use exact statement implications: Merca 2022 Conjecture 2 is a conjecture and predicts (p-1)/2 if p-1 not cubefree, while the new p mod8 formula refutes that for p=109; its Theorem 3 proves p=3,5 only. General arbitrary-A progression iff goes beyond Merca prime-square families. Resultary published totient and sum-of-divisors records are different arithmetic functions; neither controls divisor-count tau. No stronger verified universal modulus-four tau progression theorem found in inspected primary material.

## value

PASS

This is an effective full classification for arbitrary arithmetic progressions of a classical multiplicative function modulo four, and settles a named 2022 counting conjecture by a structural quadratic congruence obstruction. The p=109 discrepancy is not mere recomputation because the general criterion proves the full infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
