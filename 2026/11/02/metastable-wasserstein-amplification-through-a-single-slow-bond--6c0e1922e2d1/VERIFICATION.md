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

The birth–death order-preserving coupling and path Kantorovich formula reduce the induced W1 norm exactly to the maximum of adjacent positive gradients of P_t x. Reflection about the slow edge identifies its central gradient as 2e₀ᵀexp(tR_ε)z, R_ε=R₀−2εe₀e₀ᵀ. Neumann cosine eigenvectors give the ε=0 expansion; analytic perturbation of the separated slow mode gives eigenvalue 2ε/m and amplitude m−(m−1)²ε/2+O(ε²). The first fast decay has λ_m and B=(2/m)cot²(π/(2m)), satisfying Bλ_m/2=K_m. Uniform control of the interior-edge stable spectrum rules out their dominance for small ε. Balancing slow decay 2εt against fast deficit Be^(−λ_m t) localizes the global peak at log(K_m/ε)/λ_m and yields the second-order coefficient. The small-time central gradient derivative equals 2(1−ε), and at ε=1 the Dirichlet gradient generator is substochastic. Independently constructed full 2m×2m generators confirmed peak/time asymptotics over m=2..6 at ε=10^−4,10^−6. Finite numerics do not prove the spectral uniformity assertions.

## originality

PASS

Chafaï–Joulin 2013 already characterizes Wasserstein Lipschitz norms through birth–death gradient intertwinings; this standard reduction is explicitly not novel. The sharp global weak-bond peak height, maximizing time, logarithmic and order-ε coefficients are not found in the inspected general results.

## value

PASS

A reversible irreducible semigroup can show arbitrarily large W1 amplification on fixed unit graph distance before convergence. The full global peak and next-order expansion quantify a natural metastable transport pathology rather than just demonstrating one short-time expanding edge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
