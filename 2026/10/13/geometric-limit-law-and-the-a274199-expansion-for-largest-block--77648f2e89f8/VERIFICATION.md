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

The verifier first enumerates all binary and ternary words at small lengths to independently check the unbordered-word recurrence. It then checks the exact shortest-border identity
\[
q^m-u_m(q)
=
\sum_{1\le j\le m/2}u_j(q)q^{m-2j}
\]
for several alphabet sizes and all tested lengths through \(40\).

For binary and ternary words through length \(8\), it exhaustively computes the greedy largest block-palindrome factorization and verifies the exact finite formula for every tested tail event \(\Pr(M_n\ge r)\).

The verifier separately computes the defining A274190 array and exhaustively enumerates constrained compositions through index \(16\), confirming stabilization to
\[
1,1,2,3,5,8,12,19,29,44,67,101,152,228,342,511,763.
\]
It also constructs the formal power series from the triangular shortest-border recursion and confirms the same coefficients independently.

Finally, it evaluates the exact rational truncations of \(s_q\) and reproduces the published expected-width values for every \(q\) from \(2\) through \(10\).

Finite computations are checks on the proof and implementation. The theorem for all alphabet sizes, all limiting widths, and all coefficients follows from the symbolic renewal and composition arguments in `RESULT.md`, not from finite extrapolation.
