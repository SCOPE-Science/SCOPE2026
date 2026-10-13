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

# Reproducibility
Run `python3 artifacts/verify.py` from the extracted folder. The script uses only the Python standard library and ends in `VERIFY_OK`. It enumerates all 256 sets of possible three-bit prefixes and for each computes the maximum compatible three-bit suffix set directly, independent of the proof's four-case inequality. It checks the maximum product is ten and the explicit optimum is achieved. It separately tests the induced-arc inequalities on all 15 nonempty sets of two-bit states and checks every forbidden overlap for the constructed codes at lengths six, seven and eight. These finite tests corroborate the exact six-bit base and contain no claim about an exhaustive infinite test. The mathematical argument for all \(n\ge6\) is in `RESULT.md`.

# Limits
The checker does not establish publication originality, code equivalence classification, or optimality for other alphabets or overlap intervals. The review is same-model only; independent audit has not occurred.
