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

The factorization follows from the proved cut-vertex and cycle-omission lemmas; exhaustive finite testing is an independent check, not an infinite proof.

Run `python verify_cactus.py` with `networkx>=3.3,<4` installed. The verifier directly enumerates nonempty subsets, independently tests induced connectivity and domination, computes block-factor coefficients, and compares the full coefficient vectors. It also evaluates discriminants on randomly constructed longer cactus graphs.

The recorded output `verification_output.txt` reports 103 nonisomorphic atlas cacti, 720 random cacti of orders 8–15, 6,280,063 tested candidate subsets, 7,105 further cycle-block discriminant checks, and explicit triangle and square identities. Random tests use a fixed seed. The verification covers the enumerated finite inputs only and does not certify the theorem's infinite range or rule out prior discovery. No independent audit has been performed.
