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

# Reproducibility and verification

Run `python3 verify.py` with a standard Python 3 interpreter. It requires no third-party packages. The initial execution returned `PASS: 249 exact rational checks` and exhibited two distinct normalized positive triples with equal two-step return probability.

The checks use `fractions.Fraction` and exact factorial arithmetic. They cover the Bessel-log coefficient recurrence and its signs through order 12; generating-function identities, moment inversion, Newton identities and first-return renewal equations in dimensions 2–8; exact nonsingularity of the relevant generic Jacobian minors; and an explicit three-dimensional lower-cutoff counterexample. Failure of any asserted equality or inequality raises an exception and prevents the PASS message.

The finite computations do not establish mathematical truth for all dimensions or continuous weights. Generality follows from the analytical proof in `RESULT.md`: the Bessel differential equation, strict beta-integral monotonicity of the remaining polynomial coefficient, and the rank/implicit-function theorem argument. No formal proof assistant or independent validation has been used. These scientific records do not establish priority beyond the cited literature comparison.
