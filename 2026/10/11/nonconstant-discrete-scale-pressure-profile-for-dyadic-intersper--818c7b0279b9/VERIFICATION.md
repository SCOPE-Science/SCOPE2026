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

# Reproducibility and proof checks

The derivation depends on four independently inspectable steps: (i) unique marker-return decomposition and the Kac–Abramov entropy formula, (ii) an exact relative-entropy inequality for return-block probabilities, (iii) uniform convergence of \(A(2^{-n}u)-n\) to \(F(u)\), and (iv) the nonzero first Fourier coefficient \(\Gamma(1-2\pi i/\log2)\) of the dyadic derivative. Each is spelled out in RESULT.md, including the domain and limit quantifiers.

Run the included Python 3 standard-library script with `python3 dyadic_pressure_checker.py`. It checks identities at finite values, compares normalized pressure roots with the limiting profile, and tests the discrete-scale identity. Actual execution returned `PASS: discrete-scale identity, unique-root convergence diagnostics, and dyadic-sum limits.` This numerical evidence is supportive only; no finite run verifies infinite statements.

The equilibrium calculation assumes finite mean return time. This is proved from the strictly positive pressure gap. The zero-marker invariant subsystem is treated separately. For the pressure asymptotic, \(q\) is fixed while \(t\to-\infty\), and the error is uniform over the complete phase interval. No external audit or formal proof certification was performed.
