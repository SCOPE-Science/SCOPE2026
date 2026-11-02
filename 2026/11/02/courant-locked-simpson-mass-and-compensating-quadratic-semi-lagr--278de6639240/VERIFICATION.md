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

# Verification record

The algebraic proof reconstructs the full nodal update, its parity-sum matrix, the unique stationary left vector, the complete block Fourier spectrum, the exact Schur--Cohn identity, and the two-step composition criterion. The nontrivial symbolic discriminant identity was expanded and simplified exactly, independently of finite sampling. The companion `verify.py` uses only the Python standard library and tests exact rational nodal updates, left invariance, Simpson conservation thresholds and checkerboard equality over multiple periods and Courant numbers. It additionally checks the algebraic two-step root and numerical Fourier identities on a finite grid of parameter choices.

Run `python3 verify.py` in the same directory as the supplied files. Passing finite tests is not evidence for untested infinite cases by itself: the quantified proof in `RESULT.md` supplies those cases. Independent mathematical audit has not been performed.
