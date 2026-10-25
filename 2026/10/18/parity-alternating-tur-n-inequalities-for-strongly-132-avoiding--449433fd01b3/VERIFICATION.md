---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Use Archer–Graves Theorem 1.2 exact A(z)=P(z)(F(z)+G(z)). Strict Catalan coefficient estimates keep P analytic beyond |z|=1/2 and G analytic there; F=2(1−z)/(1−2z+sqrt(1−4z²)) has sole boundary singularities ±1/2. At +1/2 its leading nonanalytic term is P_+/sqrt2 (1−2z)^−1/2; at −1/2 it is −3sqrt2 P_-/4 (1+2z)^1/2. Singularity transfer yields a_n=K2^n n^−1/2(1+(α+β(−1)^n)/n+O(n^−2)), K=P_+/sqrt(2π), β=3P_-/(4P_+)>0. Adjacent multiplication gives T_n=(−1)^n(3P_+P_-/(2π))4^n/n²+O(4^n/n³), not a claimed finite threshold. Independently generated 90 coefficients; first 16 matched primary table, parity held n=8..89, constant independently evaluated 1.9514080909277811.

## originality

PASS

The exact published generating function determines the coefficients, but the eventual alternating second multiplicative difference is not among the published results and requires retaining and comparing a previously unanalysed weaker negative singularity with the positive one. The source’s first-order asymptotic alone cannot decide adjacent Turán signs. Novelty is a nontrivial analytic refinement, not enumeration or an all-n sign claim.

## value

PASS

An eventually alternating strict log-concavity/log-convexity law and its explicit leading curvature defect give qualitative asymptotic shape information not supplied by the growth rate, motivated by the recently enumerated strong pattern-avoidance sequence. The negative singularity dominates a delicate second difference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
