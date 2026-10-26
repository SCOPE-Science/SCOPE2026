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

The proof uses a size-independent exact finite-state reduction with 676 support pairs and 2808 tagged-vertex states. The verifier enumerates every transition in that reduced state space, checks entry and primitive periods, and exactly compares the two monomial polynomial identities. The same script separately enumerates 94,770 actual labelled initial configurations on six selected graph sizes using the literal vertex update. Witnesses certify the sharp transient and the existence of both nontrivial periods.

Run `python3 verify.py` using Python 3 standard library; compare its output with `verification_output.txt`. The observed last line is `VERIFY_OK`.

The finite-state computation is part of the exhaustive proof of a proven finite quotient. The smaller vertex-level samples are corroboration, not a substitute for all-size proof. Independent audit is not performed.
