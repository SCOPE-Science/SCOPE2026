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

The executable `verify.py` uses only the Python standard library. Run `python verify.py` in a directory containing the file. It checks rational endpoint embeddings, exact one- and two-sided leakage identities, and an exhaustive finite rational grid of the one-sided \(2\times2\) angular bound. The assertions compare rational numbers, not toleranced floating-point logs. The general matrix lemma, all dimensions, and the optimality for arbitrary real distortions are established analytically in RESULT.md; finite checks alone do not certify them. No independent audit has been performed.
