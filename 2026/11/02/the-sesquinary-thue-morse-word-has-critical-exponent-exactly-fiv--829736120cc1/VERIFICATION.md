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

Run `python3 VERIFY.py` in a standard Python 3 environment. Expected final line:

`VERIFY_OK recurrence_terms=65536 periods=128 witness_index=18 parity_algorithms=2`

The script computes 65,536 parity values in two distinct ways: from the length-decreasing three-way recursion and by successive rational-base least-significant digits. It checks both macroblock identities and the absence of length-\(5p+1\) factors of period \(p\) in a finite prefix for all \(1\le p\le128\). It confirms the \((101)^5\) witness beginning at index 18.

The program is a finite sanity check, not a certificate of the infinite theorem. The proof in `RESULT.md` uses exact block identities, exhaustive residue arguments, and a length-recursion induction for all periods. No independent scientific audit was conducted.
