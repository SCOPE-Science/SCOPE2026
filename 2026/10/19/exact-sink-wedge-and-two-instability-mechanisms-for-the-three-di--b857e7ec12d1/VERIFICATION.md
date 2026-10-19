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

# Verification notes

The complete argument is in `RESULT.md`; the executable `verify.py` checks identities from the orbit reduction and the two-step Jacobian using exact SymPy algebra. It then compares polynomial roots with the derived stability inequalities for seven rational parameter pairs and six nonzero squared orbit amplitudes; it also tests the shift recurrence for those pairs and six additional contraction values for boundary identities. On the supplied code the observed outcome is:

```
PASS: exact map recurrence, return polynomial, Schur reductions, boundary factorizations;
PASS: 68 rational-parameter recurrence and finite spectral checks
```

Run with `python3 verify.py` after installing SymPy. There is no randomness or external download, and no third-party paper is embedded.

The infinitude of real parameter choices is covered by the proof, not by the finite spectral tests. The generic Schur reduction and its quadratic inequalities are mathematical facts invoked and algebraically expanded in the proof. Exactly on a spectral stability boundary, the theorem asserts only a unit-circle multiplier configuration; no nonlinear stability or criticality beyond that is certified.
