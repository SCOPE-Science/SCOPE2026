---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Write X=A+epsilon B, so A^2=0 and AB+BA=0 in any characteristic. Rank-r A has r length-two Jordan blocks and s=n-2r zero blocks. Diagonal P reversing the image block sign satisfies PA=-AP, including char 2, so anti-commutator fibers biject with the commutant of A, dimension (n-r)^2+r^2. The reductions are counted by choosing image U subset kernel K and an isomorphism F_q^n/K to U: [n choose r]_q[n-r choose r]_q |GL_r|=q^(2r(n-r)) Phi_n/(Phi_r Phi_(n-2r)). Multiplication cancels exponent to n^2. Uniform exponential estimates Phi_m-Phi_infty=O_q(q^-m) imply rank weights differ from 1/Phi_infty by a summable boundary term, yielding total O_q(1) remainder and O_q(1/n) empirical CDF error. Endpoints r=0 and n=1 valid. Fresh exhaustive anticommutator kernel ranks checked F2 n<=3 and F3 n<=2.

## originality

PASS

Length-two local-ring similarity classifications and square-free matrix-polynomial formulas do not assert the unrestricted labelled square-zero rank census; first jet of square-zero scheme is a possible equivalent reformulation, so stronger literature could implicitly cover it.

## value

PASS

The all-dimensional arithmetic rank census and macroscopic uniform rank law for first-order thickening are natural deformation-theoretic phenomena, sharply contrasting with the field-only square-zero rank distribution. A future researcher can use both the exact fibers and limiting law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
