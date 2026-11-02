---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Gauss–Markov innovations factorization K=L diag(1,1-a1²,...,1-a_(n-1)²)L^T establishes SPD, and precision Q=K^-1 has explicit tridiagonal coefficients. All K entries are nondecreasing in each a_i and some strictly; its Perron vector is strictly positive, so λmax(K) strictly rises. Sign conjugation DQD makes all entries nonnegative with strictly positive immediate offdiagonals; each entry is nondecreasing and some strictly, hence its Perron root λmax(K^-1) strictly rises as well. Their product κ2 rises in each a_i, proving unique equal-minimum-gap maximizer for fixed n, including n2. The Toeplitz Fourier symbol (1-r²)/(1-2r cosθ+r²) bounds eigenvalues strictly for every finite vector by positive-frequency integral. Constant and alternating trial vectors asymptotically attain upper/lower symbol edges as n grows; ratio supremum coth²(h/(2ell)), never attained at finite n. Solve inequality in r to get exact all-cardinality Γ threshold. Independently verified exact product kernel/precision inversions and eigen extreme monotonicity in 240 small synthetic configurations, distinct from proof.

## originality

PASS

Classical Kac–Murdock–Szegő Toeplitz spectral calculations already yield the equally-spaced benchmark; earlier general kernel separation work gives useful uniform bounds. What is not supplied by inspected sources is the strict factorwise monotonicity under *each irregular adjacent gap*, which proves unique equal-spacing worst configuration and the optimal uniform separation rule.

## value

PASS

Minimum site separation is a natural kernel-interpolation stability design constraint. The precise worst irregular geometry and necessary-and-sufficient uniform all-cardinality Γ rule are directly useful sharp facts; the result is not merely regular Toeplitz algebra because strict comparison over arbitrary nonuniform sites is the structural step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
