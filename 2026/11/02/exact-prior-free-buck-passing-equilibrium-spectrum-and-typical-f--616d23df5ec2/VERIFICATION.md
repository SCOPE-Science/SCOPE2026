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

# Verification details

`verify.py` is a standalone standard-library Python script. It enumerates all outgoing-neighbor choices of every vertex for each of \(K_{1,1}\), \(K_{1,5}\), \(K_{2,2}\), \(K_{2,3}\), \(K_{2,4}\), \(K_{3,3}\), \(K_{3,4}\), and \(K_{4,4}\). It computes exact-rational long-run cost from each player's cycle and basin, tests every unilateral outgoing-neighbor change, checks whether equilibrium is equivalent to a unique cycle with depth-one-or-zero vertices, and checks every coefficient of the counting formula. Total complete profiles enumerated: 71,799.

Recurrent-cycle half-length equilibrium counts are: \(K_{1,1}\): [1]; \(K_{1,5}\): [5]; \(K_{2,2}\): [4,2]; \(K_{2,3}\): [6,12]; \(K_{2,4}\): [8,48]; \(K_{3,3}\): [9,72,12]; \(K_{3,4}\): [12,288,144]; \(K_{4,4}\): [16,1152,1728,144]. The script checks numerical positions of the maximizing term for balanced sizes 10, 20, 50, 100, 200, and 500. Its terminal success marker is `EXACT_COMPARISONS_OK profiles=71799`.

The algebraic exact count and all-size characterization are established by the proof in `RESULT.md`. Finite tests cannot prove an infinite characterization or a distributional limit. The concentration follows from a uniform Stirling error, the explicitly differentiated exponent, and a strict maximizer. Scientific priority is subject to the literature limitations documented in `REVIEW.md` and `AUDIT.json`. No independent external audit has been performed.
