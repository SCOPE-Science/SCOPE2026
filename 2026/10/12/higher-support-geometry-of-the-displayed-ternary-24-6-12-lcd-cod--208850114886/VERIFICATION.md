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
`artifacts/verify.py` reconstructs the exact published \(6\times24\) matrix over \(\mathbb F_3\). It verifies rank \(6\), computes \(GG^T\) and checks determinant \(1\), and enumerates all \(3^6\) messages to reproduce the ordinary minimum distance and weight distribution.

For each \(1\le r\le6\), the verifier enumerates every \(r\)-dimensional message subspace exactly once by its reduced-row-echelon basis. The dimension counts are \(364,11011,33880,11011,364,1\), totaling \(56631\). For every subspace, the support is computed from the nonzero columns of \(BG\) and rechecked as \(24\) minus the number of generator columns annihilated by the row space. These two calculations agree in every case and reproduce the stored support histograms and
\[
(d_1,d_2,d_3,d_4,d_5,d_6)=(12,16,19,21,23,24).
\]

The verifier also canonicalizes all generator columns projectively and confirms that all \(24\) are distinct. A separate normalized search through every three-column support finds exactly \(\{1,15,23\}\), \(\{2,5,11\}\), and \(\{8,12,24\}\), proving the stated dual minimum and multiplicity. It independently locates the unique dimension-two minimizing subcode and its zero-coordinate set. Successful replay prints `VERIFY_OK`.

The computation is exhaustive only for this finite published matrix. It does not establish a classification of all codes with the same parameters or a general family theorem.
