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
\mathbb F_{25}=\mathbb F_5[\gamma]/(\gamma^2+\gamma+2)
\]
and verifies that \(\gamma\) has multiplicative order \(24\).

Using the source parameters
\[
(q,e_1,e_2)=(5,5,13),
\]
it reconstructs
\[
c(a,b)=\left(\operatorname{Tr}_{25/5}(a\gamma^{20i}+b\gamma^{13i})\right)_{i=0}^{23}
\]
and checks the published original weight enumerator.

It deletes coordinate zero to obtain the punctured code and independently takes the kernel of coordinate zero before deleting it to obtain the shortened code. Their ordinary weight enumerators are checked against Example 2(b).

The verifier then generates every subspace of \(\mathbb F_5^4\) and \(\mathbb F_5^3\) exactly once in reduced-row-echelon form. The checked subspace totals are
\[
156,\ 806,\ 156,\ 1
\]
and
\[
31,\ 31,\ 1.
\]
For each basis it computes the union of codeword supports and compares the complete histogram with `artifacts/certificate.json`.

Successful replay prints `VERIFY_OK`.
