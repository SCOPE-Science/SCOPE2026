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
# Reproducible verification

Use Python 3 without external dependencies:

```sh
python verify_total_coalition_crowns.py
```

The corresponding output is supplied in `verify_total_coalition_crowns_output.txt`. All paths are relative to the enclosed artifact directory; both scripts and outputs are embedded fully. The checker uses graph adjacency, restricted-growth-string enumeration of unordered partitions, the two-coordinate coalition predicate, and an independent total-coalition graph degree-profile test.

It verifies \(21,824\) vertex subsets for \(3\le n\le7\) against graph adjacency; exhaustively enumerates all \(115,975\) vertex partitions for \(n=5\), finding maximum cardinality six and \(900\) extremizers; and for \(n=5,6,7\) exhaustively checks respectively \(22,827\), \(159,027\), \(752,752\) partitions of the candidate optimum size. Exactly \(900,3600,11025\) pass, all with opposite mixed triple classes and a double-star coalition graph. The checker is finite, while the general claim for every \(n\ge5\) follows from the independent symbolic proof in `RESULT.md`.

The earlier scalar value and the two-triple construction appear in the literature and are not claimed as new. No independent audit or external certification has been performed.
