---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For nonnegative Fourier frequencies summing N=3M, the bijection (M+x,M+y,M-x-y) converts the Laplacian eigenvalue to 3M²+2(x²+xy+y²). Classical unique factorization of Z[omega] gives r_Q(m)=6 sum_{d|m} chi_{-3}(d). A forbidden nonnegative-frequency triple first occurs at Q=ceil(3(M+1)^2/4): any negative coordinate is <=-M-1, completed square gives lower bound, and nearest y to (M+1)/2 attains it with x=-M-1. Thus the arithmetic band is exact and first excluded value genuinely loses representations. For every N, the uniform frequency lattice on a triangle gives the circular-cap CDF for sum t_i²; bounded convex perimeter yields a uniform CDF O(1/N) discretization error; differentiation gives square-root cusp coefficient 6 sqrt(2) at 1/2. Zero center and N not divisible by three treated separately; no unrestricted divisor rule beyond the sharp cutoff is asserted.

## originality

PASS

Best-of-knowledge PASS for sharp *first excluded* Eisenstein representation on a positive-frequency total-degree shell and quantitative entire-shell spectral distribution/cusp. Unrestricted Eisenstein divisor representation counts and circle–triangle geometry are classical and credited. Physical equilateral-triangle Laplacian eigenvalues and Robin/Dirichlet data are a different operator/spectral counting measure, not a direct proof of fixed-degree torus-shell clipping or full-shell probability law. An unindexed lattice-simplex truncation theorem remains possible; Pinsky 1980 is not asserted noncovering because full text could not be obtained.

## value

PASS

A natural holomorphic homogeneous-frequency shell has precise near-minimum eigenvalue multiplicities until an exact first lattice obstruction and an all-degree normalized spectral density with a matching geometric cusp. The precise arithmetic/geometric transition and uniform O(1/N) rate are reusable structural spectral facts, beyond routine counting of Eisenstein norms alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
