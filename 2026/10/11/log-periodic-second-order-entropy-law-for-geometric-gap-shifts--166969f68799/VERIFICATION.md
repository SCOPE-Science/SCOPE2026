---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The symbol-frequency constrained entropy E_b(t) has a unique maximizing stationary renewal process. For any invariant μ, first split the all-zero atom a; under inducing on [1], return-label frequencies q have mean (1−a)/t ≤1/t, and Abramov/Kac yield h_μ ≤ tH(q). Nonnegative relative entropy versus p_k∝exp(−λb^k) bounds H(q) by log Z+λ/t, attained only with a=0, independent returns, and m(λ)=1/t. Writing λ=ρb^(−K), the shifted sums give Z=K+Ψ_b(ρ)+O_b(b^(−K)) and λ∑b^k exp(−λb^k)=A_b(ρ)+O_b(b^(−K)), uniformly for ρ∈[1/b,1]. Inverting L=log_b(1/t) produces the displayed log L+(log_b L+Ξ_b(ρ))/L+O_b((log L)^2/L^2). Index shifts establish periodic Ξ; a nonzero Γ(1−2πi/log b) Fourier coefficient makes A nonconstant, and the exact derivative product forces Ξ nonconstant. Any fixed ρ is sampled along λ=ρb^(−K), giving the complete cluster interval. Independent truncated numerical calculations checked b=2,3,5 periodic endpoints only; all infinite conclusions use analytic proof.

## originality

PASS

The 2026 Haydarov–Kadyrov–Makhmudov–Mamayusupov paper treats inducing, fixed-zero atom, and general renewal Gibbs variational formulas; the 2025 Ramirez–Somers paper gives broader ordinary topological entropy and mentions powers-of-two sets. The first-order renewal mechanism is prior, but the precise low-marker-density two-term law with an explicitly nonconstant geometric-lattice phase and exact subsequential interval was not found in those inspected sources or Resultary searches. Classical Mellin periodic expansions pose a real possible equivalence risk; the novelty claim is bounded and attaches only to the second-order normalized phase.

## value

PASS

Geometric return-length sets are a canonical sparse S-gap class, and entropy at a fixed rare-marker frequency is a natural thermodynamic/multifractal invariant. The theorem gives a nontrivial iterated-log endpoint and fully characterizes the nonconstant order-1/L lattice correction, beyond ordinary pressure/entropy equations. It is an independently useful exact asymptotic for a natural infinite symbolic dynamical family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
