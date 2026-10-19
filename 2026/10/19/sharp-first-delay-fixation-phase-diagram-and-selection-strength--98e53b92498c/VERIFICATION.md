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
# Verification scope

The mathematical claim is proved by direct solution of four absorbing-chain equations and two integer-polynomial sign identities, not by finite sampling. To independently check the displayed identities and selected samples, execute `python3 verify.py` in the directory holding that file. The checker uses only standard-library `fractions.Fraction`, integer polynomial arithmetic, and a separately constructed absorbing Markov transition system.

The checker reports: five universal bivariate polynomial identities passed; two universal selection-strength polynomial identities passed; 144 exact-rational independent four-state Markov-chain comparisons passed; and exact positive/negative witness comparisons passed. The universal identities are exact integer coefficient equalities, while the 144 rational comparisons are finite supplemental checks. Assertions passing do not certify unpublished-priority status or an external audit. Source comparisons are limited to the specifically named literature and checked mathematical implications; the original model and fundamental-matrix method belong to prior research.

Boundary cases: all fitness ratios must be strictly positive; the explicit zero-strength case has equal fixation probabilities, and the critical threshold is inside the allowed interval. Claims about longer delays, larger populations, different initial histories, or different reproduction/replacement conventions are not made.
