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

The proof uses conditional independence at the echo midpoint, detailed-balance time reversal and invertibility of finite-dimensional Feynman--Kac evolution. The counterexample is verified by `proof_checker.py`, a Python-standard-library, rational-arithmetic computation of degree-40 matrix exponential polynomials.

Run `python3 proof_checker.py`. The script computes the rational real and imaginary parts, checks that the latter vanishes exactly, checks that the former is less than \(-1/10\), and verifies the rational bound \(2\cdot3^8R+R^2<10^{-4}\), with \(R=3^8 8^{41}/41!\). The two facts imply that the exact Hahn echo is strictly negative. Finite tests do not establish the general reversible positivity statement; that follows from the independent analytical norm-square argument in `RESULT.md`.

The optional decimal output is diagnostic, not an independent formal numerical certificate. No experimental observation or historical-priority certification is claimed.
