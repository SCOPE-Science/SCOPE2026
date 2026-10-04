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
Run `python3 verify.py`.

The checker tests the critical local descent for every even
\[
2\le k\le400
\]
and every tested prime through \(5000\) above the theorem's threshold. It verifies that the first composite in the prime progression occurs by the allowed least-missing-prime index, that the composite is odd, that its largest prime divisor is at most one third of it, and that the next prime state is smaller.

It separately follows trajectories from all starts through \(1000\) for every even \(k\le100\) and confirms that every observed cycle meets the predicted prime range.

These finite tests are regressions, not an exhaustive proof. The all-parameter theorem is proved symbolically by the progression lemma and strict prime-state descent.

A successful replay prints `VERIFY_OK`.
