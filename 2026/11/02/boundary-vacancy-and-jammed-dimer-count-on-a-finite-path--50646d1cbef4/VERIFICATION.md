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

# Verification and reproducibility

Run `python3 verify.py` from the directory containing the seven provided files. No external Python dependencies are required. The program checks the exact rational moment recurrences against the closed coefficient formulas through length 150, exhaustively simulates every arrival order at lengths two through eight, checks the finite signs through length 150, and verifies the rational upper bound controlling all lengths at least ten. It reports **629 passing exact assertions**.

The infinite statement is established analytically in `RESULT.md`: the differential equations follow from an exact first-edge decomposition, and the tail estimate bounds the covariance uniformly above the finite cutoff. The finite tests test those derivations but cannot establish the infinite result on their own. The bound uses elementary exponential tails and the inequality \(e<3\). No independent human or external proof review has been completed.
