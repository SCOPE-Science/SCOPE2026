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

# Verification record

The included `check.py` independently counts occurrences using a standard subsequence dynamic program, not the profile identity. Exact enumeration across all binary words of lengths through 15 was compared with the profile formula in 3,168 separate parameter/length/frequency cells, for \(1\le a,b\le4\), \(a+b\le n\le15\), \(1\le k\le18\). The \(0011\) frequency-five profile and its closed binomial formula were also checked through \(n=39\). The recorded output appears in `check_output.txt`; use `python3 check.py` to replay.

The infinite claims do not follow from finite verification. They are proved in `RESULT.md` via classification by the first one of a scattered occurrence, finite bounds on canonical zero-count profiles, and a unique \(a+b\)-free-gap factorization. The length generating function holds for all positive integers \(a,b,k\) and every nonnegative integer \(n\).

Scientific boundaries: only two-run binary patterns and positive occurrence frequencies; no complexity claim for the profile enumeration, no independent mathematical audit, and no claim of publication-priority certification.
