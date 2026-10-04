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

The analytic proof in `RESULT.md` starts from the four-sector secular determinant printed in Section 4.2 of arXiv:1906.09091v1. The only division is by \(k^2\omega_j^2\sin k\), so the stated scope explicitly excludes \(k=0\) and \(\sin k=0\).

The packaged `verify.py` performs two corroborative checks using only the Python standard library:

1. It evaluates, in exact rational arithmetic, each of the four normalized source-sector polynomials and its claimed factorization on a grid of rational \(k^2\) and \(c=\cos k\) placeholders. This checks the algebraic identities independently of floating-point root finding.
2. It numerically brackets roots of \(\cos k=\pm(k^2-1)/(k^2+3)\) around several multiples of \(\pi\) and verifies convergence of \(N_n(k-N_n)\) to \(\pm2\sqrt2\).

The infinite factorization, simplicity, multiplicity, and asymptotic statements are established symbolically in the proof. The finite numerical checks are not used as exhaustive evidence. The claim does not assess the Dirichlet family or the exceptional point \(k=1\).
