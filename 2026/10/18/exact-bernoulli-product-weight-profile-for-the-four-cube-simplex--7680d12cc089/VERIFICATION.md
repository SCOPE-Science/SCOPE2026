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

# Reproduction and limits

Execute `python3 verify.py` in the directory containing this document and `verify.py`. The program uses only the standard Python library. It recomputes all \(4368\) unordered five-subsets of \(\{0,1\}^4\), cross-checks each integer determinant by two distinct algorithms, reproduces the complete Hamming-weight coefficient vector, checks the entire diagonal polynomial identity with exact integer arithmetic, and evaluates one nonsymmetric rational bias quadruple using exact fractions. A successful run prints `FOUR_CUBE_PRODUCT_WEIGHT_EXACT_CERTIFICATE_OK`.

The extension from the diagonal to all real independent-coordinate parameters relies on the polynomial degree and symmetry proof in `RESULT.md`; finite rational checks alone would not establish it. The resulting formula does not extend to arbitrary vertex weights without another argument. External independent validation has not been performed.
