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

# Verification protocol and limits

Execute `python3 verify.py` using only the Python 3.10+ standard library. The executable checker reconstructs stationary mixed age moments independently using the reset generator recursion: single-coordinate mean \(1/[r(1-w_i)]\) and, for a subset with at least two labels, moment equal to \(1/r\) times the sum of its lower-order deletion moments. It assembles exact mixed cumulants using all set partitions and checks the derived formula as rational identities for all subsets in several balanced, linearly varying and geometric probability vectors. It also checks the arithmetic-geometric-mean envelope, equality at balanced weights, and heterogeneous diffusion scaling. The saved source passed 798 exact rational checks.

The proof of stationarity, conditional independence, all-order differentiation and the sharp envelope is mathematical rather than computational; finite tests do not establish it for all dimensions, weights or cumulant orders. Uniform-weight stationary JPDF formulas are prior results. No independent review or external validation is asserted.
