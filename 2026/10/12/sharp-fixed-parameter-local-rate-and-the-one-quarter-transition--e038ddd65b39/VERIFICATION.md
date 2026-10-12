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

# Verification of the two-atom Acc-Sinkhorn local-rate theorem

The analytic proof in `RESULT.md` covers **every** \(s\in(0,1)\) and every source-permitted \(0<\mu<1\). The supplementary `verify.py` is self-contained and uses only the Python standard library. Run `python3 verify.py` beside this file; it prints `VERIFY_OK 173 arithmetic and nonlinear finite-difference test cases`.

The test script checks exact rational trace/determinant identities and Schur inequalities for a rational grid; validates the repeated-root quadratic and rate-ordering transition at 70 decimal digits for 98 spectral parameters; and verifies by centered finite differences that the **original nonlinear** row/column Sinkhorn update and coupled Acc-Sinkhorn update have the claimed derivative matrices.

This computation neither searches all real parameter values nor proves asymptotic convergence. The universal statements are justified by the determinant inequality, negative characteristic-polynomial test, exact sign factorization, and smooth local fixed-point theorem given in the analytic proof. The unique optimal parameter corresponds to a repeated, generally defective eigenvalue; a polynomial prefactor in the critical linearized orbit is allowed. The paper's homotopy schedule and global convergence assertions are not independently validated here.
