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
# Verification of the exact wheel census

Execute `python3 verify.py` in the directory containing the packaged files. The program imports only Python's standard library.

The direct test enumerates all spin words (hub and rim) for \(5\le n\le12\), computes the original Ising energy, and tests every subset flip of cardinality one, two or three. It then independently compares the three stability flags with the forbidden-pattern criterion, and compares the energy-graded direct count with both closed binomial sums. Finally, it expands the two proposed rational generating series through rim length \(150\) and verifies each coefficient against its closed form, and numerically verifies both algebraic roots. The observed output reports 49,252 finite-state assertions with no failures, plus the displayed exact enumerations. No random sampling or inferred infinite extrapolation is used.

**Limits:** This software does not formally certify the all-size proof or literature novelty. The all-size proof requires the local flip-cost classification, cyclic independent-set counting, and aperiodic rational-coefficient asymptotics supplied in `RESULT.md`. No independent audit has occurred.
