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

The standalone Python 3 verifier uses independently constructed rook-graph open-neighborhood bitmasks and memoized exhaustive search. It checks \(2\times n\) for \(2\le n\le7\), \(3\times n\) for \(3\le n\le6\), and \(4\times4,4\times5\). Both the extremal length and the exact exceptional ordered-sequence counts match; every optimal sequence on the \(2\times3\) and \(3\times4\) boards satisfies the proved structural description. Output ends with `VERIFY_OK`.

Command: `python3 verify.py`. The checker uses no external packages. This is finite supplementary evidence; the exact all-parameter result is proved in `RESULT.md`. The search for earlier results cannot certify definitive novelty, and independent audit has not been performed.
