---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The frozen source specifies Saiki-Takahasi-Yorke map and Lebesgue fair Bernoulli L/R coding. The branch Jacobians are signed monomial (left diag(2,1,...), right cyclic shift with -2 on the wrapped coordinate); for each admissible word, original-coordinate column j has squared norm 4^{N_j}, N_j equal to visits to cyclic residue r_t by time n, and sum N_j=n. Fair independent right-symbols give Markov P=(I+shift)/2 on Z/M with uniform invariant law from deterministic r_0=0. For any centered contrast f of the occupation vector, solve g(r)-g(r+1)=2f(r); bounded martingale differences are ±f(r) with conditional quadratic variation f(r)^2. Ergodic theorem, martingale CLT and Cramer-Wold give exact covariance I/M-11^T/M^2, multiplied by (log2)^2. Continuous mapping of range gives the log condition-number Gaussian range law; bounded second moments of martingale sums imply uniform integrability and the mean constant (2log2/√M) E max_j Z_j. Finite-state ergodicity gives almost sure common Lyapunov exponent log2/M. Independent integer matrix products for every binary word length <=6 in M=2..5 (126 per M) matched visit counts, and exact Poisson/Green-Kubo identity held for M=2,3,5,11; tests supplement the symbolic all-fixed-M proof.

## originality

PASS

Best-of-knowledge PASS for the explicit map-specific full covariance and condition-number range and expectation. Original source proves coding, periodic-point spectral properties and mixing; exact later published periodic real-spectrum refinement concerns eigenvalues at periodic points. Neither contains the typical-trajectory stationary occupation limit with this explicit covariance and condition-number constant, though abstract martingale CLT is standard.

## value

PASS

The twisted baker map is specifically designed to couple stretching and directional twisting. Its exact rank-(M-1) isotropic Gaussian fluctuations and expected log-condition-number growth distinguish nearly equal asymptotic Lyapunov exponents from significant finite-time anisotropy. The covariance is a natural quantitative dynamical invariant not supplied by generic mixing or periodic-eigenvalue statements, and the parameter-uniform formula holds for every fixed integer M>=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
