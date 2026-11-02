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
# Reproducibility checks

Run the self-contained included program using `python verify_pal_inverse.py`. It enumerates all received words in explicitly bounded binary/ternary cases, directly reconstructs the source words at each palindromic window, checks the sharp maximum and local collision condition, and tests the periodic construction at many greater block lengths. A successful actual execution prints:

```text
VERIFY_OK exhaustive_cases=73 exhaustive_received_words=832346 sampled_or_witness_cases=11200 k_witness_range=1..700 max_alphabet_tested=5
```

**Proof versus computation:** the finite checks do not establish the all-length theorem. The proof is in RESULT.md and rests on the exact two-parent collision equality, the product of palindrome reflections, a spacing upper bound, and a residue-periodic attaining construction. The checker uses only the Python standard library and accepts no external data. No independently audited scientific evidence is asserted.
