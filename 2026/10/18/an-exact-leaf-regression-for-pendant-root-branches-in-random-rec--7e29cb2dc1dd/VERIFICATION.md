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

The standalone program `verify.py` requires Python 3 and only standard-library modules. From the directory containing `verify.py`, run:

```sh
python verify.py
```

The program enumerates every one of the \((n-1)!\) recursive parent assignments for each \(2\le n\le9\), verifies the exact conditional mean for every realized value of \(Z_n\), checks the known rencontres marginal and the moment implications with rational arithmetic. It separately propagates both polynomial recurrences and checks the mixed invariant coefficientwise for \(2\le n\le25\). The expected output reports the exact number of assertions.

These are finite consistency tests, not the justification of a universal theorem. The all-size result follows from the four exhaustive transition cases, the two polynomial recurrences, their operator identity and coefficient comparison as written in `RESULT.md`. In particular, the \(n=2\) zero-variance edge case is excluded only from the correlation formula, not from the conditional regression.

The conditional variance and full conditional law are not determined here. The singleton-root-branch marginal was already available in the cited literature; it is verified as a needed input, not presented as an original theorem. No independent audit has been performed.
