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
The checker enumerates all
\[
(n,k)
\]
with
\[
4\le n\le14,
\qquad
2\le k\le n-2.
\]

For every \(k\)-subset \(I\), it constructs a \(k\)-subset \(J\) by replacing two entries of \(I\) with two entries of its complement and verifies
\[
|I\cap J|=k-2.
\]

It then explicitly enumerates the Plücker-coordinate basis of
\[
\bigwedge^{k-1}J\wedge\mathbb C^n
\]
and confirms that \(I\) is absent, so the coordinate hyperplane \(p_I=0\) contains the tangent space at \([e_J]\).

Separately, it checks that the weights
\[
\sum_{i\in I}2^i
\]
are pairwise distinct and that the total number of fixed dual coordinates is \(\binom nk\).

Finite checks are regression evidence only. The all-parameter theorem is the symbolic tangent-space and Euler-localization argument in `RESULT.md`.
