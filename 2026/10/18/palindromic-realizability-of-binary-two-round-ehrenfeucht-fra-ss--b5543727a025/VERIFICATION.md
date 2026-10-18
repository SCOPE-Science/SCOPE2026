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

Execute `python3 verify.py` under Python 3. The script terminates with `VERIFY_OK` after checking the complete 97-state transition closure, isolating 90 two-colour types and 20 reversal-invariant ones, and finding palindrome representatives of each invariant type of length at most nine. It independently checks that the unrestricted shortest representatives and constructed palindromes are equivalent under the literal two-round Ehrenfeucht–Fraïssé game; it also directly computes pointed character signatures rather than trusting transition indices.

Minimum palindromic representative lengths among the 20 classes: lengths three, four, five, six, seven, eight, nine have class counts 2, 2, 6, 2, 6, 0, 2. The two classes attaining length nine contain `001010100` and `110010011`; their unrestricted minimum length is eight. The source code and proof in `RESULT.md` supply the finite-state completeness argument: closure under both append transitions extends the finite enumeration to every finite binary word.

This is a self-review with directly replayable finite computations, **not independent validation**. Priority cannot be certified by a finite literature search; the specific sources and remaining risks are described in `REVIEW.md` and `AUDIT.json`.
