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

# Reproducibility checks

Run `python3 verify.py` with Python 3.10 or newer; it uses only the standard library and integer/fractional arithmetic. It computes the actual complete matching of each agent priority permutation and independently checks the closed multiplicity formula for every preference order when \(2\le n\le6\). It tests exact Pareto improvement by enumerating every competing matching when \(n\le5\). It checks all ordered-composition probabilities for \(2\le n\le7\) against exhaustive rankings without relying on the priority enumeration, verifies Stirling frequencies and exact means, and samples priorities at \(n=7,8\).

Observed output: 872 exhaustive exceptional preference profiles, 1,077,736 priority evaluations, 495,781 supported-matching comparisons, 15,016 independent Pareto-comparison checks, ordered-composition counts of \(2,4,8,16,32,64\) for \(n=2,3,4,5,6,7\), with final `PASS` and `COMPOSITION FREQUENCY PASS` messages.

Checks are finite. The theorem for all \(n\) rests on the four exact proof steps in `RESULT.md`, not on empirical extrapolation. Neither independent review nor any formal external certification is claimed. Results apply to a complete **joint matching lottery**, not only the agent/object marginal matrix.
