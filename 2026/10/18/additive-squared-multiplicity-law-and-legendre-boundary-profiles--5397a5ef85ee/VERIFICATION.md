---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For H² and f=c∏(z−ζ_j)^{m_j} with ≥2 fixed distinct unit-circle nodes and at least one repeated zero, polynomial residual R=1−fq_n has exact Euler jet constraints (E^ℓR)(ζ_j)=δ_(ℓ,0). Evaluation matrix A_(jℓ),k=k^ℓ ζ_j^k for k=0..K−1 (K=n+d+1) has full row rank by Hermite interpolation; min-norm coefficients equal a=A*(AA*)^(−1)b. Scaling its Gram by D_K,jℓ=K^(ℓ+1/2) yields block diag H_(m_j) plus O_f(K^−1): diagonal Hilbert moment blocks from Riemann sums and cross-node oscillatory sums O(K^(ℓ+v)) by summation by parts. Positive block inverse perturbation gives K||a||²=Σ(H_m^(−1))_00+O_f(K^−1). The Hilbert inverse first column is the shifted-Legendre evaluation-at-zero reproducer Q_m(t)=Σ_(ν<m)(2ν+1)(−1)^νP_ν(2t−1), with Q_m(0)=m²; thus ||a||²=(Σm_j²)/K+O_f(K^−2) and the simultaneous all-index profile Ka_k=Σconjζ_j^k Q_(m_j)(k/K)+O_f(K^−1). Independent exact Hilbert inverse first entries 1,4,9,16 (m=1..4) and normalized finite mixed-multiplicity Gram residuals converge toward 5 and13. Uniformity is in 0≤k<K with fixed nodes, not coalescing nodes.

## originality

PASS

The nearest 2019 primary paper provides the finite matrix kernel method, simple distinct boundary zeros and a single higher-order boundary zero; concluding remark 8(G) explicitly treats different boundary zeros with different multiplicities as a future direction. The inspected material does not give the mixed-jet decoupled Σm_j² constant or the uniform oscillatory full coefficient profile. Known general confluent Christoffel/derivative-kernel ideas could potentially imply related asymptotics, a documented risk.

## value

PASS

Repeated boundary zeros control inverse-filter approximation difficulty; the leading constant is quadratic in multiplicities rather than linear, and the result identifies the complete shape of every residual coefficient with explicit Legendre profiles. This gives a natural sharp quantitative extension of simple-root Hardy approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
