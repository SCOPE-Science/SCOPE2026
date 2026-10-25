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

# Reproduction and limits

Run `python3 check.py` from the directory containing this file. The checker uses only the Python standard library. It constructs distinct scattered subsequences, then identifies all minimal absent strings from the one-symbol extensions of present subsequences, testing every one-position deletion. It tests all 32767 binary words with lengths 0 through 14 and the sharp witness \((010)^k\) for \(0\le k\le7\); the terminal output is `VERIFY_OK 32767`. The check is finite, whereas the result for all \(k\) follows from the induction and the published recurrence cited in RESULT.md. No third-party full texts are embedded.
