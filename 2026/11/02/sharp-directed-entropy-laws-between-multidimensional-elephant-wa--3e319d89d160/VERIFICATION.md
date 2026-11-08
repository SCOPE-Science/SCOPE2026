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

For conditional counts Delta_k, q_theta,k(j)=1/D+theta Delta_k(j)/k. The exact KL chain rule and uniform-positive-simplex Taylor expansion reduce KL to D(alpha-beta)^2/2 sum S_k/k^2 plus a cubic remainder. The exact recurrence S_{k+1}=(1+2alpha/k)S_k+(D-1)/D has the stated gamma/harmonic solution; martingale Azuma tail integration bounds the third moments, making the remainder O(1) for alpha<=1/2 and lower-order above. Check boundary alpha<1/2, =1/2 and >1/2, fixed interior domain, and reversal of parameters. Independent D=4 rational moment checks passed 28 cases, not an infinite proof.

## originality

PASS

Best-of-knowledge distinct mathematical claim after direct model/parameter and implication comparisons; known overlapping prerequisites and specializations credited. The known q_theta formula plus exact moment recurrence are shared lemmas, but a mere O-bound on D(P_alpha||P_0) cannot imply constants for D(P_alpha||P_beta), nor the directional ratio. Local LAN/LAMN does not cover fixed-separated alpha,beta without uniformity and integration. The paper reconstructs a self-contained second-moment/Taylor derivation.

## value

PASS

The full-history KL is a natural information-geometric invariant of the original elephant walk; Qin previously bounded its order against an independent comparator. Exact constants for two arbitrary fixed memories and a sharp finite-to-unbounded directional-asymmetry transition identify a nontrivial mechanism needed for likelihood comparison and distinguish full trajectories from endpoint marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
