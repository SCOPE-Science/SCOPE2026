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

Run `python verify.py` using Python 3.8 or later and the standard library. The accompanying `verification_output.txt` is the captured output of this command; a successful replay ends with `VERIFY_OK`.

For each \(n\) from 2 through 13 the checker enumerates every nonempty proper subset and uses breadth-first search on the inverse-subset transition graph to find the shortest expansion length. Independently it calculates the first cyclic zero-to-one boundary, the predicted all-subset counts \(H_n(t)\), and the exact sets at threshold \(n\).

For each \(n\) from 2 through 8, a separate routine enumerates **forward word transformations** rather than reusing the inverse-state BFS. It verifies each shortest extending word is uniquely `b` followed by the prescribed number of `a` letters. Enumeration is finite, while the proof in RESULT.md proves the theorem for unbounded \(n\). No independent audit has been performed.
