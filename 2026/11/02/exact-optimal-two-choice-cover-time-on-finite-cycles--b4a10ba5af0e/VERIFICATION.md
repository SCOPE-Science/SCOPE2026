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

# Reproducibility of the finite diagnostics

`checker.py` is self-contained and depends only on Python 3's `fractions` and `itertools`. Run `python3 checker.py`. The verified output is `PASS: 21,972 exact rational assertions; 104 interval lengths, exhaustive memoryless policy checks for k<=9, 102 full cycle sizes.`

The program checks the proposed finite-stage exit-value function for all intervals with \(1\le k\le104\), including Bellman equations at every state and the values under a concrete optimal deterministic policy. It also enumerates all \(2^k\) deterministic memoryless control policies for \(1\le k\le9\) and solves their absorbing tridiagonal systems exactly, checking that none beats the candidate from any starting position. It sums independently computed stage values for all cycles \(3\le n\le104\) and compares against the closed parity formulas. A policy need not be memoryless in the original theorem: the analytical Bellman principle covers arbitrary admissible history-dependent choices.

A finite check cannot prove an all-size formula. The separate analytical proof uses phase decomposition, a closed-form Bellman solution and a properness argument. The only assumptions are independent two-neighbor offers with replacement on simple cycles, without access to future randomness. A mathematically independent review has not been performed.
