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

# Reproducibility and verification

The proof reduces to exact integer cellular chains, two explicit integer determinant certificates, mod-two Gaussian elimination, and exhaustive evaluation of the full 336-element graph automorphism group. The standalone files `verify.py` and `CERTIFICATE.json` are sufficient to replay these finite calculations with Python, NumPy, and SymPy.

Replay observed: **PASS** with cell vector 91, 252, 168; boundary-minor determinant +2, rank modulo two 153; torus-minor determinant +1; 14 torus generators; automorphism character class counts 1, 21, 28, 56, 42, 56, 48, 84; character squared norms 336 and 336, with cross inner product zero.

The computation makes no statement about homotopy attaching maps, integral representation splitting, or arbitrary graphs. The mathematical proof of the integral torus basis additionally uses the saturation argument in `RESULT.md`. Independent scientific audit is not claimed.
