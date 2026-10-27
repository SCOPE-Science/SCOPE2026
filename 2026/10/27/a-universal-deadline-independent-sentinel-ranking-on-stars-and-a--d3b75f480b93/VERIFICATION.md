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

The analytical proof in `RESULT.md` applies to all integers \(n\ge3\), \(2\le k\le n-1\), all \(0<p<1\), and every integer deadline \(t\ge0\). Independent finite checks confirm the closed distributions, do not substitute for their proof, and do not establish publication priority.

The included standalone `check_star_sentinels.py` requires only the Python standard library. Running `python check_star_sentinels.py` from the extracted package returned `PASS: 5797 exact checks; all monitored-subset symmetry classes verified.` It enumerates exact rational state transitions on stars with \(4\le n\le7\), all sensor sets with \(2\le k\le n-1\), three rational probabilities, and deadlines through step six. It separately checks the two rational five-vertex witnesses and checks convergence of finite sums to the exact expected-delay difference. No independent external scientific audit has occurred.
