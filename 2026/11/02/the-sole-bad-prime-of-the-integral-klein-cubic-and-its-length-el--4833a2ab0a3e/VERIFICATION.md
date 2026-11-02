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

The standard-library verifier `verify_klein11.py` checks characteristic-specific identities, finite rational singular loci for five small primes, and exact Hessian rank. It is supplementary: uniqueness over algebraic closures follows from elimination in the proof, and smoothness at every other prime follows from the product of the five gradient equations. The local Tjurina-algebra isomorphism follows from exact elimination after inverting the nonzero coordinate \(u\), not a finite-field point sample. The arithmetic geometry of alternative integral models is not tested.
