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
`artifacts/verify.py` is a standalone exact verifier using only the Python standard library.

It constructs \(\mathbb F_8=\mathbb F_2[u]/(u^3+u+1)\), evaluates the trace-norm defining function on all \(64\) pairs, and obtains the exact \(28\)-point defining set. From the evaluation formula it builds the \(7\)-coordinate message representation of every generator column and checks that the columns are distinct, nonzero, and reproduce the published weight enumerator by exhaustive enumeration of all \(128\) messages.

For each \(0\le t\le7\), every \(t\)-subspace of \(\mathbb F_2^7\) is generated exactly once from a reduced-row-echelon basis. The number of generated subspaces is checked against the binary Gaussian binomial coefficient. For every subspace the verifier counts its intersection with the \(28\) generator columns, reproduces the complete histograms stored in `artifacts/certificate.json`, and derives both the generalized Hamming weights and the number of subcodes attaining each minimum.

The computation is exhaustive and finite. It proves no statement about other \([28,7,12]\) equivalence classes, and it does not use finite sampling to infer an infinite claim. Successful replay prints `VERIFY_OK`.
