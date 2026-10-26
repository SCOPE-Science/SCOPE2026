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

The standard-library program `verify.py` is executable with `python verify.py`. It exhaustively generates every labeled tree on two through eight vertices through Prüfer sequences, removes isomorphic duplicates through center-rooted canonical encodings, checks class counts \(1,1,2,3,6,11,23\), and solves the weak-selection meeting-time systems over exact rational numbers. All scores and inequality checks use exact fractions. The nine-vertex witness is separately checked with rational substitution and strict comparisons.

The analytical bridge from the positional-voter Markov chain to the coalescence system is shown in `RESULT.md`. A separate numerical full-chain cross-check at small positive advantage was also performed for the nine-vertex witness but is not a component of the exact proof. The test does not certify the nine-vertex enumeration of all isomorphism classes, behavior under arbitrary finite advantage, or independent publication priority.
