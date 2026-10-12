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
`artifacts/verify.py` uses only the Python standard library.

It realizes
\[
I_2=\{0,a,b,c=a+b\}
\]
as pairs over \(\mathbb F_2\), with multiplication determined by
\[
a^2=c^2=b,\qquad b^2=ab=0.
\]

For every
\[
1\le n\le7,
\]
the verifier enumerates all \(4^n\) vectors. For each nonzero vector \(v\), it computes
\[
\langle v,v\rangle
\]
directly and checks that
\[
\{0,v\}
\]
is ACD exactly when the number of \(a\)- and \(c\)-coordinates is odd.

It groups the ACD vectors by the exact composition
\[
(n_0,n_a,n_b,n_c),
\]
which is the coordinate-permutation orbit invariant, and verifies the closed distance profile
\[
N_{2t}=t(t+1),
\qquad
N_{2t+1}=(t+1)(t+2).
\]

It also checks the total orbit formulas, the labeled count
\[
2^{2n-1},
\]
the maximum-distance class count, and the published length-one-through-five sequence
\[
2,\ 4,\ 10,\ 16,\ 28.
\]

Successful replay prints `VERIFY_OK`.
