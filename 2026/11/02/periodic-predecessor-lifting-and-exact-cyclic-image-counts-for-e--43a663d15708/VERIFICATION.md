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

Execute the adjacent standalone Python file `verify.py` using standard Python 3:

```
python3 verify.py
```

Expected terminal confirmation: `VERIFY_OK`.

The check independently enumerates every binary ring input and every output through length \(18\); compares exact image counts against the closed formula; computes the forbidden-subword transfer matrix through length \(120\); exhaustively checks parity-signed cyclic two/three-one-run classes through length \(15\); and explicitly constructs minimal repeated-ring predecessors for every `010`-avoiding output through length \(13\). Successful replay produced `VERIFY_OK` and counts `1,2,2,6,12,23,37,66,119,217,387,693,1237,2207,3927,6986,12412,22028,39047` for lengths \(1\) through \(19\).

These finite checks do not establish an infinite theorem by themselves; the all-length analytical argument appears in `RESULT.md`. No independent audit, machine-checked proof formalization, or comprehensive historical-priority certification has been performed.
