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
`artifacts/verify.py` uses only the Python standard library and reconstructs the code from the four quadratic factors printed in the source.

It implements \(\mathbb F_4\) with \(\omega^2+\omega+1=0\), multiplies the factors, builds the seven cyclic shifts of the one-generator index-\(3\) quasi-cyclic word, and checks rank \(7\). It exhausts all \(4^7\) codewords, recovering minimum distance \(11\) and the displayed ordinary weight distribution. It separately computes the Hermitian Gram rank and obtains \(7\).

For generalized Hamming weights, every independent subset of generator columns through size \(6\) is row-reduced to a canonical subspace key. Duplicate spans are removed. The verifier counts how many of the \(21\) columns lie in each distinct span, recovers maxima \((0,1,2,3,5,7,10)\), checks the explicit maximizing witnesses in `artifacts/certificate.json`, and derives \((11,14,16,18,19,20,21)\). The dual hierarchy is then computed from Wei duality. No floating-point arithmetic, heuristic search, or solver status is used.
