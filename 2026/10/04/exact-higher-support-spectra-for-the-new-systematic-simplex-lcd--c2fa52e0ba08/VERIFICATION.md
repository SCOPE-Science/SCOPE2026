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

For each of
\[
(q,m)=(2,3),(2,4),(3,2),(3,3),
\]
the verifier constructs
\[
G_q(m)=[I_m\mid S_q(m)],
\]
where \(S_q(m)\) contains all nonzero vectors of \(\mathbb F_q^m\) as columns.

It enumerates every message subspace in reduced row-echelon form. For each \(r\)-subspace it computes the support of the corresponding subcode directly from the generator matrix. The resulting support histograms are compared with
\[
\binom{m}{s}
\sum_{j=0}^{s}
(-1)^j
\binom{s}{j}
G_q(s-j,r)
\]
at support size
\[
q^m-q^{m-r}+s.
\]

The verifier also checks that each histogram sums to the Gaussian binomial \(G_q(m,r)\) and that its minimum is
\[
q^m-q^{m-r}+r.
\]
Successful replay prints `VERIFY_OK`.
