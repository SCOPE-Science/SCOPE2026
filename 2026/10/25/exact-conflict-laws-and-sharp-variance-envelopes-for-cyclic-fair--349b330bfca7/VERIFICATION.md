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

# Reproduction and checks

Run `python3 verify.py` from this directory using Python 3.8 or later; it requires only standard-library modules. The observed output was:

```
VERIFICATION_OK 1353 exact checks; triangle distribution {3: 2, 1: 6}
```

The program exhausts feasible histogram vectors for \(n=2,3,4\) and checks both claimed sharp variance values at every feasible edge total. It enumerates all independent block shifts to check expectation and variance for sampled finite interaction graphs with \(2\) to \(4\) blocks; where those graphs are forests, it separately checks the distributional convolution formula. It exhaustively checks pairwise uniformity of differences among block pairs in four-block systems for \(n=2,3,4,5\). Finally, it checks the exact cycle-law obstruction.

The finite test does not prove the theorem for arbitrary numbers of blocks or agents; that follows from the Fourier-orthogonality, independence, and integer-extremal arguments in `RESULT.md`. The general Fourier flow formula is proved algebraically in the text rather than tested through symbolic root-of-unity arithmetic. No independent external audit has been performed.
