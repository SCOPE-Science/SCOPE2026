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
The packaged checker `artifacts/verify.py` uses the normalized functional
\[
\varphi(x_1,\ldots,x_n)=x_1
\]
and product
\[
x\cdot y=\varphi(x)y.
\]

For
\[
(n,q)=(1,2),(2,2),(2,3),(3,2),(3,3),
\]
it exhaustively enumerates every \(n\times n\) matrix.

For each matrix it directly checks the Nijenhuis identity on all ordered basis pairs. Every matrix passes.

It then groups matrices by
\[
\varphi\circ N
\]
and verifies that all \(q^n\) target functionals occur, each exactly
\[
q^{n(n-1)}
\]
times.

The exact rank distribution is compared with
\[
\frac{\prod_{i=0}^{r-1}(q^n-q^i)^2}
{\prod_{i=0}^{r-1}(q^r-q^i)}
\]
for every rank.

Finally it directly checks the weight-zero Rota–Baxter identity, confirms equivalence with
\[
R^2=0,
\]
and verifies every square-zero rank stratum against
\[
\binom{n}{r}_q
\binom{n-r}{r}_q
|\operatorname{GL}_r(\mathbf F_q)|.
\]

It returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field result follows from the cancellation proof in `RESULT.md`.
