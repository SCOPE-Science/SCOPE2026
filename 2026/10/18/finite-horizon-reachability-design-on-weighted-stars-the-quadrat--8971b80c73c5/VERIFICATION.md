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

The star leaf Krylov coordinates are w_i times polynomials with degrees 0 through m−1 and alternating unit leading coefficient, giving the squared product in (1). Cayley–Hamilton gives AK=KC even for singular K. In the companion basis component j starts in degree j−1; row-column scaling and the integral Jacobian give T^(n²) and the positive scaled Hilbert factor, uniformly across the closed simplex. For distinct symmetric spectra the Gram integral of the squared exponential alternant gives Schur coefficients (1/n, 1/[n(n+1)], 1/[n(n−1)]). The shifted-Legendre projection has E sum(u)=n/2, Var sum(u)=a_n², and E sum(u²)=sum_{j<n}(1/4+a_j²+a_(j+1)²); the off-diagonals a_j=j/[2 sqrt(4j²−1)] give exactly (6). With M=E[(sum u)²] and D=E sum(u²), the quadratic coefficient on tr(A²) in the log is (nD−M)/[n(n²−1)]=n/[2(4n²−1)], and the coefficient on tr(A)^2 cancels. Companion analyticity extends the resulting coefficients through the star's collision and vanishing faces. The trace is −2B and the squared trace invariant tr(A²)=B²+3 sum w_i². In the ordered chamber the strictly concave leading log objective has stationarity at scaled Laguerre roots by their differential equation. The Hessian maps w to −lambda times the all-ones vector and w² to m times that vector minus 2lambda w. With sum w²=2B²/n this gives the stated zero-sum nonzero drift from the tangent stationarity equation; the linear drift vanishes by the budget-constant trace. Compact uniform convergence puts all maximizers near permutations of the leading interior design. The analytic implicit function theorem gives local uniqueness there, or use the chamber Hessian bounded above by −2I/B² before a uniformly small perturbation. Independent exact two-leaf symbolic companion expansion (python /workspace/replay.py 1, SymPy 1.14.0) gives the log-normalized coefficient (6−9y)/35 for y=w_1 w_2 and B=1, with y(T)=1/6−T²/840+O(T³); differentiating the ordered roots of z²−z+y gives the claimed signed sqrt(3)/840 shifts. The replay corroborates this instance only; no all-horizon claim or explicit T_0 is supported.

## originality

PASS

Best of current knowledge, the distinct assessed advance is the explicit nonzero quadratic redistribution and global short-positive-horizon optimizer on the conductance simplex. The Vandermonde determinant, Laguerre equilibrium, classical ensemble identities and generic first-order trace term are credited as background, not new results.

## value

PASS

Reachable volume under a single hub actuation and a fixed conductance budget is a natural network-design objective. The leading Laguerre solution alone would miss a demonstrably nonzero finite-time reallocation; the signed per-spoke formula and global uniqueness up to permutation turn a limiting design into a quantitative positive-horizon result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
