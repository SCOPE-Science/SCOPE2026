---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Decompose coverage K_n as a sum of present-symbol indicators A_i and the switch count T_n as adjacent inequality indicators I_j. Iid exchangeability makes each Cov(K_n,I_j) identical. For symbol probability p, P(A_i=0,I_1=1)=(1−p)^(n−2)[(1−p)^2−(s2−p²)], which algebraically yields Cov(A_i,I_1)=p(1−p)^(n−2)[2s2−(1+s2)p]. For U_t=Σp_i(1−p_i)^t and V_t=Σp_i²(1−p_i)^t, Cauchy–Schwarz gives V_{t+1}/U_{t+1}≤V_t/U_t≤s2. Therefore Cov(K_n,T_n)≥(n−1)U_t s2(1−s2)>0 for every n≥2 and nondegenerate finite iid law. For uniform p=1/m, substitution gives the stated exact special formula and conditional switch/coverage gap. Independently enumerated weighted words and verified exact rational mixed moments for uniform and heterogeneous m=2..4, n up to 5 (e.g. p=(1/2,1/3,1/6), n=5, covariance=173/486). The universal proof is the indicator calculation and Cauchy–Schwarz, not finite enumeration.

## originality

PASS

Best-of-knowledge original after mathematical claim-versus-prior comparison: The exact formula and strict sign need covariance between positional and occupancy indicators; such an identity is not automatically implied by separate run and urn concentration formulas. This is best-of-knowledge original, with implicit earlier mixed-generating-function risk. Explicit unexcluded risks and source-access limits are documented without claiming exhaustive novelty proof.

## value

PASS

This is an exact strictly signed cross-moment linking an order-invariant statistic (observed richness) to an order-sensitive statistic (run changes). It holds for every unequal finite categorical law, not just uniform occupancy, with a transparent conditional contrast and structural Cauchy–Schwarz mechanism; this is a naturally useful probabilistic coupling rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
