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

The analytical convergence proof is given in `RESULT.md`. The independent script `verify_edge.py` (Python with NumPy) simulates Bernoulli reversal sequences, checks their last-reversal cumulative probabilities against the exact independent-product expression, and evaluates deterministic sample-path bounds on the distance from the ballistic edge. The script tests three \(c\)-values at \(N=300000\), with 1200 trajectories each and four cumulative-probability checkpoints, all meeting a 0.06 absolute Monte Carlo tolerance. The finite tests cannot prove a convergence theorem; the proof uses Poisson point-process convergence and the deterministic reversal-count squeeze. The experiment treats only the exact rate \(p_k=c/(k\log k)\) after the first three steps, while the theorem covers all independent rates with the same asymptotics. No independent audit has been performed.
