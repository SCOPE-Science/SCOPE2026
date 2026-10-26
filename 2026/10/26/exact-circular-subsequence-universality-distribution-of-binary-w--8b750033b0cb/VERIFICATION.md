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

# Reproducibility of the circular binary universality enumeration

Run `python3 verify.py` in the directory containing the embedded standalone script. The verifier uses only the Python standard library. It compares a direct greedy full-alphabet arch count across **each** rotation against independent maximum-matching and formula calculations for every indexed binary word of length one through seventeen, totaling 262,142 words. An integer polynomial recurrence independently expands the bivariate generating function to length 256 and checks that every row sums to the total number of binary words. Successful execution prints `CIRCULAR_BINARY_SUBSEQUENCE_CENSUS_PASS brute_words=262142 brute_lengths=1..17 gf_coefficients=1..256`.

The infinite theorem relies on the matching characterization, parity-lift lemma, run decomposition, and cycle-enumeration proof in RESULT.md. Finite verification cannot exclude errors beyond its tested range, and no independent specialist mathematical audit has been performed. The fixed alphabet, indexing of source positions, and common cyclic cut must be preserved.
