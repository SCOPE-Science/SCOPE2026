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

# Verification record
The finite-sample variance lower bound follows from a conditional-variance proof using an independent fair refresh bit, forced refresh at the observed vertex and its neighbors in the next round, and equal forced lag-endpoint bits. The proof remains valid on infinite graphs of locally finite degree, because possible descendants of the selected bit are cut off after one round. Selected observation times are spaced by twice the lag plus two, preventing overlap of selected refresh-bit constraints. The bound is not a claim of sharpness.

The standalone `verify.py` uses exact rational finite-state Markov dynamic programming, not Monte Carlo. Invoking `python verify.py` passed 150 exact checks on the two-vertex edge, three-vertex path (middle observed), and triangle, with two refresh probabilities, lags one through three, and various observation lengths. A passing finite test suite does not certify the infinite claim; the written proof does that work.

The normal limit and existence of the limiting variance are implications of independently published Lemma 2.3 and Theorem 2.7 in arXiv:2207.01224, as applied to the new strictly positive lower bound. These external theorems are relied upon, not reproved here. No independent audit was performed.
