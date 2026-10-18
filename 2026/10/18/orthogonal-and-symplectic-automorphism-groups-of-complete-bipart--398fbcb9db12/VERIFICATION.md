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

# Reproducible finite checks

Run `python verify.py` after installing NumPy as specified in `requirements.txt`. It independently evaluates all invertible \(2\times2\) and \(3\times3\) matrices in the listed small prime-field cases and checks all multiplication identities. It independently counts point-stabilizing orthogonal matrices over two small prime fields and \(\mathbb F_4\), and checks the nonmonomial example. Expected final stdout line: `ALL_TESTS_PASSED`. This covers finite test instances only; all-field quantifiers are established by the proof in `RESULT.md`.
