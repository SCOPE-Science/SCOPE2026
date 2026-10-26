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

The analytic argument uses the identity \(\operatorname{tr}(XX^*)-\operatorname{Re}\operatorname{tr}(X^2)=\|X-X^*\|_{\mathrm F}^2/2\) for \(X=A^{1/2}B^{1/2}A^{-1/2}\), followed by Ky Fan eigenvalue majorization of \(S-JSJ\) with \(S=B^{1/2}\) and \(J=2P-I\). This yields a bound on the off-diagonal Frobenius energy, and balanced extreme-eigenvalue pairs attain equality.

To check exact rational examples, run `python3 verify.py` with Python 3; no external packages or network are needed. Expected output: `PASS 2950 exact rational checks across ranks, dimensions and orbit orientations`.

The finite checks compare the trace identity for dimensions \(2\) to \(8\), the sharp matched-pair construction in dimensions \(2\) to \(10\) for every splitting rank, and the specialized two-dimensional commutator formula for 900 rationally parametrized rotations. Random sampling and finite cases are not proofs of the universal majorization inequality or its optimality; the proof and explicit construction establish them for all stated matrices.

Primary mathematical limitations: the fixed-spectrum sharp result assumes a two-eigenvalue first factor; unrestricted first-factor spectra are not classified. The full 2025 introductory paper was not accessible for complete priority comparison. Independent audit was not performed.
