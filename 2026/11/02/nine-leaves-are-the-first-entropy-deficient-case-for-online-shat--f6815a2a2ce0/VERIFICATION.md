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

The `certificates.json` file records the exact tree and complete adaptive decision-tree witness for each integer leaf count from two through ten, including the 31-query, 32-terminal-witness certificate at ten leaves. Execute `python verify_cert.py` with Python 3 from the extracted file directory. This reconstructs each leaf-pair path by an independent breadth-first traversal and checks every query answer and unique terminal witness; it also computes each displayed finite online rank with a fresh immutable-set recurrence. The program enumerates the integer component-size partitions of nine and confirms that only \((3,6)\), \((4,5)\) and \((1,2,6)\) could start a depth-five tree.

`make_cert.py` is a separately represented, bitmask-based generator for the same certificates. It uses no external dependencies. The universal impossibility proof for nine leaves is the argument in RESULT.md: the programs check its finite partition list but do not independently certify its case-analysis lemma for every arbitrarily subdivided tree. No claim is made for more than ten leaves, and no independent audit has been performed.
