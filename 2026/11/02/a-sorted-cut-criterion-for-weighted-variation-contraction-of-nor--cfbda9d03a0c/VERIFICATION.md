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

# Reproduction and limits

Run `python3 verify.py` using the script supplied with the mathematical statement. It requires only Python 3 and uses `fractions.Fraction` for all decisive values. The verifier checked 276 independently sampled positive integer weight arrays with \(q\in\{1,\ldots,7\}\), 25,728 exhaustive binary cuts in those arrays, 12,576 exact-rational forward-Euler inequalities on certified contractive instances, and the \(K_{2,3}\) counterexample with initial variation \(3\), derivative \(1/6\), and one Euler-step gain \(1/96\).

The computation does **not** prove the infinite family or the continuous-time statement. Those follow from the cut derivative formulas, cut exhaustion, nonnegative coarea decomposition, and the finite-dimensional exponential limit detailed in `RESULT.md`. No independent scientific audit has been performed.
