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

The mathematical claim is proved in `RESULT.md`. The executable `checker.py` verifies the cut rank using three independently constructed finite matrices: literal original graph distance-four cuts; the Hamming distance-three convolution matrix; and multiplication in the truncated square-zero polynomial ring. It compares against the exact closed formula for dimensions \(4\le d\le11\), checking every coordinate cut for \(4\le d\le8\). There are 49 exact binary rank comparisons.

The checker separately constructs the complete \(d=4\), 16-qubit phase state from every controlled-\(Z\) edge, obtains a reduced density matrix, and verifies its entire nonzero spectrum numerically to tolerance \(2\cdot10^{-12}\). This is one direct density-spectrum test, and zero deviation in the recorded run. No extrapolation from a finite experiment is used in the proof.

Run `python checker.py` with the environment declared in `requirements.txt`. Observed output ends with:

```
PASS: 49 independent exact binary-rank comparisons and one direct density-spectrum test.
```

Unproved extensions include general bipartitions, other Hamming relations, noisy states and other local Hilbert-space dimensions. Historical originality remains subject to inspection of potentially relevant earlier modular Hamming-scheme literature. No independent scientific audit or certification has been performed.
