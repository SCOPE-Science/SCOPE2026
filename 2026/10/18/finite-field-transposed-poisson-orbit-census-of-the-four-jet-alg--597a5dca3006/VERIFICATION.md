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

# Reproduction and checks

Execute `python3 verify.py` with Python 3.8 or newer. The code implements truncated polynomial arithmetic, compositional inversion, derivations and Lie brackets directly, and does not use the closed orbit formulas to compute the group action. Its independent direct conjugation is compared with the candidate coefficient formula for every derivation and automorphism at prime-field orders \(3,5,7\). It then independently constructs the full conjugacy orbit of each normal-form stratum and verifies all claimed sizes.

Observed output: \(q=3\) gives \(27\) brackets, \(18\) automorphisms and \(8\) classes; \(q=5\) gives \(125\), \(100\) and \(12\); \(q=7\) gives \(343\), \(294\) and \(16\). The class-size multisets are respectively: zero size one; linear size \(q^2\) repeated \(q-1\) times; quadratic size \(q-1\) repeated \(q\) times; cubic size \((q-1)/2\) repeated twice. The program verifies Jacobi and the transposed Leibniz identity on the basis for all \(q=3,5\) parameter choices and sample \(q=7\) parameters. Final marker: `ALL_TRANSPOSED_POISSON_JET_CHECKS_PASSED`.

The check does not enumerate nonprime fields or all odd prime powers, and does not claim to: its purpose is to stress-test the stated general algebraic proof. Isomorphism completeness rests on the exhaustive symbolic action calculation. Independent scientific audit has not been performed.
