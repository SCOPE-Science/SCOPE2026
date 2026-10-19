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

Execute `python3 verify.py` in a standard Python 3 environment. No input data, network request, third-party Python package or external source file is needed. The verifier constructs four morphism blocks at scale \(2^{13}\), enumerates complete actual adjacent-pair coverage, and obtains every distinct nonzero palindrome for lengths \(1\) through \(8192\) with a literal-string palindromic tree. The \(0^n\) factor is accounted for separately for each length. It also checks the first \(8192\) sequence symbols against the defining zero-run rule and independently enumerates palindrome strings using center expansion through length \(128\).

Expected end of standard output:

```
VERIFIED_PAIR_SET=AB,BB,BC,BD,CB,DB,DC,DD
VERIFIED_LENGTHS=1..8192
EXCEPTIONAL_LENGTHS_45..8192=66
ZERO_ONLY_LENGTHS_45..8192=8082
PROFILE_SHA256=c94eac15fdef31d2b90ccd14121e0782788a316c05a5c80f9d7bde100ff05e55
VERIFY_OK
```

The code compares all \(8192\) values, not just sample lengths. Its mathematical completeness rests on the proved covering lemma for four-letter adjacent substitution pairs. The extra center-expansion check is fully independent as an enumerator but limited to the first \(128\) lengths. The result does not cover any length exceeding \(8192\). Independent audit: not performed.
