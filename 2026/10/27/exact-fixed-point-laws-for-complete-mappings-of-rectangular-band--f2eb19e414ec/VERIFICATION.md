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

# Reproducible checks

Run `python3 check.py` in an ordinary Python 3 environment. No third-party packages or network are required. The program exhaustively tests *every* permutation of labeled grids of shapes \(1\times1\), \(1\times3\), \(2\times2\), and \(2\times3\), testing the underlying complete-mapping condition directly; it separately evaluates the exact fixed-point polynomial by inclusion-exclusion over subsets. The exact histogram and variance agree in every case. The \(3\times3\) subset computation supplies an additional exact rational-arithmetic check, but it is not an exhaustive search through all \(9!\) permutations. The final printed status is `VERIFY_OK`.

The general all-dimensional bijection, degree-incidence formula and factorial-moment argument are proved in `RESULT.md`. Exhaustive tests on small grids do not establish the infinite-parameter statements. No independent mathematical audit is claimed.
