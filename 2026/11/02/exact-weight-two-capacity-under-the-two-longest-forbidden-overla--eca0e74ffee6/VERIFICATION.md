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

# Reproducibility and limits

Run `python3 verify.py` with a standard Python interpreter. The program constructs the proposed codes and compares their sizes to the formula for lengths \(4\) through \(120\). It directly compares every ordered codeword pair for lengths \(4\) through \(20\), checks all weight-preserving successors corresponding to the two forbidden overlaps up to length \(120\), and computes exact conflict-graph independence numbers for lengths \(4\) through \(8\). Successful execution ends with `VERIFY_OK`.

Observed output:

```
EXACT_OPTIMA [(4, 1), (5, 2), (6, 5), (7, 6), (8, 7)]
DIRECT_FACTOR_CHECKS_4_TO_20_OK
NEIGHBOR_CHECKS_4_TO_120_OK
VERIFY_OK
```

A separate exact mixed-integer search of the full conflict graphs for lengths \(4\) through \(22\) matched the theorem. Those searches are not needed for reproduction and are not used as an infinite mathematical certificate. The all-length proof in `RESULT.md` is based on exhaustive structural case analysis of arbitrary shifts, not extrapolation from these checks.
