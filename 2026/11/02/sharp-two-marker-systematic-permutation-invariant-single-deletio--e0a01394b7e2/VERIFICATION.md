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

# Verification procedure

In a directory containing `verify.py` and `codebooks.json`, run:

```sh
python3 verify.py
```

The checker uses only the Python standard library. It independently standardizes each deletion by sorting and by pairwise comparisons, checks every encoded message is present exactly once, confirms all codeword symbols are distinct and correct, and compares all deletion outputs between distinct codewords. It additionally tests the adjacent-deletion characterization for all permutations of lengths three through seven. The preceding infinite lemma is proved on paper, not inferred from this finite enumeration.

Observed results: length-three code with two information symbols has two codewords and two distinct outputs; length-five code with three information symbols has six codewords and eighteen distinct outputs; length-six code with four information symbols has twenty-four codewords and ninety distinct outputs. No cross-codeword PID collision occurred. `verification_output.txt` includes the complete checker output and ends with `VERIFY_OK`.

Limitations: computational verification of codebooks is exhaustive for those explicit finite sets, not exhaustive over all possible encoders. The mathematical lower bound independently rules out zero markers at every information length at least two and one marker at every information length at least three. No independent audit is represented by this verification.
