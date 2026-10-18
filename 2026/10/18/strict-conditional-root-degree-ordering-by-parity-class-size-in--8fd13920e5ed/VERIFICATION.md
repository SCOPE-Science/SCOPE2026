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

The standalone `verify.py` was executed against the reviewed formulas. It performed 340 exact arithmetic assertions: enumerated all Prüfer codes for orders 2 through 7, reconstructed the even-distance color class and root degree for each, and checked every exact class probability and shifted binomial conditional mass. It also checked strictly ordered conditional survival functions and mixed moment identities, plus the complete bipartite excess-degree count for chosen root-containing color sets. Output: `VERIFIED 340 exact assertions`. These are finite tests and do not constitute a universal proof. The proof is the complete bipartite weighted degree enumerator, mass-ratio monotonicity, and Poisson limit in `RESULT.md`. No external or independent audit has been performed. The 1962 Scoins paper remains an accessible-abstract-only historical priority risk.
