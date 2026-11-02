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

# Reproducible checks and limits

Run `python3 verify.py` using Python 3 and its standard library. The verifier constructs the exact recurrence and local prime parts without floating point, computes Möbius transforms directly, checks the proposed least repair multiplier against the least common multiple of all measured denominators, and checks the Legendre-symbol criterion. It also checks the claimed possible support of transforms and exhibits a negative transform at index \(2r\) when an odd prime divides a trace term.

Checked range: all positive parameters \(1\leq u\leq10\), every prime at most \(43\), and all positive indices at most \(120\). This comprises 140 parameter/prime pairs and 16,800 exact integer Möbius sums. These are finite falsification checks only. The all-parameter proof and prime-density claim rely on the mathematical argument in RESULT.md, including odd-prime lifting and quadratic-character equidistribution. No independent mathematical audit is claimed.
