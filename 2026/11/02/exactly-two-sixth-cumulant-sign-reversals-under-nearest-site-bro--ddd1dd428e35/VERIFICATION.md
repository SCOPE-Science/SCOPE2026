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

# Reproduction and limits

Run `python3 CHECK.py` in this directory; `sympy` and `mpmath` are required. The checker establishes the exact sixth-coefficient Laurent-polynomial identity from the implicit renewal equation, the finite exact coefficient signs and inequalities used for the infinite positive tail, and a rational bound proving the crucial negative value \(N(1)<0\). It also solves the implicit tilted renewal-root equation independently at three resetting rates and compares numerical sixth-order expansions. The expected output is `PASS 30 checks` and two approximate threshold pairs.

The uniqueness of the two transitions is an analytical argument in `RESULT.md`, not the result of sampling a finite parameter grid. Approximate decimal thresholds are not certified to every displayed digit. The proof concerns the asymptotic sixth cumulant of actual single-particle position and not finite-time values, first-passage observables, nonuniform arrays, or a different resetting mechanism.
