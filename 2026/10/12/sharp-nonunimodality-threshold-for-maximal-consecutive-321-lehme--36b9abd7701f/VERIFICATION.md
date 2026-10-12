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

# Reproducibility and evidence

Extract the package files preserving relative paths. Execute `python3 artifacts/verify.py` with a standard Python 3 interpreter. The expected stdout is embedded as `artifacts/verify_output.txt`; the verifier uses only the standard library and has no network dependency.

For \(2\le n\le9\), the checker enumerates every legal Lehmer code (a total of \(409112\) codes across these lengths), decodes its permutation, tests avoidance of three consecutive decreasing entries, and determines exact poset maximality with a multidimensional upper-zeta transform of indicator values. It directly computes the defect histogram and compares it to the closed coefficient formula. A wholly separate weighted block-composition enumerator checks \(2\le n\le28\); the coefficient and claimed unimodality verdict are checked for \(2\le n\le120\).

The final line of the stored output is:

`ALL CHECKS PASSED; independent_full_lehmer_posets_n=2..9; total_all_codes=409112; block_compositions_n=2..28; coefficient_and_unimodality_n=2..120`

The checker is a finite regression test. The theorem for all lengths is proved by the published block-structure lemma, the explicit coefficient identity, the two infinite strict-valley families and a finite list of remaining cases. Independent external audit has not been performed.
