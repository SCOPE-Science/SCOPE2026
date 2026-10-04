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

`verify_blp_lorentzian.py` checks the derivative identity, the exact revival maxima, and the geometric sum for deterministic non-Markovian coupling ratios.

It verifies that the direct partial sum
\[
\sum_{n\ge1}e^{-\pi\Gamma n/\kappa}
\]
matches
\[
\frac{1}{e^{\pi\Gamma/\kappa}-1}
\]
to numerical precision.

It also checks the normalized threshold asymptotic and the three-term strong-coupling expansion.

The finite replay is supplementary. The closed form and asymptotics are proved analytically in `RESULT.md`.

No independent audit has been performed.
