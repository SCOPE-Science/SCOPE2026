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

Run `python3 verify.py` beside `certificate.json`.

The checker implements three independent finite views of the new binary count. First, it evaluates the two-coordinate recurrence for alternating arches and compares it with Fibonacci values through \(k=15\); for \(k\le10\), it also constructs the complete SAS set by direct subsequence testing.

Second, it exhausts every one of the \(2^k\) orientations of \(k\) minimum binary arches through \(k=12\). The largest count is \(F_{k+3}\), attained by exactly the two alternating orientations.

Third, it enumerates every binary word of length at most \(12\). Its universality index is computed by independent arch scanning and every candidate SAS is tested directly as a subsequence. The Fibonacci upper bound holds throughout, and every minimum-length equality case is one of the two alternating words.

These computations are stress tests rather than the infinite proof. The general upper bound uses the inspected published extremal theorem for \(A_k\), and the exact Fibonacci count plus the minimum-length equality characterization are proved by the explicit recurrence and induction recorded in `RESULT.md`.

Independent audit has not been performed.
