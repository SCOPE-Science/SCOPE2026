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

The bundled `artifacts/verify.py` is self-contained and uses only exact integer and binary arithmetic.

It reconstructs each printed hexadecimal generator matrix, checks that source padding beyond the true length is zero, verifies binary rank eight, verifies \(GG^T=0\), and reproduces the source minimum distance. It then enumerates each subspace of \(\mathbb F_2^8\) exactly once by reduced-row-echelon form. The per-dimension enumeration counts are checked against

\[
(1,255,10795,97155,200787,97155,10795,255,1).
\]

For every subspace the script performs two checks. The direct route encodes an RREF basis and takes the union of its coordinate supports. The section route sums multiplicities of generator columns inside the relevant message subspace and applies orthogonal complementation. Both routes must reproduce the hard-coded hierarchy and minimizer vectors for all four codes. A successful replay terminates with `VERIFY_OK`.

The verification is exhaustive for the four displayed representatives. It is not an equivalence-class census of all self-orthogonal codes with the same ordinary parameters, and it does not certify any global optimum for higher generalized Hamming weights.
