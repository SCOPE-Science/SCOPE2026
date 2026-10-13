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
The checker independently builds Stirling numbers of the second kind from
\[
{n\brace b}=b{n-1\brace b}+{n-1\brace b-1}
\]
and verifies the closed-level and exact-layer formulas through
\[
n=30.
\]

It verifies directly that the cocharacter weights
\[
1,2,4,\ldots,2^{n-1}
\]
have pairwise distinct ordered nonzero differences through \(n=30\), reproducing the fixed-locus classification used in the proof.

For small prime fields, the checker enumerates projective diagonal tuples and groups them by their exact number of coordinate values. These counts agree with the set-partition formula using the finite-field configuration quotient. Evaluation of the resulting arrangement-count polynomial at \(1\) gives the complex compactly supported Euler contribution
\[
q_1=1,
\qquad
q_b=(-1)^{b-2}(b-2)!
\quad(b\ge2).
\]

Finite calculations are regression evidence only. The proof for arbitrary \(n\) and \(r\) is the symbolic fixed-point, configuration-space, and Euler-localization argument in `RESULT.md`.
