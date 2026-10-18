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

# Finite verification and limits

Compile `verify.c` with `cc -O3 -std=c11 verify.c -o verify` and run `./verify`. The program independently checks both subsequence predicates; minimality by deletion at every position; exact family membership; and each length count for all binary words of lengths \(2m\) through \(4m\), where \(1\le m\le5\). It reports `VERIFY_OK objects=2235596 minimum_supersequences=13890 n<=5`. This is an exhaustive finite check only; the proof in `RESULT.md` supplies all infinite cases. No external independent scientific audit is claimed.
