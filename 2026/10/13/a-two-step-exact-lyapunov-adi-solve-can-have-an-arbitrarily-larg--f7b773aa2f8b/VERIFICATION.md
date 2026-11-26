---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For exact real-shift ADI with E=I and P0=0, use Z=sqrt(2 sigma)(A-sigma I)^(-1)b and b_new=b+sqrt(2 sigma)Z; expansion of the Lyapunov residual after the positive update ZZ^T gives b_new b_new^T. At sigma=1, A=-I+MN with N=e1 e2^T and N^2=0 yields C=(A+I)(A-I)^(-1)=-(M/2)N. Thus b0=e2, b1=-(M/2)e1, b2=0, and the spectral and Frobenius residual norm ratios are both M^2/4 (9 at M=6). Direct solves for the two columns give Z1=sqrt(2)(-M/4,-1/2)^T and Z2=sqrt(2)(M/4,0)^T, so P1=Z1Z1^T and P2=P1+(M^2/8)e1e1^T. Substitution gives zero residual at P2; Hurwitz stability gives uniqueness. This verifies the Loewner inequalities and exact termination independently of the supplied verifier. The scalar multiplier (a-sigma)/(a+sigma) has modulus <1 for a,sigma>0, ruling out growth in dimension one. R2 has rank zero, not one; the norm equality still holds for rank at most one. The frozen verification notes and verify.py were inspected, not run; in particular verify.py lines 30–42 check supplied P and P1 by substitution and define P2 from P-P1, rather than independently constructing the ADI columns. The ratio is a multiplicative change, not an additive increase, and exact termination does not assert finite-precision behavior.

## originality

PASS

The matrix/right-hand-side family and exact solution are prior, as are the ADI recurrence, residual factorization and nonnormal Cayley overshoot. The supported distinct claim is the sharp, dimension-minimal counterexample for ADI residual norms: arbitrary prescribed first ratio at one fixed spectrum with immediately following exact termination and Loewner improvement. No checked statement gives that consequence as a residual-monotonicity or fixed-spectrum result. The proof is short but needs the choice of a shift matching the Jordan eigenvalue, exploiting the resulting nilpotent map on a specified right-hand side rather than merely restating a norm or convergence bound.

## value

PASS

A motivated minimal counterexample to spectrum-only control of the commonly monitored ADI residual, even for shifts that solve exactly after the next step. The exact magnitude and two positive updates separate transient norm growth from deterioration of the Gramian approximation. Its value is that concrete obstruction, not the known matrix family, routine inverse, or new general ADI theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
