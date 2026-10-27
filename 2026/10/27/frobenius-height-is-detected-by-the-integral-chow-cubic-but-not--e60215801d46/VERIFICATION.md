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

# Reproducibility and proof boundaries

Run `python3 verify_chow.py` in the same directory as this file (Python 3; standard library only). The checked result is:

`VERIFY_OK heights=9 unimodular_changes=104 prime_reductions=54`

The script checks that the cubic for nine sample prime powers has coefficients \((0,3,3q,0)\) in the ordered monomials \((a^3,a^2b,ab^2,b^3)\) and discriminant \(81q^2\). It checks 104 integral unimodular coordinate substitutions and the top intersection products \(h^2u=1\), \(hu^2=q\), and \(u^3=0\) in the displayed projective-bundle presentation, and tests normalized residue-field relations at six primes. These are exact integer operations, not floating-point approximations.

The universal assertions for all primes and all positive heights are proved symbolically in `RESULT.md`: exact locally free kernel, integral projective-bundle formula, discriminant transformation law, prime-field generator changes, and fiberwise point counts. Finite examples are not used to infer a universal statement. This verification does not address whether an earlier uninspected publication implicitly contains the same comparison.
