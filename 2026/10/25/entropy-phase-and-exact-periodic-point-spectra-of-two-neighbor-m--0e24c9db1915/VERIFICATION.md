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

# Verification and limits

Run `python3 verify.py` using Python 3.10 or later; only its standard library is needed. The checker independently enumerates all independent residue masks for moduli 3 through 16 and checks cyclic-rotation orbit counts and periods. It enumerates every n-periodic binary word for moduli 3 through 12 and periods 1 through 12, testing forbidden congruences over the full common period and comparing with the exact formula. The tests are exact integer computations and are reproducible from the embedded standalone source.

Finite enumeration cannot prove statements for all moduli or periods. The unrestricted proof is the residue-mask reduction, unique Bernoulli maximization on each cyclic phase orbit, cyclic-gap enumeration, and the independent finite-composition formula for periodic words. Historical priority relative to a full-text-inaccessible 2015 article and any unindexed equivalent statement remains unresolved. No external independent audit was performed.
