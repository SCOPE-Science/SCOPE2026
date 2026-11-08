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

In the orthonormal Fock monomial basis e_k=pi^(k/2)z^k/sqrt(k!), the normalized weighted circular sampling Gram has diagonal G_kk=N x^k/(k! K_n), independent of angles and positive weights of total N. Rayleigh bounds therefore imply kappa²>=h_n(x)=max_k(x^k/k!)/min_k(x^k/k!). A regular N-gon of equal weights diagonalizes G via discrete Fourier orthogonality and attains h_n(x) at each radius. Since w_k=x^k/k! is log-concave in k, its minimum occurs at k=0 or k=n; h_n(x) strictly decreases below x_n=(n!)^(1/n) and strictly increases above, giving unique radius. At x_n, w0=wn=1 force constant column to be a least-eigenvalue eigenvector for equality. Vanishing weighted Fourier moments makes the square weighted Vandermonde unitary, whose row norms force all a_j=1 and whose geometric sums force one regular N-gon. Stirling expansion and Poisson mode estimate give e^(1/4)(2pi n)^((1/e-1)/4) exp(n/(2e))(1+o(1)). Independent finite DFT and Gram eigenvalues agreed at n=1,2,3,5,8,16 with κ from sqrt(M_n); all-n proof is algebraic.

## originality

PASS

Gröchenig–Ortega-Cerdà 2022 open full paper establishes finite Fock polynomial MZ families and Proposition 6.1 (no N=n+1 sample families with constants uniformly bounded in n), not the exact degree-by-degree optimum within equal-radius weighted designs, its unique factorial radius, rigidity or exponential asymptotic prefactor. Pan general Vandermonde ill-conditioning is not specialized to the truncated Fock normalized kernel and factorial radial weights. Resultary search identifies other disk/cyclic frame conditioning but no dominating same-claim theorem. The DFT observation alone is prior and excluded as new.

## value

PASS

Exactly N=n+1 normalized samples are the natural square critical Fock polynomial sampling regime; restricting to one radius models circular measurement and leaves nontrivial joint optimization of radius, phases and positive weights. A sharp finite-degree spectral conditioning barrier, unique optimal design and exponential rate with explicit power prefactor are precise structural facts usable in sampling/stability research; not just recomputation of a published no-uniform-bounds statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
