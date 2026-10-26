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

# Verification of the two-trace complement-doubling law

The accompanying `verify.py` script uses only Python's standard library and can be run with `python verify.py`. It checks all \(126\) nonempty binary seed words with lengths \(1\) through \(6\), including both monochromatic and mixed seeds. For several doubling rounds it compares the two-trace recurrence with direct matrix multiplication and with a separate last-occurrence recurrence for distinct subsequences. Whenever the host length is at most \(16\), it also computes the actual set of distinct subsequence strings.

The script separately checks the first \(13\) Thue–Morse blocks, including one of length \(4096\), and a nontrivial seeded block family. The first seven enumerated counts are checked against \(1,3,10,72,2664,3647088,6476006417760\). Successful execution prints `VERIFY_OK exhaustive_seeds=126 Thue_Morse_prefix_length=4096`.

This is finite reproducibility evidence, not an exhaustive check of all words or an infinite proof. The arbitrary-seed recurrence and convergence argument are proved algebraically in `RESULT.md`; the effective error bound uses \(t_{m+1}\geq2t_m\) and the geometric series with ratio \(1/8\). Independent audit has not been performed.
