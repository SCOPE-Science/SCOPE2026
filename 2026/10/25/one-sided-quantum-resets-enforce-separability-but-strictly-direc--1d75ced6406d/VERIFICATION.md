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

# Mathematical verification

The exact proof is given in `RESULT.md`; the verification program is `one_sided_reset_verify.py` and requires NumPy and SciPy. Run `python one_sided_reset_verify.py`.

The program explicitly constructs the \(4\times4\) Hamiltonian and all \(16\) matrix-unit images of the Lindblad generator; it does not assume the reduced four-coefficient equations. In 256 deterministic parameter samples it checks stationarity, trace normalization, full-generator rank \(15\), numerical agreement with the independent kernel solution, the twice-degenerate spectrum, PPT positivity, the reset-qubit commutator rank, the second-qubit measurement commutator, and the exact strict-positivity identity. The recorded run returned:

`PASS: 256 independent Liouvillian solutions; analytic spectra; PPT; discord asymmetry; full-rank identities`

Analytic verification does not depend on these samples. The all-parameter uniqueness proof and directional-discord classification depend on the strict assumptions \(r>0\), \(J\Omega_1\Omega_2\ne0\), the faithful fixed-state identity, and the adjoint-commutant argument. No independent audit has been performed.
