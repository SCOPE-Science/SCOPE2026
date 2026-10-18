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

Reconstructed homogeneous norm Σ_{x,j}|u(x+e_j)−u(x)|² on Z^d (d≥3), p*=2d/(d−2), q>p*: the transient Green vector G has <u,G>_D=u(0), K=G(0), h=G/K and nearest-neighbor value ρ=1−1/(2dK)∈(0,1). Discrete harmonic maximum principle, decay and ℓ^{p*} make 2d points ±e_j the sole strict largest noncentral values, so A_q=Σ_{n≠0}h(n)^q=2dρ^q+o(ρ^q). For a unit-energy near maximizer, translate and phase to its maximum a and decompose u=a h+v with v(0)=0, a²/K+||v||²_D=1; interpolation first gives t=||v||=O(q^−1/2). Hölder and mean value yield R_q=O(qt(ρ+t)^{q−p*}); near-maximality and a Green test improve t=O(ρ^q e^{C√q}), hence R_q=o(ρ^q), b^q=1+o(ρ^q) and (C_{d,q}/√K)^q=1+2dρ^q+o(ρ^q). Taking qth roots gives 2dρ^q/q with correct normalization, real/complex cases, no attainment assumption. The limiting proof is analytic, not finite-box extrapolation.

## originality

PASS

The 2014/2015 Ilyin–Laptev–Zelik source proves the sharp ℓ∞ endpoint and a nonsharp supercritical finite-q estimate, not the first exponentially small q→∞ correction. No surveyed original statement implies the first-shell prefactor. Best-of-knowledge with abstract Green-kernel perturbation risks.

## value

PASS

Sharp lattice Sobolev norms are natural constants, and the first correction beyond the endpoint is a quantitatively precise, dimension-uniform structural asymptotic. Its exponential base identifies the lattice Green first shell and its prefactor exactly counts the 2d nearest neighbours. It is not a renaming of the endpoint constant or a finite experiment, even though fixed finite-q exact values and critical q remain unknown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
