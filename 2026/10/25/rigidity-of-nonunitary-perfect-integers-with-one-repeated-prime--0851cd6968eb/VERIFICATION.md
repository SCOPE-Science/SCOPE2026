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

The universal result follows from exact prime-power divisor-sum identities, parity, a geometric upper bound, divisibility in the even-core equation, and monotonicity of \(\sigma(n)/n\) under divisibility. Every case with no repeated prime, one odd repeated prime, and one repeated prime equal to \(2\) is treated. No finite experiment supplies an infinite proof.

Reproduce finite corroboration with `python3 check.py` in this directory. The verifier uses only the standard library and has no downloads or external services. It directly factors every positive integer through \(300000\), computes two divisor sums independently, and compares the solutions and repeated-prime supports to the formula. It also checks \(1782\) additional structured prime-power cases and \(25\) Mersenne-index instances. Observed outcome:

`VERIFY_OK interval 300000 all_nonunitary [24, 112, 1984, 32512] unique_powerful [24, 112, 1984, 32512] extra_exact_families 1782 Mersenne_tests 25`

The checks do not certify mathematical priority. An independently performed audit has not been reported.
