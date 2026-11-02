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

The exact mathematical proof in `RESULT.md` establishes the complete-intersection property, all-dimensional Jacobian classification, projective orbit count, and local Hessian nondegeneracy. All assumptions and the characteristic-zero restriction are explicit.

The standalone `verify.py` was run with the system Python interpreter and returned:

```text
VERIFY_OK: exact projective orbit counts n=6,9,12; modular Hessian rank n=6,9,12,15,18; multiplicity obstruction n<=31
```

The script uses only the Python standard library. It computes orbit representatives in the labelled \((1,\omega,\omega^2)\) model for \(n=6,9\), checks the combinatorial counts \(30,560,11550,252252\), evaluates Jacobian and constrained-Hessian ranks exactly modulo \(1009\), and checks the positive multiplicity expression for the finite stated range. Finite-field tests and enumerations are auxiliary evidence, not proofs in characteristic zero or for arbitrary \(n\). The Hessian argument over \(\mathbb C\) and its projective radial quotient are explicitly supplied in the main proof.

No external proof certification or independent audit is asserted.
