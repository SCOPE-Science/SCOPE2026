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
The packaged checker `artifacts/verify.py` uses the basis
\[
(t,v_1,v_2)
\]
with
\[
[t,v_i]=v_i,\qquad [v_1,v_2]=0.
\]

It starts from a completely general \(3\times3\) matrix and reconstructs every ordered basis-pair Rota–Baxter defect.

Symbolically, the nonzero equations are checked to be exactly the entries of
\[
fA+af=0
\]
and
\[
A^2+u\otimes f=0.
\]

It then exhaustively tests every linear map over \(\mathbf F_2\) and \(\mathbf F_3\) directly against the defining Rota–Baxter identity.

The exact rank distributions are
\[
(1,25,18,0)
\]
over \(\mathbf F_2\) and
\[
(1,122,192,0)
\]
over \(\mathbf F_3\), giving totals
\[
44
\]
and
\[
315.
\]

The checker also verifies for several values of \(q\) that
\[
1+\left(q^4+2q^3-q^2-q-1\right)+q(q^2-1)^2
=
q^5+q^4-q^2.
\]

It returns `VERIFY_OK`.

The arbitrary-prime-power theorem rests on the symbolic proof and exact counting argument in `RESULT.md`; finite enumeration is a replay check.
