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

The finite certificate is `verify.py`. It uses exact rational arithmetic in \(\mathbb Q(\omega)\), with \(\omega^2+\omega+1=0\), and never uses floating-point values to establish the spectrum.

The checker reconstructs the projective single-qutrit Clifford adjoint group from Fourier, quadratic-phase, and Weyl displacement generators and verifies that the closure has \(216\) elements. It then enumerates all eighteen functions \(F:\{0,1,2\}\to\{0,1,2\}\) with exactly two image points. For each map it constructs the exact traceless Liouville block
\[
(\phi_F)_{(0,c),(0,b)}=\frac13\sum_{j=0}^2\omega^{bj-cF(j)},
\]
forms the \(64\times64\) qutrit-Clifford twirl \(B_F=(\phi_F^{\otimes2})^{\mathcal C_3}\), verifies that every averaged entry is rational, and checks the exact rank, polynomial identity, and trace used in the proof.

The deterministic output is included as `verification_output.txt` and ends in `VERIFY_OK`. The full \(81\)-dimensional spectrum is then reconstructed from the block-lower-triangular formula of Wallman and Flammia. The certificate proves only this finite qutrit-Clifford classification; it does not test or certify arbitrary unitary \(2\)-designs or general qutrit channels.
