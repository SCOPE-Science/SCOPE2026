---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The induced return-time model gives the positive pressure root sum_{k>=0}exp(-beta A_k-P(k+1))=1, including the zero-marker fixed measure (pressure 0). With b=exp(-beta c zeta(p)), split the excess over the geometric tail into k=0, k=1, k>=2 and a long tail k>=beta^a with a>1/(p-1). For 1<p<2 the long-tail Mellin sum is c Gamma(2-p)/(p-1)*beta*b^(p-1); the k=1 term is exp(-beta*c*(1+2^-p)). The remaining k>=2, denominator expansion O(R^2+b), and cut-off middle terms are lower order than the smaller competing exponent. For p>=2 the tail is lower order than k=1. Gamma stochastic ordering proves (p-1)zeta(p) strictly increases and meets 1+2^-p once. At equality the beta prefactor determines the winner. Verified numerical critical root p*=1.553201524280211. No uniformity for varying c or p claimed.

## originality

PASS

Best-of-knowledge source-comparison judgement: claim is not shown to be a restatement or corollary of the actual inspected antecedents. No inspected prior implication yields the second correction; the known root equation is only the starting identity.

## value

PASS

The exact second correction and the phase crossover distinguish finite short excursions from the accumulated effects of polynomially many distant return lengths, a natural feature of renewal thermodynamics not determined by the leading Arrhenius pressure scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
