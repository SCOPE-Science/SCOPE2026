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

# Verification details

The symbolic argument decomposes the square-zero partner into five blocks and verifies all five square-zero identities. It then checks directly that the image of the \(2\times2\) commutator with the nilpotent block equals that block's anticommutant (dimension two) in every characteristic. Two \(k[z]/(z^2)\)-module homomorphism spaces each have dimension \(s\), even when the remaining square-zero block contains nontrivial Jordan blocks. These are proof steps, not numerical inferences.

The included `verify.cpp` enumerates every matrix permitted by the linear anticommutator equation for a fixed rank-two square-zero \(X\), performs direct finite-field multiplication to test \(Y^2=0\), confirms \(XY+YX=0\), and computes \(\operatorname{rank}(XY)\) using Gaussian elimination. The field operations include the extension field \(\mathbb F_4\), represented by a root of \(u^2+u+1\).

Passing test totals (number of matrices \(Y\) with \(XY\ne0\)): \(n=4\): \(12,72,240,600\) for \(q=2,3,4,5\); \(n=5\): \(48,648\) for \(q=2,3\); \(n=6\): \(768\) for \(q=2\). The corresponding complete candidate spaces have \(256,6561,65536,390625,8192,1594323,1048576\) elements. Each case was exhausted independently of the closed formula.

These tests do not exhaust higher dimensions or all prime powers. Independent mathematical review remains unperformed.
