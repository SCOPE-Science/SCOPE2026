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

`verify.py` reconstructs the claimed finite quotient directly from the two published quadratic identities.

It generates the \(120\) multilinear arity-\(4\) monomials of the free operad on one nonsymmetric binary generator. It then forms every arity-\(4\) consequence of each quadratic relation by the three insertions \(R\circ_i *\), the two insertions \(*\circ_j R\), and all leaf relabelings. Exact rational row reduction of the resulting \(240\times120\) matrix gives rank \(106\), hence quotient dimension \(14\).

Using the free columns of the exact row-reduced matrix as a quotient basis, the script reduces the relabeling action of representatives of all five conjugacy classes of \(S_4\). The resulting character is
\[
(14,-6,2,2,0).
\]
Exact inner products with the irreducible \(S_4\) character table yield
\[
S^{(2,2)}\oplus3S^{(2,1,1)}\oplus3S^{(1,1,1,1)}.
\]

The saved output ends with `CHECK_OK`. The calculation is exhaustive only for arity \(4\); no higher-arity claim is inferred from it. The identification of this quotient with the kernel also uses the published theorem that \(D\mathrm{Acaa}(4)=0\).

Independent audit has not been performed.
