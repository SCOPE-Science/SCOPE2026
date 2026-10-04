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

The claim is reduced to the split commutator matrix obtained by subtracting the two input orders in equation (23) of Nagy–Zhou, arXiv:2609.32651v1. The scalar factor \(1-w\) is nonzero and therefore does not affect rank.

`verify_commutator.py` constructs the normalized matrix over \(\mathbb Z[X_0,\ldots,X_4]\) and checks exactly that its determinant is zero and that every deleted-row/deleted-column determinant equals
\[
(-1)^{r+c}X_rX_c(X_0+X_1+X_2+X_3+X_4)^2.
\]
The actual run captured in `verification_output.txt` reports `VERIFY_OK`.

For field elements, the conjugate-coordinate map is invertible and the coordinate sum is \(\operatorname{Tr}_{F/K}(x)\). Thus the symbolic identities prove rank \(4\) when the trace is nonzero. On the nonzero trace-zero stratum all \(4\times4\) minors vanish; alternating rank parity and the nonzero entry \(X_1\) force rank \(2\). No finite enumeration is used to infer an infinite statement.

Limits: extension degrees other than \(5\) are not checked or claimed, and no isotopy-invariance statement is made.
