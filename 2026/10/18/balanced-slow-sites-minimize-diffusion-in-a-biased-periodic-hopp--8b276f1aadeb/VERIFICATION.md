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

# Reproducibility and checks

Run \(\texttt{python3 verify.py}\) in a directory containing the companion script. Python's standard library suffices. All calculations use exact rational numbers. The script independently forms the periodic Markov generator, solves its stationary Poisson equation, computes the variance of the corrected displacement martingale, and compares it with the new closed pair-kernel expression. It also exhaustively checks small cyclic binary configurations against all claimed extrema.

Observed output on execution:

```
PASS: 336 independent generator/Poisson comparisons; 56 complete pairwise extrema enumerations; 56 zero-bias/one-way ordering-invariance comparisons.
```

The finite enumeration ranges over \(4\le n\le10\), \(2\le m\le n-2\), with exact-rational biases \(p=3/4\) and \(p=2/3\) for the strict-extremum tests. The generator comparisons also include \(p=1/2\) and \(p=1\). The unlimited-period theorem depends on the separate martingale-corrector identity and cyclic convexity proof, not on finite testing. No independent audit or formal machine proof has been performed.
