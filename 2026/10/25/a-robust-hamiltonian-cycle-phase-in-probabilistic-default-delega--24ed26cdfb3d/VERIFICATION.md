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
# Verification

The proof in `RESULT.md` is the basis for the general theorem. Its critical steps are the path probability product, bounded ideology penalty, best cycle-transfer deviation for multiple cycles, predecessor-to-tree deviation for the unique nonspanning cycle, and exhaustive three-voter best-response algebra.

Run `python3 verify.py` with Python 3 standard library. The checker passed 8,027 exact-rational assertions. It independently reconstructs expected payoff by enumerating independent participation outcomes for graphs with up to four voters, exhaustively compares predicted Nash equilibria to all profiles through five voters for selected strict-diameter instances, and checks rational three-voter threshold points including equality.

Finite enumeration does not prove a theorem for every electorate size or real parameter. The analytic proof covers arbitrary finite numbers of voters and arbitrary nondegenerate independent turnout probabilities. No independent audit, external certification, or infinite mechanical proof was performed.
