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

The portable checker `verify.py` and the 162-row `CERTIFICATE.tsv` are bundled with this finding. Run `python verify.py` from the same directory. It reconstructs the recurrence exactly, compares it with direct \(S_3\)-permutation evaluations for every binary word through length \(13\), checks each certificate witness, and verifies that both transitions permute the full 162-state signature set. The universal statement beyond length \(13\) depends on the bijection proof in `RESULT.md`, rather than on further sampling.

Checks completed successfully in the provided environment. The verification is self-review and computational; independent scientific audit was not performed. The evidence does not establish novelty against inaccessible or unindexed literature.
