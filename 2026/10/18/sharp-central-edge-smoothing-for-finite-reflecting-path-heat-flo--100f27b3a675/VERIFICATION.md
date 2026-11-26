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

With the forward incidence matrix E, Q_n=−EᵀE and A_n=−EEᵀ, so the heat intertwining holds including n=2. The norm at an edge is the variation of the corresponding Dirichlet kernel row with zero endpoints. Its discrete derivative evolves by Q_n starting at e_(i−1)−e_i. Each adjacent two-site Markov factor has nonnegative ordered minors (adjacency is essential); Cauchy–Binet and the Lie–Trotter limit give nonnegative ordered two-minors for the full heat matrix. Positivity then orders the two neighboring column ratios, so the row derivative changes sign at most once and the row variation is twice its peak. Strict Gram Cauchy–Schwarz at off-diagonal entries makes the global maximum a diagonal one. Odd reflection on the 2n-cycle gives K_t(i,i)=q_t(0)−q_t(2i); the consecutive radial differences satisfy the stated cooperative tridiagonal ODE with −3 end diagonals, including n=2. They are strictly positive, so exactly the central edges maximize, with the stated step attaining the norm. The sine expansion gives the finite formula and strict decrease. Killing removes paths that leave and return with positive probability, giving the strict lattice deficit, which vanishes along central sites at fixed time by the jump-count tail. For the scaled lattice profile put z=2t and r=I₁(z)/I₀(z); the logarithmic derivative in z is r−(1−1/(2z)). The Riccati equation gives slope −1/(4z²) at each zero; the function is positive near zero and negative at infinity by its leading asymptotic −1/(8z²). There is exactly one global maximum, and no finite path attains it. Independent root evaluation gave t*=0.3949892106717841 and constant 0.6630149334909871. Diffusive scaling follows from the fixed-mode sine and eigenvalue limits and the summable majorant exp(−4sk²).

## originality

PASS

The closest exact catalogue result supplies the same central Dirichlet diagonal and its finite spectral data, and its sharp BV approximation coefficient differentiates to exactly the displayed numerical profile. Those kernel and centrality statements are covered and not credited as new. Its different operator norm does not give the arbitrary bounded-input upper bound or maximizing evaluation location for that norm: its step calculation supplies a lower bound there, not the needed row-variation comparison. The supported distinct contribution is the sharp evaluation for the bounded-input spatial gradient, including the finite deficit and unique dimension-uniform time-weighted optimum. No inspected comparison implies that full claim.

## value

PASS

A rate-one path is a canonical test for bounded-input heat regularization. The exact operator norm and sharp, unattainable finite-path deficit separate edge geometry from lattice smoothing; the global time optimizer identifies a finite-time peak that is strictly above the large-time continuum constant. The bounded-input upper bound and this sharp dimension-uniform optimization add information beyond retrieving a kernel formula or differentiating the BV expression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
