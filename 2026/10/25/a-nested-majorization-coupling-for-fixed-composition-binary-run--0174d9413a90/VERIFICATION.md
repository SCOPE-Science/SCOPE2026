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
# Verification

## Proof checks

The conditioning counts are \(2\binom{a-1}{t-1}\binom{b-1}{t-1}\) and, at odd levels, the two binomial products in the proof. The transition ratios match those counts exactly. Insertion of a uniformly chosen unused cut sends a uniformly chosen \(k\)-element subset of an \(n\)-element set to a uniformly chosen \((k+1)\)-element subset, because each target has exactly \(k+1\) predecessors. Splitting \(u+v\) changes the quadratic sum by \(-2uv\), with \(u,v\ge1\). The generating-function coefficient yields the independent conditional expectation formulas.

## Reproduction

Run `python verify_runs.py` using Python's standard library. Observed output:

```
PASS: 49 (a,b) pairs, all binary words, all attainable run counts,
all longest-run thresholds, exact conditional Q, and exact cut kernel states.
```

The script enumerates all fixed-content words with \(1\le a,b\le7\), compares exact rational conditional expectations against the formulas, compares every adjacent conditional longest-run tail, and independently constructs and checks every intermediate distribution of the stated cut-growth kernel. This is finite corroboration; the proof is the general argument in `RESULT.md`.

## Limits

These checks do not prove anything about nonuniform content probabilities without conditioning, more than two symbols, or any location-sensitive run statistic. The independent audit is not performed.
