---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed h_k-g_k=z/(1-z)^2 and h_k integral in w=1-z with epsilon=1-k. The rescaling epsilon^3 h_k(1-epsilon y) has derivative -(2-epsilon y)/(y^3(1+(1-epsilon)y)); its positive-real integration constant converges to H(y)=y^-2-2/y+2log(1+1/y), whose derivative is -2/[y^3(1+y)]. Since g_k=h_k-Koebe, epsilon^3F_k -> 2Re H, not H alone. On the disk, |F_k(z)|<=C/(d^2(epsilon+d)), d=|1-z|, from straight-segment integration. Polar scaling r=1-epsilon x, theta=epsilon t gives majorant x^beta/[(x+|t|)^(2q)(1+x+|t|)^q]; integrable near origin exactly when 2q<beta+2, and at infinity when 3q>beta+2. Hence dominated convergence proves the full strictly positive finite coefficient for fixed beta,q. Independent SymPy differentiation and four direct positive-real integral evaluations confirmed profile convergence. The derivative/majorant argument, not finite quadrature, proves the infinite limit.

## originality

PASS

Best-of-knowledge noncoverage after comparing the precise statements and implications, original scope, related general theorems and aliases, with the specific residual priority limitations below; lack of a search hit is not itself evidence of novelty.

## value

PASS

The explicit canonical shear changes from order-two boundary growth at fixed distortion to order-three growth at limiting distortion. The open exponent window is mathematically natural: each finite-parameter weighted moment is finite but the limiting harmonic Koebe moment diverges. An exact two-dimensional profile and leading coefficient quantify the singular crossover, and no whole-class extremality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
