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

# Reproducible checks and limits

Run `python3 verify.py` with any standard Python 3 installation. The script has no external dependencies.

The independent direct enumerator constructs all assignments of minimum candidate weight and explicitly checks every zero vertex's four neighbours on labelled square cycles for \(5\le n\le18\). It matches the stated count and confirms the sole double-labelled minima in these finite cases.

A separately constructed cyclic four-position transfer uses state tuples of labels in \(\{0,1,2\}^4\). Its transition validates the middle vertex's neighbour-sum inequality and adds the new label's weight. Traces of closed walks at each length enumerate labelled cyclic words. The minimum weight and multiplicity agree with the theorem for all \(5\le n\le60\).

The checks actually completed and printed:

```
INDEPENDENT_DIRECT_ENUMERATION_OK 14 orders n=5..18 (all assignments of minimum weight)
INDEPENDENT_CYCLIC_TRANSFER_OK 56 orders n=5..60; optimal weight and count
SPECIAL_TWO_LABEL_COUNTS_OK n=5:5 n=10:5 others:0 through n=18
FINITE_VERIFICATION_OK; proof of the infinite theorem is in RESULT.md
```

The infinite formula follows from the mathematical argument in RESULT.md. No exhaustive infinite search, automated formal proof, comprehensive historical-priority certification, or independent scientific audit has been performed.
