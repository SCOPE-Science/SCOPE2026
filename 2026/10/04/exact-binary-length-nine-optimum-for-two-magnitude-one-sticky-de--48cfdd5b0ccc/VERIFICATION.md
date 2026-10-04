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

`verify.py` reconstructs the at-most-two-run magnitude-one sticky-deletion channel directly from maximal constant runs and independently by deleting original positions subject to a distinct-run constraint. It checks the two implementations agree on all \(512\) source words and does not read a precomputed conflict graph.

For the lower certificate it reads `artifacts/codewords.txt`, checks that there are exactly \(120\) distinct binary words of length \(9\), constructs every error ball, and asserts that no received word belongs to two listed balls.

For the upper certificate it reads `artifacts/weights.csv` as exact rational numbers, checks that the total weight is exactly \(120\), enumerates all \(512\) binary source words of length \(9\), and checks that each reconstructed error ball has weight at least \(1\). The weighted disjoint-ball inequality therefore certifies that every correcting code has size at most \(120\).

The committed replay output is in `artifacts/verification_output.txt` and ends with `VERIFY_OK`. The proof is finite: it makes no claim about other blocklengths, does not classify all optimum codes, and does not infer an infinite theorem from enumeration.
