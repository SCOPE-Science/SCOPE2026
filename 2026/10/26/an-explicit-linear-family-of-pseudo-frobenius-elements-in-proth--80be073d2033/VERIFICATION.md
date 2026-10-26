---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The self-contained `verify.py` uses Python standard library shortest-path computation of the complete Apéry sets for n=3,...,10 and exact residuewise comparison with greedy coin minima. It computes all pseudo-Frobenius elements in those examples and checks the n+2 formula witnesses. These finite experiments are not an infinite proof; see the coin and popcount argument in RESULT.md. No independent audit has been conducted.
