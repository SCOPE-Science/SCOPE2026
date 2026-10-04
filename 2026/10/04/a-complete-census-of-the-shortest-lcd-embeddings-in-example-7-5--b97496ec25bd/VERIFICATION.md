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

The verifier represents \(a+ub\in\mathbb F_2+u\mathbb F_2\) by the two bits \((a,b)\), with \(u^2=0\). It reconstructs the source matrices \(G\) and \(U\), enumerates all \(2\times2\) invertible matrices over the ring and confirms there are \(96\), then combines them with all \(16\) rows \(E\in R^{1\times2}\).

For each of the resulting \(1536\) shortest embeddings it enumerates all \(4^3=64\) ring codewords. It computes the exact ring Hamming distribution, applies \(\phi(a+ub)=(b,a+b)\) coordinatewise, computes the binary weight distribution, and checks that the binary generator consisting of the Gray images of the three rows and their \(u\)-multiples has rank \(6\) and Gram rank \(6\).

The replay checks the full distance census, the two optimal weight-enumerator types and their multiplicities, and the source-displayed embedding. It is exhaustive for the fixed Example 7.5 data; no random search or unproved extrapolation is used.
