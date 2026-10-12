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

The proof was replayed at the level of its critical algebra. For a vacuum-to-single-excitation operator, exactly one local Pauli-\(Z\) dephasing term changes sign, giving total dissipative eigenvalue \(-\kappa\). Hence the entire such coherence sector acquires the common factor \(e^{-\kappa t}\) while the Hamiltonian performs the noiseless one-excitation evolution.

For the reduced qubit channel, excitation conservation fixes the population part to a single parameter \(p\in[0,1]\). After partial transposition, the only block relevant to a negative eigenvalue is \(\frac12\begin{pmatrix}0&c\\ \overline c&1-p\end{pmatrix}\), whose determinant is \(-|c|^2/4\). Thus it is indefinite exactly when \(c\ne 0\). The bundled checker verifies this identity and the displayed eigenvalue formula on a deterministic parameter grid, and verifies the local-dephasing sign count for chain sizes up to twelve as a regression test. The finite regression grid is not the proof of the all-length statement.

For the Clark et al. engineered chain the source gives \(\tau=\pi/J\) and perfect mirror inversion, so \(|f|=1\). At finite \(\kappa\), \(|c|=e^{-\kappa\tau}>0\), proving that the channel is not entanglement breaking. No claim is made at the limiting point \(\kappa\tau=\infty\), nor about high transfer fidelity.
