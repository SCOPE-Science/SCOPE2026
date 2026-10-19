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
# Reproducibility

The standalone `verify.py` uses only Python's standard library. Execute `python verify.py` in the directory containing the extracted embedded artifacts.

The program checks all partitions through matrix dimension \(6\) over prime fields of characteristics \(2\), \(3\), and \(5\): \(318\) comparisons between direct ranks of \(B\mapsto\sum_{i=0}^{m-1}A^iBA^{m-1-i}\) and the claimed Jordan-partition formula. It exhaustively enumerates every dual coefficient matrix in \(9\) small prime-field cases and \(4\) finite-field cases over \(\mathbb F_4\). The latter field is implemented as the quotient by \(t^2+t+1\), avoiding treating prime powers as prime integers.

Expected terminal markers are `RANK_TESTS_PASS 318`, `EXHAUSTIVE_TESTS_PASS 9`, and `GF4_TESTS_PASS 4`. Every individual exhaustive distribution is printed.

These checks are finite; the arbitrary-size and arbitrary-field conclusions rest on the proof in `RESULT.md`, particularly the truncated-polynomial multiplication rank lemma. The accompanying results have not undergone an independent audit.
