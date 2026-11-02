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

The result is supported by a self-contained proof and the reproducible standard-library program `verify.py`. Run `python verify.py` to construct literal distinct-subsequence sets for binary words of lengths zero to twelve; cross-check the coprime recurrence and exact modulo-\(m\) fibers for \(2\le m\le24\); compare rational-probability direct enumeration and finite-state dynamic programming in 45 cases; and check nine instances of the nonstationary finite-state convergence numerically.

The program is a finite test, not a proof of statements for unbounded word length or all moduli. Those claims are established by the Chinese remainder argument for primitive lifts, subtractive Euclidean reachability, padding at a self-loop, and Doeblin contraction. The bound is intentionally not optimized. Source independence and a fixed positive probability lower bound must be retained.

Only the listed checks have been performed. Independent audit has not been performed.
