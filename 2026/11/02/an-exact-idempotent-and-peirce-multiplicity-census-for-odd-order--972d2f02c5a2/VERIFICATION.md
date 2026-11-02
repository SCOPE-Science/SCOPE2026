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
# Verification

Run `python3 verify_core_idempotents.py` with Python 3 and NumPy. It constructs integer doubling/inversion orbits and their exact root-of-unity weights; enumerates every Fourier assignment predicted for the seven small test groups; checks the complex Fourier idempotence relations; independently reconstructs and multiplies vectors in the quandle algebra; and checks the right-multiplication identity, trace, and square trace against the claimed eigenvalue multiplicities. All seven reported group instances pass and the program prints `VERIFY_OK`.

The coefficient computations use ordinary floating-point roots of unity (tolerance 2e-7) and constitute finite corroboration, **not** a computer-assisted proof for arbitrary finite odd groups. The unrestricted proof appears in `RESULT.md` and uses exact cyclic-group/root-count reasoning. No external independent audit was performed.
