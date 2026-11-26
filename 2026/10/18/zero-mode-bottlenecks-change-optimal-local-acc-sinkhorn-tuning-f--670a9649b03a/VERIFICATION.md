---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Xu–Chen v1 Algorithm 1 gives exactly the stated fixed-parameter, two-state recurrence. At balance the row and column logarithmic corrections differentiate to -diag(a)^(-1)Pi and -diag(b)^(-1)Pi^T, yielding J up to gauge on their composition. J is similar to a positive semidefinite Gram matrix; it is positive row-stochastic, with the simple Perron eigenvalue removed by the quotient. Rank at most m forces nongauge zero modes. With d=1+alpha the modal derivative has determinant lambda/d^2 and trace ((alpha+3)lambda+alpha^2+alpha-1)/d^2. Direct substitution gives 1-tr+det=(alpha+2)(1-lambda)/d^2 and 1+tr+det=(2alpha^2+3alpha+(alpha+4)lambda)/d^2, all strictly positive along with 1-det; smooth local exponential attraction follows in an equivalent norm. Scaling the quadratic Schur test to a disk of radius r>0 gives three affine inequalities in lambda, so only 0 and L matter. For t=sqrt(L)<1/2, the balance alpha_B satisfies alpha^2+alpha-1=t(1+alpha). It has alpha_B<1, so (alpha_B+3)t<1+alpha_B by the identity (1+alpha)^2-(alpha+3)(alpha^2+alpha-1)=(1-alpha)(alpha+2)^2. The top roots there are complex of modulus t/d and the zero root of largest modulus has that same modulus. The product bound excludes smaller parameters and the strictly increasing positive zero-mode root excludes larger ones. At L=0 the nilpotent derivative occurs at the unique positive zero of alpha^2+alpha-1. For t>=1/2 the critical equation increases strictly in alpha with derivative 2alpha+(1-t)^2; it has the asserted root alpha_C<=1. At that root the zero mode is admissible since 1<=(alpha_C+3)t/(1+alpha_C)<3, so its normalized signed root 2-(alpha_C+3)t/(1+alpha_C) has modulus at most one. Below alpha_C the determinant bound is strict; above it d^2 p(r_C) is negative because at alpha_C it vanishes with derivative -r_C[2alpha_C+(1-t)^2]<0 and is strictly concave. This forces a real root above r_C. The threshold comparison follows from t(1+alpha_B)<1 below the quarter and, above it, t(1+alpha_C)-1=s(1-s)(3-s^2)/(2-s)>0 for s=sqrt(1-alpha_C). The explicit 2 by 4 plan has weighted Gram eigenvalues 1,t^2,0,0 by constant and contrast directions. At L=0.04, independent substitution gives alpha_B=0.766190379 and R=0.113238076, versus R=0.170761146 at the single-mode alpha_C. Replay the analytic steps in RESULT.md §§1–6; verify_acc_sinkhorn.py was inspected but not run, and finite grids cannot prove uniqueness.

## originality

PASS

The v1 update, single-mode critical damping, and quarter threshold are prior. The supported distinct claim is the two-endpoint spectral minimax with a competing zero mode, including its strictly different below-quarter optimal parameter. The closest indexed same-map analysis is a genuine overlap on the single-mode family, not a result for simultaneous zero and positive modes.

## value

PASS

Rectangular transport gives a natural full-spectrum problem rather than a hand-picked mode. Exact endpoint control diagnoses when the known single-mode rule gives the wrong tuning, and the positive realization at L=0.04 quantifies a substantial rate penalty. This is useful precisely for choosing or assessing the fixed inner iteration; the value does not rest on asserting an advantage over ordinary Sinkhorn below the quarter, where the exact result shows a disadvantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
