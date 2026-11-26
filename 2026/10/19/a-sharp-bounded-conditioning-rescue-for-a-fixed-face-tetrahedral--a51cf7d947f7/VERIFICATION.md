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

For the fixed oriented tetrahedral faces, write B for the first three columns. The remaining column is -B1; B has full column rank, so (B D^{1/2})^+ B=D^{-1/2}. Thus the preconditioned operator is exactly D^{-1/2} M D^{-1/2} for M=diag(a,1,1/a)+11^T. The inherited choice gives I+vv^T with squared length 1/a+1+a, hence condition number 2+a+1/a. With D=diag(M), an independent symbolic determinant of lambda I-D^{-1}M gives (lambda-1)(lambda^2-2lambda+1/2)-a lambda/(1+a)^2. The three simple positive roots at a=0 justify the O(a) condition-number estimate about 3+2 sqrt(2). For any D, the leading principal block has invariant correlation c=[2(1+a)]^{-1/2}; its normalized determinant det/(trace)^2 is at most (1-c^2)/4, so by interlacing the full condition number is at least (1+c)/(1-c). This bound is uniform over all positive D and squeezes the infimum to the claimed order. The reciprocal sharp ratio follows directly. Replay: use RESULT.md lines 41–87, or construct M and symbolically compute det(lambda I-diag(M)^{-1}M). The packaged check.py was read, not executed; its rational and finite eigenvalue checks do not certify the optimization. There is no claim of a finite-a optimum, variable face selection, or stability in finite precision.

## originality

PASS

The inherited spectral method, Jacobi scaling, and two-by-two principal-block inequality are established tools. The distinct result supported on the inspected evidence is their sharp fixed-face application to this graded tetrahedral Hodge family, including the universal asymptotic infimum with its O(a) control and the unbounded penalty of inheritance.

## value

PASS

A fixed retained subcomplex is a natural constraint in Hodge preconditioning. This sharp example distinguishes improving conditioning from approximating the operator in norm, and quantifies when inherited weights lose by order 1/a despite a simple bounded correction. The universal lower bound makes it an exact benchmark for positive reweighting, not merely a choice of an improved heuristic; no claim about larger meshes, running time or better face selection is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
