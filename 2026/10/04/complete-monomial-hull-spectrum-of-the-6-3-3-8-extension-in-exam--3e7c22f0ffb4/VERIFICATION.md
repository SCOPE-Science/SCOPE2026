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

It implements \(\mathbb F_8=\mathbb F_2(\omega)\) with \(\omega^3+\omega+1=0\) and reconstructs the generator matrix printed in Example 5.6. It checks rank \(3\), the source’s one-dimensional Euclidean hull, and the baseline weight enumerator
\[
1+7z^3+84z^4+189z^5+231z^6.
\]

For every normalized scaling \((1,a_2,\ldots,a_6)\in(\mathbb F_8^\times)^6\), the verifier forms the scaled generator, computes its exact Euclidean Gram rank, and tallies the hull dimension \(3-\operatorname{rank}(GG^T)\). All \(16807\) cases are exhausted. The resulting counts are \(14685\), \(2091\), \(31\), and \(0\) for hull dimensions \(0\), \(1\), \(2\), and \(3\). It also checks the three explicit witness scalings in `artifacts/certificate.json`. No randomized or floating-point computation is used.
