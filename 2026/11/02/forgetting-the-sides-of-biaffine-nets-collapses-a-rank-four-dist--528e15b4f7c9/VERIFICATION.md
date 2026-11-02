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

# Reproducibility

Run `python3 verify_biaffine.py` and `python3 independent_direct.py` with a standard Python 3 installation. No external libraries are required. The recorded output is in `verification_output.txt`.

The first program uses the five ordered-pair orbit positions for the Desarguesian net, recursively forming the exact possible atomic extension diagrams after the third selection. It checks pure and side-named rank-four root types for field orders \(2,3,4,5,7,8,9,11,13,16\), including explicit fields of orders \(4,8,9,16\). The second program constructs the adjacency matrix afresh and enumerates all ordered vertex pairs and later continuations without using orbit reductions at field orders \(2,3,5\). Each program compares the actual nested type objects, not only their hash values.

The verification establishes concrete finite instances, not infinitely many orders or non-Desarguesian cases. Those depend on the proof's complete five-case local incidence classification and fourth-neighbor counting bounds. The converse separations have explicit rank-four sentences. No independent external audit has occurred.
