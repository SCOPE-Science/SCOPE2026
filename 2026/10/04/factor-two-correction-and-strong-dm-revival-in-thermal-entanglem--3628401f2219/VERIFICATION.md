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

`verify_dm_teleportation.py` reconstructs the source Hamiltonian from Pauli matrices, diagonalizes it to form the Gibbs state, evaluates all four Bell probabilities, applies the induced Pauli channel independently to both input qubits, and computes Wootters concurrence directly.

The direct matrix result is compared with the corrected analytic expression on deterministic antiferromagnetic and ferromagnetic grids. Whenever the concurrence is positive, the source's printed Eq. (14) is checked to be exactly one half of the direct value.

The script also checks explicit strong-\(D\) revival and convergence of
\[
D^2C_{\mathrm{out}}
\]
to
\[
C_{\mathrm{in}}.
\]

The replay is supplementary. The correction and asymptotic law are proved analytically in `RESULT.md`.

No independent audit has been performed.
