---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For k<=2 independent Hermitian observations modulo I, minimize the convex coercive spectral width of B−Σt_j A_j. At the minimizer, subgradient optimality yields intersecting convex hulls of expectation vectors on extremal eigenspaces; Toeplitz-Hausdorff makes each of these pure-state expectation sets convex for k<=2. Hence unit top/bottom eigenvectors with matching observations attain spectral width, are orthogonal if positive, and Δ=2 operator-norm distance from real affine span. For scaled Pauli blocks, exact Bloch shells have radial intervals [|(1+r)p−r|,r+(1−r)p]. Overlap for p>=q yields gap ≤4r/(1+r) and q=0,p=2r/(1+r) attains it; both residual qubit blocks force affine distance 1. At r=0 pure Bloch sphere gives B=2||a||−1, not affine. Zero, one, two observations and r endpoints are included. Independent exact-rational overlap tests checked 1,386 grid pairs and witnesses; infinite quantifiers rest on analytic proof.

## originality

PASS

Best-of-knowledge original quantitative stability and parameterized obstruction, while qualitative affine factorization and joint-range geometry are prior.

## value

PASS

An optimal modulus for what two pure-state expectations cannot reveal, with an orthogonal witness; the three-observation phase transition gives a sharp boundary to the numerical-information rigidity theorem and an explicit nonlinear zero-defect counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
