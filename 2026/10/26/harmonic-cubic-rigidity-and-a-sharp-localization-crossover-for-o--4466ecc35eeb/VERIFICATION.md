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

Run `python3 verify.py` with a standard Python 3 interpreter; no third-party package is required. The program enumerates all 3 pair partitions of four positions and all 15 pair partitions of six positions, evaluates the exact rational contractions and harmonic variance in dimensions 2, 3 and 4, checks pure-trace determinism, verifies a rational two-dimensional orthogonal rotation, and checks both strict rank-one orderings for dimensions 2 through 100.

Observed output on the packaged source:

```text
n 2 rank-one crossover 5/8
n 3 rank-one crossover 3/7
n 4 rank-one crossover 5/16
PASS 108 exact tensor/crossover test cases, plus strong-convexity samples
```

These are finite algebraic checks. The theorem for all dimensions and all symmetric tensors follows from the sixth spherical moment identity and its tensor-pairing proof in `RESULT.md`. The absolute mathematical publication priority and independent scientific audit have not been established.
