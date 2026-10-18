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

# Reproducible checks

The independent `check.py` program uses only the Python standard library. Executing `python3 check.py` generates the data in `check_output.txt` and raises an assertion if any finite premise fails.

It constructs the exact complete length-\(18\) language using the \(28\) distinct windows of \(\mu^7(0)\); verifies equality under the complete length-\(18\) windows of every substituted element; checks an independent bit-index recurrence through \(8192\) positions; tests all images of length-\(10\) factors after one pass and all images of length-\(18\) factors after two passes; prints the complete small-length table and sharp collision witnesses. All reported checks succeeded.

The universal step is separately proved in RESULT.md: injectivity on all length-\(m\) factors containing at least \(k\) ones implies injectivity on every longer factor. The finite program checks hypotheses of that lemma but cannot itself establish all infinite cases. Originality searches do not constitute independent priority verification. No independent scientific audit or validation has been performed.
