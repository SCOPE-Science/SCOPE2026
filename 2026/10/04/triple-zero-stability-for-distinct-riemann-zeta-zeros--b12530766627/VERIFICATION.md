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

The exact-arithmetic replay is `python3 verify.py`. It verifies the parameter identities and inequalities used after the two source assumptions are stated, including the maximal-block obstruction at \(m=348\).

The replay does not certify the source's pair-correlation energy evaluation or its computer-assisted seven-point local inequality. Those are explicit assumptions of the number-theoretic consequence. The generalized Gram lemma and the counting reduction are proved symbolically in `RESULT.md`; the script checks their instantiated rational constants rather than replacing the proof by numerical experimentation.
