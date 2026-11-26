---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 verify.py` in the directory containing this file. For \(N=2,4,8,16,3,9,5,7\), the verifier computes exact cyclotomic polynomial remainders for every nonempty frequency subset. For every required-level profile it finds all actual minimum-size valid subsets, counts them, checks their tree branching and stabilizers, and counts the lexicographically canonical representatives modulo translation. Each successful modulus prints one `PASS` line. The finite computation is a diagnostic; the proof in `RESULT.md` gives the general result.
