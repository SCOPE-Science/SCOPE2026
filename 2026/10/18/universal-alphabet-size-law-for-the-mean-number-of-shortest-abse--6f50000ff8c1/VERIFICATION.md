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

# Verification of the finite-alphabet first-moment formula

Run `python3 verify_qary_sas.py` using Python 3. No external packages are required. The program directly enumerates \(17{,}349\) host words across alphabets of sizes \(2,3,4\), computes the greedy universality index, and counts shortest missing scattered subsequences by independent pattern enumeration. It compares these figures to arch-coefficient recurrences derived separately, verifies the diagonal and off-diagonal arch counts on short complete arches, and confirms that the ternary rational identity holds through degree \(35\).

The run produced:

`QARY_SAS_CHECKS_PASS direct_source_words=17349 alphabet_sizes=2,3,4`

`q3_aggregate_n0..8 [3, 6, 12, 60, 204, 576, 1908, 6456, 20508]`

`q3_rational_coefficients_verified_through_n35`

All infinite quantifiers and the asymptotic rely on the combinatorial and singularity proofs in `RESULT.md`, not on those finite computations. The positive-root numerical approximations are informational and are not used as proof certificates. Independent validation has not been performed.
