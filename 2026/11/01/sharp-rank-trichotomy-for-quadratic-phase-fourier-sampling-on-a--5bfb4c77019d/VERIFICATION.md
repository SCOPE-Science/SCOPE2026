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

# Verification record

The analytic reconstruction checks the zero-row Schur complement, the full multiplicative-character basis and inversion sign, the coprime-cyclotomic-field argument, and both zero-parameter boundaries. In the nonzero-linear branch the unique nonzero fiber is explicit, \(u_0=-a/(2b)\), \(h(u_0)=-a^2/(4b)\) if \(b\ne0\); when \(b=0\) use the bijection \(u\mapsto au\). Every required claim follows without numerical interpolation. The half-rank branch uses a prime Fourier minor, not a computed minor enumeration.

`checker.py` was executed successfully with NumPy: 222 coefficient pairs were tested at primes 3, 5, 7, 11, 13, 17, and 19, with exact finite-field singleton-fiber assertions and numerical singular-value ranks. The tests are not exhaustive over all primes, provide no certified numerical conditioning bounds, and do not replace the proof.

Source overlap was checked against published records and the accessible primary papers described in `AUDIT.json`; coverage cannot be ruled out in inaccessible older literature. No independent audit or external validation was performed.
