---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Write mass a_k=binom(n,k) A u^k (1+tr^k); exact neighboring ratio equals k(n-k)/((k+1)(n-k+1))*(1+Delta*z_k/(1+z_k)²). Substituting LC and ULC definitions gives sharp pointwise tests. The scalar z/(1+z)² maximizes at z=1 with value 1/4 and every index can reach z=1 by a weight 0<w<1, establishing necessity and sufficiency and equality. Max n-k occurs k=1; max k(n-k)=floor(n²/4). Log-concavity of continuous curvature profiles (strict negative second log derivatives) makes failure indices a consecutive block; endpoints n=2 checked.

## originality

PASS

Kella and Löpker treat general binomial mixing and thinning, not sharp two-atom LC/ULC odds gap membership. General concentration of known ULC laws, and synchronicity sufficient criteria for mixtures, do not settle necessary-and-sufficient thresholds. Search considered equivalent formulations using latent Bernoulli exchangeability and binomial coefficient normalization.

## value

PASS

Exact robust shape thresholds and a single-band violation theorem for a canonical positively dependent exchangeable count family answer natural membership questions, enabling rigorous use of LC/ULC bounds without independence assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
