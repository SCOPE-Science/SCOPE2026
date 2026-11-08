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

Radial U(d)-orthogonality diagonalizes Toeplitz by homogeneous degree n with multiplicity binom(n+d−1,d−1) and exact eigenvalue quotient of radial moments. Strict decrease of symbol and monotone likelihood-ratio tilt proves λ_n strictly decreasing. The moment log-density L_n(r)=(2n+2d−1)log r−2phi(r) satisfies L_n″<=−2m, unique saddle r_n phi′(r_n)=n+d−1/2 and r_n~sqrt(n); global Gaussian concentration and local lower-normalization give λ_n=f(r_n)(1+O(n^-1/2)) uniformly with only bounded C² Hessian. The derivative q′(r)=phi′(r)+r phi″(r) lies between 2mr and2Mr, so comparing the threshold f(R_t)=t to saddle-localized λ_n brackets the final included degree by n_t=q(R_t)+O(R_t). Binomial multiplicities then yield t^(2d/beta)N(t)=h(R_t)^d/d!+O(t^(1/beta)). As r_n gaps are O(1/r_n) and |h′(r)|=O(1/r), sampled and continuous cluster intervals coincide; two examples check the difference between convergent slope and oscillating Hessian, or oscillating slope. Independent Gaussian radial moment integration supports the local eigenvalue localization across dimensions 1–3, beta 0.5,1.5,3, degrees 40–250.

## originality

PASS

Xu–Dong arxiv:2609.16970 has quadratic Weyl laws and one radial 1D example showing two distinct subsequential limits (Proposition 5.3). It does not present an all-dimension uniform pointwise profile or an iff slope criterion for all bounded-Hessian radial weights in inspected text. Grudsky–Vasilevski treat radial symbols under fixed Gaussian weight. The 2026 Huang–Wang–Zeng abstract describes general rearrangement characterizations of Fock-type Toeplitz singular values, possibly stronger; its full text remains inaccessible via arxiv/OA and authorized Oxford returned vpn_disconnected, so implied prior coverage cannot be definitively excluded. This is a qualified best-of-knowledge PASS, not a finding that inaccessible paper is non-covering.

## value

PASS

Provides a complete exact radial-geometric criterion for classical Weyl asymptotics of a natural compact Toeplitz operator, a quantitative pointwise spectral profile, and all subsequential limit values, in any fixed complex dimension. This directly addresses the uniform-curvature insufficiency shown by Xu–Dong and distinguishes Hessian oscillation from the actual radial slope controlling eigenvalues, rather than merely adding a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
