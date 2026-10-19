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

# Reproducibility and limits

Execute `python3 verify.py` with the Python standard library. The script enumerates all choices of the three tokens through generator time \(n=9\), aggregates exact rational map masses, checks distinct-map counts against a rational recurrence, validates parsing multiplicities and equiprobability, and checks the finite-time entropy chain rule at three rational weight triples to floating-point tolerance. It also checks the renewal entropy identity for a nonuniform triple, the equal-weight dimension, and the classical nonuniquely-decodable codeweight example. Its assertion count is \(33428\).

The program deliberately does not claim an exhaustive infinite-time proof. The semigroup growth law is proved by transfer generating functions, the entropy limit by the law of large numbers and Stirling's formula, and the dimension relation uses the cited published theorem. Source priority cannot be inferred from a finite semantic-search index. Independent external scientific validation has not been carried out.
