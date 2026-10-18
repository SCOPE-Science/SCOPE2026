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

Finite verification: install packages in `requirements.txt` and run `python verify.py` in the directory containing these files. The checker uses (i) an independently updated birth–death law on Hamming weights, (ii) exact-integer enumeration of coordinate-flip words and Boolean Fourier transforms, (iii) diagonalized normalized Choi matrices of the low-dimensional channels, and (iv) finite high-dimensional comparisons with the predicted logarithmic-time capacity excess. It returned `VERIFY_OK 136 finite radial/Fourier/Choi/asymptotic checks`. At the critical scaling, its outputs include excess capacities 0.702034838 (dimension 64), 0.716382161 (dimension 256), and 0.717888423 (dimension 1024), compared with the analytic limit 0.721347520.

The verifier tests only finitely many dimensions, times and parameters. The universal capacity identity follows from degradability, coherent-information concavity and Pauli symmetry; the asymptotic entropy profile follows from the parity-quotiented Fourier expansion, a Gaussian-Hermite limit, an explicit \(L^2\) tail bound and uniform integrability. Neither independent expert validation nor a formal computer proof is claimed. One closely related 1990 source's full original text could not be examined, and publication priority remains provisional.
