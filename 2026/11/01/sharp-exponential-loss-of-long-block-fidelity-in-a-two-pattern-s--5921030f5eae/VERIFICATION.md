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

The proof's finite-critical identities were checked symbolically by direct derivation: exact adjacent-pair masses \(1-2\alpha,\alpha,\alpha,0\); stationary transition matrix; floor-sum decrease count; integer transition counts; uniform bounded correction to log Markov word mass; exact cross-entropy identity. The independent mathematical dependence is the classical Morse–Hedlund criterion for non-eventually-periodic binary sequences, which yields \(n+1\) distinct factors once aperiodicity is established by irrational decrease frequency.

Execute `python3 CHECK.py` from the same directory as these files. The standard-library program tests the formulas using three explicit irrational rates, enumerating their exact circle partition intervals in double precision for selected lengths through \(n=60\). A successful run prints `VERIFICATION_OK`. Results are only numerical corroboration. Double precision does not certify arbitrary irrationality, all orders, or extreme parameter limits.

Known source-access limitation: the complete text of the 2019 ordinal-network Markov-modeling article was not available for detailed priority comparison. This is not evidence of novelty; the available abstract and later full-text descriptions were compared, and the remaining uncertainty is recorded.
