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
The universal theorem is proved from the exact generation criterion
\[
\langle S\rangle=G
\iff
B\ne\varnothing
\text{ and }
\operatorname{span}_{\mathbf F_p}
\bigl(A\cup\{b-b_0:b\in B\}\bigr)=V,
\]
where \(A\) is the set of translation parameters and \(B\) the set of reflection parameters.

This criterion gives \(d(G)=t+1\) and controls every pair extension without an exhaustive infinite argument.

The packaged checker `artifacts/verify.py` reconstructs the group multiplication and subgroup closure. It exhaustively enumerates every minimum generating triple for the groups with
\[
(p,t)=(3,2)
\quad\text{and}\quad
(p,t)=(5,2),
\]
and compares every graph edge with the theoretical criterion. It also checks direct generating witnesses for every predicted edge when
\[
(p,t)=(3,3).
\]

The replay returns `VERIFY_OK`.

The finite computations are checks of the formulas, not a proof of the theorem for arbitrary \(p\) and \(t\).
