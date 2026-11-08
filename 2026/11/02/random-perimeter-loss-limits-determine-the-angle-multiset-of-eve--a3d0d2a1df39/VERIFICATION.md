---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For any fixed full-dimensional convex polygon with genuine interior angles α_i∈(0,π), every-sided sampled event has complement probability ≤Σ_i(1−d_i/P)^N. On that event the missing perimeter is exactly Σ_i [a_i+b_i−sqrt(a_i²+b_i²−2 a_i b_i cosα_i)]. Multivariate nearest-gap survival gives independent Exp(1) limits for N a_i/P and N b_i/P, while exponential endpoint tails and the exponentially rare empty-side event yield convergence of all fixed integer moments. Substitution S=U+V~Gamma(2,1), T=U/S~Uniform gives one-corner MGF ∫(1−z bα(t))^−2 dt, b=1−sqrt(1−4cos²(α/2)t(1−t)). Its first singularity is zα=1/(1−sin(α/2)) and exact local blow-up exponent −3/2 from a nondegenerate quadratic maximum. Independent numerical quadrature at α=π/2 and deltas 10^-3, 10^-5 gave normalized constants 1.0007845895 and 1.0000080797. Product singularity locates smallest angle; its exponent determines multiplicity; analytic factor division and induction recover every angle. Checker source inspected, but numerical quadrature is not used for the universal theorem.

## originality

PASS

Accept best-of-knowledge originality of the inverse all-angle identification from the limiting missing-perimeter distribution, while explicitly attributing the forward local corner Poisson process and general random-polytope techniques to prior literature.

## value

PASS

Recoverability of the complete unordered angle multiset from one natural asymptotic stochastic observable is a meaningful inverse-geometric classification across all convex polygons. The result also sharply shows that side lengths and congruence class are unidentifiable, so its scope has an informative boundary beyond trivial normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
