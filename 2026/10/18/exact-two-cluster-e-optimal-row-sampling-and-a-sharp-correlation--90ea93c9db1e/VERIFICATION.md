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

Projection on a unit row reduces squared error by its squared inner product with the error; minimizing the expectation over unit errors gives the stated sharp eigenvalue. The positive definite Gram matrix and the information matrix are related by orthogonal change of coordinates, including zero-probability cases. Smallest eigenvalue is concave in the probabilities, so averaging within the permutation groups loses nothing. The two contrast eigenvalues and the coupled 2×2 block then exhaust the spectrum. For r≤c the coupled block at uniform sampling is at least the contrast value, itself a global upper bound after averaging. For equal sizes, group interchange makes uniform optimal, with rate (a−pr)/(2p) when r>c. Independently, the coupled-mode maximum can be certified without differentiating: let g_A,g_B be the two class-mean directions in row space with Gram [[a,r√(pq)],[r√(pq),b]]. Take a unit test vector x with inner products (√p,−√q) times a positive κ. Its Rayleigh quotient against u g_A g_Aᵀ+v g_B g_Bᵀ is κ² for all feasible u,v. Solving the eigenvector equation with this Gram inverse gives u/v=(b+qr)/(a+pr) and κ²=(ab−pqr²)/(pb+qa+2pqr). The opposite inner-product signs select the lower eigenmode. Equality in the Rayleigh bound forces this ratio, so the concave coupled branch in u has a unique peak and is strictly increasing and then decreasing. For t=u/v≥1 the transverse bound is (1−c)v; after subtracting it from the coupled matrix the determinant is qc v²[tD−(1−c)] and the lower diagonal is qc v>0. This gives exactly the asserted crossing and clipped optimum, with agreement of the values at the boundary; for t≤1 both relevant modes increase. For fixed p,c,r in the specified open asymptotic range, ab−pqr²=a(1−c)+q(ac−pr²)>0, t₀ grows linearly and the optimum is eventually clipped at R. The uniform coupled Gram eigenvalue tends to a−pr²/c by its Schur-complement equation, so the rate ratio tends to R. Independent eigenvalue checks against 2,500 sampled simplex competitors per case covered uniform, equal-size, unclipped and clipped regimes; at q=10,000 the stated asymptotic example approaches 25/9. These are finite diagnostics, not a global proof. The uploaded checker was inspected, not executed.

## originality

PASS

Earlier work explicitly formulates the identical generic one-step E-optimal problem, including its SDP, so neither the objective nor the optimization formulation is new. The specific evaluated two-block solution, transverse/coupled transition and large-class advantage are not supplied by that generic formulation. A later indexed record is mathematically equivalent in the allocation and stronger in full-simplex uniqueness; no earlier coverage by that record was established. No priority claim is made.

## value

PASS

Two exchangeable groups model clustered unit rows while keeping transverse modes in both groups. An exact solution of the worst-initial-error design problem identifies when the smaller class is oversampled and when an active contrast clips the allocation. The tunable unbounded rate advantage over uniform sampling shows that the regime change is not cosmetic. The precise benefit is a sharp one-step coefficient, not optimal finite-horizon MSE or wall-clock cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
