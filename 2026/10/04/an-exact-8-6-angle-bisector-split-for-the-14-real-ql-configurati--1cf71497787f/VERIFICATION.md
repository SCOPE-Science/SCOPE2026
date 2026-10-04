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

The exact verifier reconstructs the two limiting line equations and uses
\[
N_1=3563201,\qquad N_2=6112121
\]
for their squared normal lengths.

For each sign \(\sigma\in\{+1,-1\}\), it solves
\[
\ell_1(X,Y)=q\sqrt{N_1},
\qquad
\ell_2(X,Y)=\sigma q\sqrt{N_2}
\]
exactly, builds the circle centered at \((X,Y)\) with squared radius \(q^2\), and forms the determinant pencil with
\[
Q_1:20x^2-5y^2+1=0.
\]

It then computes the cubic discriminant in the pencil parameter. Each resulting polynomial in \(q\) is checked to be squarefree of degree \(8\), and \(q=0\) is checked not to occur.

Exact real-root counting over
\[
\mathbf Q\!\left(\sqrt{3563201}+\sqrt{6112121}\right)
\]
returns
\[
8
\]
for the plus branch and
\[
6
\]
for the minus branch.

The source's certified total of \(14\) real \(QL^2\) circles is used only to turn these necessary tangency-root upper bounds into exact branch counts. The replay output ends in `VERIFY_OK`.
