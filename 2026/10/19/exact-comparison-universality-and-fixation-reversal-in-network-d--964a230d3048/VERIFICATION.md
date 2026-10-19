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

# Reproducibility and verification

Run `python verify.py` under Python 3. The script has no nonstandard dependencies and uses exact `fractions.Fraction` arithmetic. Its checks include (i) connected labeled graphs with two through five vertices, counted as \(1,4,38,728\) graphs, (ii) 54 fixation calculations and strict sign checks for exact rational fitness ratios, (iii) all \(160\) combinations of 32 configurations and five death neighborhoods on \(K_{2,3}\), and (iv) an explicit four-vertex path with changed comparison payoff contrast.

The small-graph census does not certify arbitrary graph orders, and the finite tests do not prove a stochastic process theorem. The analytic proof in `RESULT.md` supplies the all-size and all-parameter classification. The absorption probability follows from the explicit birth–death recurrence, not Monte Carlo sampling. The mathematical meaning of complete bipartite is \(K_{a,d}\) with nonempty parts; the two susceptibility constants may be distinct and of either sign.

No independent scientific audit or outside replication is asserted here.
