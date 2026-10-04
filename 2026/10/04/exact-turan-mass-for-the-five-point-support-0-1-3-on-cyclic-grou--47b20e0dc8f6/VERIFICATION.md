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
The proof is analytic and covers every integer \(N\ge7\). The finite verification script checks the closed formulas on a large initial range but is not used to extrapolate the theorem.

For each \(7\le N\le2000\), `verify.py` constructs the stated extremal coefficients, evaluates every sampled Fourier value \(1+2a\cos(2\pi k/N)+2b\cos(6\pi k/N)\), checks the objective against the closed formula, and checks the active-contact equalities. In the \(N\equiv\pm1\pmod6\) cases it additionally verifies the factorization roots and the adjacent-grid inequalities used in the proof.

The numerical computation is subject to floating-point roundoff. Its role is to detect algebraic or boundary mistakes; correctness of the all-parameter theorem rests on the exact inequalities and factorization in `RESULT.md`.
