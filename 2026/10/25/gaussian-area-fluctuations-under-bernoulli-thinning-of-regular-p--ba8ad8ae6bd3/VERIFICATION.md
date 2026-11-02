---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For retained vertices in cyclic order, area=½Σ_j sin(K_j θ) and the missing area score f_n(k)=½(k sin θ−sin kθ), valid including one/two survivors; the zero-survivor event is handled separately and decays as q^n. A chord of index length k<n is a boundary edge exactly when both endpoints survive and k−1 interior vertices are deleted, probability p²q^(k−1). This gives the exact finite geometric series for EA_n. Taylor f_n(k)=θ³(k³−k)/12+O(θ^5(k^5+k)) with geometric gap tails makes the L² remainder O(n⁻⁴), negligible at n⁻⁵ᐟ². For geometric iid K, E K=1/p, g(K)=K³−K, a=E g(K)/E K=6q/p²; standard centered renewal-reward stopped-sum CLT and uniformly bounded wrap correction yield Var(S_n)/n→p E(g(K)−aK)^2=36q(1+q)(1+5q+q²)/p^5. Multiplying by (2π)^6/144 produces stated V_p; Slutsky gives the Gaussian law. Independent direct enumeration of retained subsets for n=4,5,6,7,9 and p=1/3,1/2 (10 configurations of parameter pairs) exactly corroborated finite mean; independent geometric-moment summations for p=.25,.4,.5,.75 agreed with V_p. Fixed p is essential, finite tests only corroborate analytical CLT.

## originality

PASS

Pardon proves CLTs for Poisson/interior i.i.d. random planar points in expanding convex settings, not Bernoulli occupancy of deterministic equally spaced boundary points. Koroleva–Nikitin studies random fixed-order polygons with continuous sampled locations on a circle; different counting/scaling. Pérez-Lantero studies the distribution/algorithmic complexity for finite sets of independent stochastic points, but its general algorithms do not provide this closed regular-vertex finite mean, sharp n^5 variance constant, or renewal CLT. Resultary semantic search returned no matching Bernoulli cyclic-gap theorem. The special model and explicit asymptotics are independently meaningful.

## value

PASS

The theorem exactly identifies the n^(-5/2) Gaussian fluctuation scale, a closed variance coefficient and the full finite-n mean for an infinite, natural random-geometry model. These are useful as baseline asymptotic estimates for random vertex deletion, and neither standard renewal CLT alone nor finite computation supplies the geometric constant without the nontrivial cyclic-gap reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
