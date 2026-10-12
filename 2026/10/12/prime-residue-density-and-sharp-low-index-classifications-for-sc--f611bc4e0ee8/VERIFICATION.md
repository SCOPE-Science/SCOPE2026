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

# Verification details

Run `python3 verify.py` with Python 3's standard library. The script is self-contained. It reconstructs the prime-power Schemmel totient using exact factorization, iterates until the terminal value, and checks rational constants with `fractions.Fraction`. Its function for the empty continuation after reaching terminal \(1\) returns zero; this convention does not redefine the standalone published iterate sum at input \(1\), which is outside the theorem's domain.

A successful execution prints `FINITE_CHECKS_OK growth_lemma_instances=1565 prime_power_dichotomies=609 small_m_classifications=488 rational_c2=1/3 rational_c4=3/35 rational_c6=5/77`.

These computations test 1,565 instances of the prime-power lower-bound inequality, 609 examples of the two general sufficient/necessary branches, and 488 examples of the sharp \(m=2,4\) classification. Every infinite assertion depends on the five written proof steps, including the classical prime progression theorem. The checks do not establish uniqueness relative to all possible earlier literature, and independent validation has not been performed.
