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
# Verification of the fair-rally first-serve law

Run `python3 verify.py` from the directory containing this file. The implementation uses only the Python standard library and computes exact rational probabilities. It checks 12 equations for the score-difference continuation after deuce; six symbolic polynomial identities for the four-state Green-row reduction and the two weights; 30 all-state dynamic-programming comparisons at integer targets \(2\le n\le31\); and the ordinary Legendre recurrence through degree \(31\).

The target checks reproduce the tiny negative advantage at \(n=11\) and positive advantage at \(n=15\). They are finite regression evidence, not an exhaustive proof. The analytic infinite-target identity follows instead from a formal generating function, a constant-term diagonal identity, and the deuce continuation algebra. Infinitely many sign changes and the exact envelope follow from the fixed-angle Legendre asymptotic and irrational rotation. The asymptotic theorem is not certified by finite tests.

The verification does not address non-fair serving, player-specific probabilities, capped deuce, other scoring rules, novelty priority, or independent audit.
