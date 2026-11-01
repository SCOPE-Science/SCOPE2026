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

# Computational verification and precise limits

The exact analytic proof is in `RESULT.md`; the two programs listed here are reproducibility checks, not a replacement for proof.

`python3 verify/rank_verifier.py` constructs the binary adjacency matrix of the complement of every selected disjoint cycle union. It independently multiplies matrix powers, uses exact binary pivot elimination, and checks the formula for \(\dim\ker F^t\) through two steps beyond the predicted stabilization time. The complete test family has 2,094 cycle multisets with each cycle length from 3 to 16, up to four components, and total order at most 40. Its recorded stdout is `verify/rank_output.txt`.

`python3 verify/orbit_verifier.py` builds each permitted graph directly from its missing edges, exhaustively constructs the deterministic successor map, detects periodic orbits and transient chains, and checks the exact first-entry counts against the analytic formula. This covers 83,136 binary configurations across sixteen cycle-size multisets; its stdout is `verify/orbit_output.txt`. The programs use logically distinct checks (matrix ranks versus individual trajectories).

The full theorem covers every number of cycles, unbounded cycle lengths, and every finite field of characteristic two. Neither finite checker, even when both pass, establishes those infinite quantifiers. Those follow from the cyclic polynomial-kernel calculation, the treatment of the all-ones rank-one coupling, and finite-vector-space Fitting decomposition in the written proof. Eventual primitive periods and individual basin structures are not calculated.
