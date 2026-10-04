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

The proof was replayed from the exact degree-three scattering matrix rather than from a coarse big-O relation. Solving the first two scattering equations produces the common denominator used in `RESULT.md`; direct substitution verifies those formulas.

`verify.py` performs three numerical replays using only the Python standard library. Two sequences impose the critical relation \(k\ell_2=n\pi+\xi/k\) exactly, one for each parity, and compare the exact amplitude ratios and exact edge-mass ratio with the claimed limits. It also checks the full three-component scattering equation to floating-point tolerance. A third sequence uses \(k\ell_2-n\pi\asymp k^{-1/2}\), for which \(k|\delta|\to\infty\), and confirms the predicted decay of the local mass ratio.

The script returns `VERIFY_OK`. These finite calculations verify algebraic implementation and representative convergence only. They are not used to infer the universal asymptotic claim. The analytic proof supplies the quantifiers. No claim is made on the singular curve \(\varepsilon\xi=2\sin\theta\) or about existence of a global dispersion branch for every prescribed critical parameter.
