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
`artifacts/verify.py` performs exact arithmetic only.

For the displayed Table 1 components it divides \(x^7-1\) and \(x^7+1\) modulo \(169\) and checks the two nonzero remainders. It constructs the \(7\times7\) quotient-ring multiplication matrices and computes their image cardinalities over \(\mathbb Z_{13^2}\) from unit pivots and the residual \(\mathbb F_{13}\)-rank, obtaining \(13^9\) and \(13^8\).

For the corrected components it verifies the two exact factorizations modulo \(169\), checks image size \(13^4\) for each component, enumerates every one of the \(169^2\) words in each free rank-two component, and reproduces the weight distribution \(1+1176z^6+27384z^7\). It recomputes the two Gram determinants and checks that both are units, proving the LCD property directly.

As a normalization check, it also reduces the printed polynomials modulo \(13\), verifies divisibility there, and exhausts their \(13^2\) codewords to recover minimum distance \(6\). The finite computation does not assess other Table 1 rows or the abstract existence theorem.
