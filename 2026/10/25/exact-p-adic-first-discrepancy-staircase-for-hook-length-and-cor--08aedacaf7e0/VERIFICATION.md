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

The reproducible finite checker is `verify.py`, using Python 3 and its standard library only. It calculates the coefficients of powers of the Euler product by the exact divisor-sum logarithmic-derivative recurrence and constructs the core series independently as the convolution of an Euler power evaluated at \(q^t\) with the ordinary partition generating function. In small degrees, it also checks the Euler-power recurrence against direct multiplication of the integer-binomial Euler factors.

Executing `python3 verify.py` returned `VERIFY_OK 14 parameter cases` for fourteen prime-power parameters. The checks cover the coefficientwise congruence, the first failure index for every inspected modulus, and the asserted leading residues at all distinguished indices in those finite instances.

The analytic argument does not depend on enumeration: the universal result rests on characteristic-\(p\) Frobenius and elementary power lifting in \(\mathbb Z[[q]]\). The checks do not establish novelty or independent validation, and the code does not exhaust infinitely many parameter choices.
