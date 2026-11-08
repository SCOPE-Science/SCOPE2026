---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For the first-order periodic Korobov RKHS and all N>=2 equally spaced grid nodes, the minimum-norm interpolant is the piecewise-linear hat interpolant minus a common mean-dependent cell bubble, obtained by the Euler–Lagrange equation and mean normalization. Integrating against mu(y)=(pi/2)|sin(2pi y)| yields w_j=P_N,j-T_N,gamma, with T_N,gamma=2pi^2 gamma H_N/[N(1+pi^2 gamma/(3N^2))]. Symmetric-decreasing convolution on a circle proves the smallest hat moment P_N at density zero, P_N=1/2-N sin(2pi/N)/(4pi). An exact Fourier product gives H_N=(2pi^2)^-1-(2pi N)^-1 cot(pi/N) for even N and H_N=(8N^2)^-1+(2pi^2)^-1-(4pi N)^-1 cot(pi/(2N)) for odd N. H_N>1/(6N^2), P_N<=1/N ensure a unique crossing gamma_N=3N^2 P_N/[pi^2(6NH_N-P_N)] with strict/weak sign boundaries. Taylor expansions give gamma_N=N+pi^2/3+O(1/N). Independent numerical integration of kernel means and direct Gram solves at N=2,3,4,5,8 matched the analytic weights and crossing; the all-N proof comes from spline/Fourier algebra, not from finite grids.

## originality

PASS

Bartel et al. arXiv:2610.01113v1 provide the exact sine periodization, first-order kernel, weight construction, and convergence framework; their full-text Sections 3 and 7.2 do not provide this all-parameter minimum weight/gamma frontier and explicitly discuss unsettled multivariate positivity. General RKHS optimal cubature and classical product-integration positivity are antecedents, but their accessible statements do not imply the concrete cotangent sign law. Resultary nearby Fourier positivity and spline records use different optimization problems. Older spline/product-integration literature remains a priority risk.

## value

PASS

For a widely used periodized lattice integration method, positive integration density does not force positivity of the unconstrained optimal cubature weights. The explicit full-uniform-grid all-parameter sign threshold, parity-sensitive cotangent values and asymptotic gamma_N~N are natural and useful for positivity-preserving implementation and counterexamples to overly broad convergence-to-positivity interpretations. The result exactly solves a motivated univariate case without claiming the multivariate open problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
