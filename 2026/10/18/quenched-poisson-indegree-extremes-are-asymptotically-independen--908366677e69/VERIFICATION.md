---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Conditioning on a feasible exact labeled history of T=m fixes precisely m iid map coordinates and puts no constraint on the remaining n-m coordinates. Its prescribed targets have at most one double hit. A coupling through the free allocation charges at most m b_(n,k-1)+b_(n,k-2) for imposing the prescribed targets and m b_(n,k-1) for completing the same free outputs with fresh uniform targets (each fresh target is independent of prior occupancies). Averaging conditional TV is exactly the TV against the product with the same H marginal. Summing the birthday survival product bounded by exp(-t²/(2n)) gives the stated mean bound. In the rare-threshold regime p_k=Pr(Pois(1)≥k)~e^-1/k! gives k~log(n)/loglog(n) and the shifted binomial tails have orders k/n and k²/n. The multinomial-to-product-Poisson ratio is bounded by e^q (zero off feasible count vectors) and tends to one near all q fixed occupancies at k. Conditional on the Poisson tails, the excesses vanish in probability, giving the factorial moments λ^q; the Poisson law is moment-determinate. Expanding the birthday survival product at t=O(√n) gives the Rayleigh limit; J|T is discrete uniform, and (UR,(1-U)R) has the stated density by the Jacobian R. TV contracts under projection to the two lengths and supplies the joint independence, including the zero-count event.

## originality

PASS

No inspected result covers the quantitative product estimate for the entire stopped labeled history against the global growing-threshold count. Credit the classical orbit and occupancy marginals separately; the supported distinct contribution is their quantitative decoupling at the full-history level.

## value

PASS

The result answers whether conditioning on an entire birthday-scale orbit affects the globally rare indegree count, not just whether two normalized summaries have separate marginal limits. The explicit uniform-in-h conditional bound depends on T(h) and gives a useful decoupling rate after averaging; the Poisson/Rayleigh joint limit is a meaningful consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
