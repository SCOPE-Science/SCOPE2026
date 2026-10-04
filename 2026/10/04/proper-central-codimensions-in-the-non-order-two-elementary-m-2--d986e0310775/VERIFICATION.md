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

The proof is symbolic and exact. It depends on the linearly independent normal forms and complete central-polynomial classification proved in arXiv:2609.20488v1. The finite checker is not used to infer the theorem.

`artifacts/verify.py` checks, for every integer \(1\le n\le40\), that the direct multinomial count of the proper central classes equals
\[
\binom{2n}{n}-2^{n-1},
\]
that the direct normal-form count of all multilinear classes equals
\[
\binom{2n+2}{n+1}-2^n,
\]
and that the exact shift relation
\[
c_n^{(G,*),\delta}=c_{n-1}^{(G,*)}
\]
holds, using \(c_0^{(G,*)}=1\).

The check also records the first values of both sequences. Its output is stored in `artifacts/verification.txt` and ends with `CHECK_OK`.

Limits: a forty-degree arithmetic replay is only a consistency check. The infinite statement is justified by the coefficient-extraction proof in `RESULT.md`, not by extrapolation from these values.
