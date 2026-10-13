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

It exhaustively generates small systematic codes over \(\mathbb F_2\) and \(\mathbb F_3\). For each source generator it computes the Euclidean hull in message coordinates, changes to a basis whose first rows generate the hull, and constructs the source normal-form shortest LCD embedding by adding an identity block on the hull rows.

For each example the verifier checks the hull dimension, nonsingularity of the embedded Gram matrix, rank \(\ell\) of the added-coordinate projection, and dimension \(k-\ell\) of the kernel subcode.

Every relevant message subspace is enumerated exactly once in reduced-row-echelon form. Thus the generalized Hamming-weight hierarchies of \(C\), \(K\), and \(\widetilde C\) are computed exhaustively.

For every \(r\), the script checks the kernel-sensitive lower bound, the universal two-sided bound, the terminal identity
\[
d_k(\widetilde C)=d_k(C)+\ell,
\]
and the self-orthogonal specialization whenever applicable.

The computation is a finite stress test. The arbitrary-length theorem is proved symbolically in `RESULT.md`.

Successful replay prints `VERIFY_OK`.
