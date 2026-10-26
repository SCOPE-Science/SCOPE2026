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

# Reproducible checks and limits

Run `python3 tournament_cyclic_checker.py` with Python 3 and no third-party dependencies. It enumerates every independent orientation of all edges on vertex sets of sizes \(n=3,4,5,6\) at \(p=1/4,1/3,1/2,2/3\). For every orientation it independently computes the directed-cycle count and evaluates the centered linear/quadratic identity, using exact rational arithmetic. For each of the 16 complete finite cases it also checks total probability, mean, and variance. The checker passed all 135,456 individual-state decomposition assertions and all finite moment comparisons.

Verification scope: the exact finite formulas are checked exhaustively only at the listed sizes and biases. The unrestricted finite formulas are proved by algebra and orthogonality, not by extrapolating this enumeration. The moving-bias Gaussian laws are proved analytically using fixed-order cumulant diagram bounds and the Lindeberg–Feller theorem; no finite computation certifies a limit theorem.

The independent audit channel has not produced an assessment.
