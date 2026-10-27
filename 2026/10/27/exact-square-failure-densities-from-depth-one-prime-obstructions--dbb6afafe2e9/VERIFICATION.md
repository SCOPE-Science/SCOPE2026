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
# Reproducibility and boundaries
Run `python3 verify.py` using Python 3.10 or later and only its standard library. It exhaustively examines every initial finite-field point for each prime \(p\le500\) in the eligible congruence classes, confirming that any zero is first reached at iteration one. It independently enumerates all starting-value classes for \(h=1,3,13,17,26,39,169,221\), evaluates the initial obstruction and checks the first seven homogeneous iterates modulo \(h\). The exact counts include \(47929\) zero-failure and \(912\) one-failure classes modulo \(48841\) for \(h=221\), and \(501\) versus \(175\) classes modulo \(676\) for \(h=26\).

The full statement is proved by the elementary projective preimage and CRT argument in RESULT.md, not by finite enumeration. The imported square criterion is explicitly attributed to Proposition 4.1 of arXiv:2610.00765v1. The verification does not examine primes greater than \(500\), nor does it independently reprove the imported criterion; these are proved and sourced separately as described. All computations are exact integers, without sampling or timeouts.
