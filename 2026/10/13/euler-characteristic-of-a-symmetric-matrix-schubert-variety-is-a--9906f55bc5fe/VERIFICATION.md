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
The checker enumerates every permutation for
\[
1\le n\le7.
\]

For each permutation it constructs the complete north-east rank matrix
\[
R_w(i,j)
=
\#\{k\le i:w(k)\le n+1-j\}.
\]

For every symmetric coordinate point \(S_{ab}\), it independently tests every north-east submatrix rank condition. It then compares that direct result with both
\[
R_w(a,b)\ge1,\quad R_w(b,a)\ge2
\]
for \(a<b\), and the equivalent prefix minimum/second-minimum criterion.

It separately verifies that every diagonal point survives, that the unique minimum is \(n\) at the long permutation, and that the ambient maximum \(n(n+1)/2\) occurs exactly when \(w(1)=1\).

Finite checks are regression evidence only. The infinite theorem is the symbolic torus-localization proof in `RESULT.md`.
