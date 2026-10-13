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
The checker verifies the finite combinatorial parts of the proof.

For every
\[
4\le n\le18,
\]
it constructs the diagonal cocharacter exponents
\[
a_i=2^{i-1}
\]
and verifies that all
\[
2^n
\]
signed tensor weights are distinct.

For every
\[
4\le n\le9
\]
and every pair of subsets
\[
I,J\subseteq[n],
\]
it checks that the diagonal degeneration exponent
\[
e_I(J)=n-|J|+2|J\setminus I|
\]
satisfies
\[
e_I(J)-e_I(I)=|I\setminus J|+|J\setminus I|.
\]
Hence the exponent has a unique minimum at
\[
J=I.
\]

These finite checks do not prove the all-parameter theorem. The proof for arbitrary
\[
n\ge4
\]
is the symbolic fixed-point and localization argument in `RESULT.md`.
