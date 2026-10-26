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

The proof relies on the exact expected-payoff expression in the motivating paper, strict convexity of its two-geometric-term difference, endpoint signs, and matched boundary-layer limits. The finite integer-group-size classifications follow from elementary one-variable sign arguments, not from fitted trajectories.

`verify.py` uses exact rational arithmetic for all sign and finite-parameter threshold checks. It also illustrates limiting root locations using high-precision decimal bisection. For \(n=96\), exact rational sign brackets isolate both interior roots while \(p_n=(5/6)^{96}\). The test suite covers \(L<1+\delta\), \(L>1+\delta\), and all three critical-amplitude branches at \(L=1+\delta\).

The finite computations do not establish the infinite-\(n\) claims; those are proved by the explicit limits and monotone root bracketing in `RESULT.md`. No uniform finite-size error constants, finite-stochastic-population fixation probabilities, or independent scientific validation are claimed.
