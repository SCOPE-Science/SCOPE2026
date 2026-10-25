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
# Reproducible verification

From the extracted files execute `python3 verify.py` (standard Python 3). The program exhaustively constructs all distinct scattered subsequence strings by independent set extension, then identifies abelian squares by direct half-count comparison for each of the \(343\) triples with \(0\le a,b,c\le6\). Each length-specific count matches the closed formula. An independent summation over fixed outer-run differences checks totals for \(4913\) triples with all parameters through \(16\). It also prints scaled witness values. The expected final line is `VERIFY_OK`.

The infinite proof requires the classification lemma, a uniform \(O(n^2)\) lattice approximation, the strict balancing argument for a symmetric diagonal-distance kernel, and one-variable optimization. These analytic arguments appear in RESULT.md. The tests are finite and provide no exhaustive evidence at unbounded lengths. Independent audit status is not performed.
