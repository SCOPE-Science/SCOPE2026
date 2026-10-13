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
The checker constructs
\[
w_{ij}=2^i+2^j,
\qquad
0\le i\le j<n,
\]
and verifies that these projective coordinate weights are pairwise distinct.

It counts
\[
n
\]
diagonal rank-one coordinate points and
\[
\binom n2
\]
off-diagonal rank-two coordinate points. Therefore the fixed-point counts are
\[
n
\]
for the rank-one locus and
\[
\binom{n+1}{2}
\]
for every cumulative rank bound at least two.

Subtracting consecutive cumulative values verifies
\[
\chi(S_{n,1}^{=1})=n,
\qquad
\chi(S_{n,2}^{=2})=\binom n2,
\qquad
\chi(S_{n,r}^{=r})=0
\]
for every tested \(r\ge3\).

The finite range is
\[
2\le n\le100.
\]
Finite checks are regression evidence only. The infinite proof uses binary uniqueness, rank preservation, Euler fixed-point localization, and constructible additivity.
