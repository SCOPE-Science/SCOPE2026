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

The two mathematical forms of the fourth moment (aperiodic-correlation and squared-polynomial convolution) are independently evaluated in `CHECK.py` over all 9075 unique gauge-normalized phase assignments. Every arithmetic operation is on ordinary integers representing Gaussian or Eisenstein integers. The reported minimum, runner-up, complete gauge-fixed optimizer set and geometric-orbit partition are checked against `CERTIFICATE.json`.

Run `python3 CHECK.py` with `CERTIFICATE.json` in the same directory. The observed result was `CHECK_OK 9075 exact exhaustive normalized arrays, double evaluated`.

This is complete **only** for four-by-two full supports with phase alphabets 2, 3, 4 and 6. The finite Fourier-grid extension follows from a separate character-orthogonality argument whenever both no-alias inequalities hold. Computations do not establish anything about continuous-phase optimizers or other array shapes. No independent audit has been performed.
