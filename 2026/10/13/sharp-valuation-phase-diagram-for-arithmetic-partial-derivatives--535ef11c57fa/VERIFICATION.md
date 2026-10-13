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

The proof was replayed algebraically from the defining identity \(D_p(bp^m)=bmp^{m-1}\) for \(p\nmid b\). The decisive boundary check is that \(m\ge2p\) is forward invariant under \(m\mapsto m-1+\nu_p(m)\), including \(p=2,m=4\); hence each subsequent magnitude ratio is at least two.

The bundled `verify.py` performs finite regression checks for every prime through 97, six signed coefficients prime to the active prime, all exponents below \(2p\), and exponents from \(2p\) through \(2p+30\) in the divergent regime. Forty successive steps are checked for each sampled divergent orbit. The recorded run completed with `VERIFY_OK` and 786314 assertions.

Finite regression is not used to infer the infinite theorem. The proof in `RESULT.md` establishes all primes, coefficients, and exponents.

Scope limit: this verification concerns integer inputs for a single arithmetic partial derivative. It does not verify the full arithmetic derivative, multi-prime arithmetic subderivatives, or general local-field dynamics.
