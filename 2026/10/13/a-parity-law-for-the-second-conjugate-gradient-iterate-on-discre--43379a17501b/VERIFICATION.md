---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For one-dimensional Dirichlet Poisson tridiagonal A_n=tridiag(-1,2,-1), initial x0=0 and nonnegative isolated load plus remote symmetric hat, the exact 2D Galerkin formula x2=[(m0m3-m1m2)b-(m0m2-m1²)Ab]/D, D=m1m3-m2²>0, gives the first-coordinate numerator rN_k(r)/D for a two-peak plateau. The exact polynomial is N_k(r)=2r⁴-2r³+A_kr²-B_kr-C_k with stated cubic k-coefficients. C_k>0, N_k(1)=2(k+1)(4k-5)>0, and second derivative of N_k>0 for all r≥0,k≥2; with the derivative of N_k at zero<0, this proves a UNIQUE positive zero r_k∈(0,1) and sign negative below, positive above. Uniform k^-3 expansion and Taylor at 1 establish r_k=1-2/k+O(k^-2). One-peak hat instead has lim_{r↓0} x2_1/r=k/3>0; plateau has strictly negative limit. Independently reconstructed Krylov moments and exact two-step CG for k=2,3,4,7,10,25, rational amplitudes and padding; integer b=(1,0,0,2,4,4,2,0,..) gives x2_1=-58/171. Green matrix A^-1 has strictly positive entries so exact solution remains positive. Checks are finite witnesses only; analytic moments/proof cover all n≥required and k≥2.

## originality

PASS

The published general result that CG can become negative even for Stieltjes matrices, and that three dimensions suffice, is explicitly prior work. The earlier Resultary finding proves a sharp *different* 3x3 threshold at diagonal parameter a=4 for forcing b_B; it does not imply the parity-dependent remote discrete-hat profile for the canonical unmodified Poisson A_n (all diagonal 2), exact unique amplitude threshold r_k, asymptotics or opposite small-amplitude sign between one- and two-peak hats. Beckermann–Kuijlaars analyze exact same Poisson finite-difference matrix but special-RHS convergence rates, not transient component sign frontier. Schmelzer–Stoll accessible abstract states general nonnegativity loss, but complete full text remained inaccessible; this is a residual risk, not automatic O failure.

## value

PASS

An exact transient sign frontier for a canonical inverse-positive SPD discretization is a motivated finite-element/elliptic-solver question: a simple parity change in a remote nonnegative hat flips the sign of the second CG step at another site while true A^-1 b stays positive. Unique amplitude threshold for all hat widths and asymptotic law are new natural structural facts, not merely one tiny negative witness or unmotivated exact arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
