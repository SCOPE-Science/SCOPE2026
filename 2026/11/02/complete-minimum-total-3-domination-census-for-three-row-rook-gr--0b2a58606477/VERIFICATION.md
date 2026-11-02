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

# Verification record

The proof in `RESULT.md` is a human-checkable argument covering all integers \(n\ge2\). Its critical equality is the exact count \(r_i+c_j-2x_{ij}\) of selected open neighbors of a cell. The row-two forcing lemma, size-eight and size-nine case partitions, and disjoint labeled counting are the decisive steps.

The bundled Python 3.9+ checker `verify.py` has no nonstandard dependencies. Run `python3 verify.py` in the directory of the extracted scientific files. It constructs each rook graph independently from its adjacency relation and checks every candidate subset of cardinality at most the predicted minimum for \(2\le n\le7\). It verifies the predicted total min-set count at each such size and the absence of smaller feasible sets.

A separate enumerator uses all eight possible three-row column masks and frequency compositions with exact multinomial coefficients for \(8\le n\le12\). It counts only feasible size-nine sets and compares with the claimed closed formula.

Observed execution:

```text
VERIFY_OK: 6 exhaustive graphs, 5 independent column-multiset counts
```

**Scope and limits:** The computational checks are bounded and do not prove the theorem for infinitely many lengths. The proof supplies the infinite reasoning. No independent formal proof assistant, external referee, or independent scientific audit has assessed this theorem. The numerical stabilization for \(n\ge5\) is already established in the cited 2017 article; originality pertains only to the full extremizer classification and counts.
