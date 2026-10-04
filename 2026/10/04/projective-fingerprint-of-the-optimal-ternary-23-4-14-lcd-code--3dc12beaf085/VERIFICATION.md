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
`artifacts/verify.py` uses only the Python standard library and begins from the published \(4\times23\) generator matrix.

It verifies rank \(4\), computes \(GG^T\) and its nonzero determinant, enumerates all \(81\) ternary codewords, and reproduces the exact Hamming weight distribution. It normalizes the generator columns projectively, checks that all \(23\) are distinct, constructs the \(40\) points and \(130\) lines of \(\mathrm{PG}(3,3)\), and recomputes the complete line and hyperplane intersection spectra.

For the stabilizer, it colors each pair of code points by the size of the intersection of its joining projective line with the \(23\)-point set. Exact backtracking enumerates all color-preserving permutations. Every projective stabilizer must occur in this list. The verifier obtains exactly four permutations and checks that each is realized by an explicit invertible projective matrix from `artifacts/certificate.json`; their orders are \(1,2,2,2\). Thus the projective stabilizer is exactly \(C_2\times C_2\).
