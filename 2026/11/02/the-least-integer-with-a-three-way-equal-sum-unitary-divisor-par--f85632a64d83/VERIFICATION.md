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

The exact Python standard-library verifier `verify.py` reconstructed all unitary divisors of \(30030\) from the gcd definition. It confirmed there are \(64\), that the explicit sets of sizes \(4\) and \(5\) are disjoint subsets, and that the complement has size \(55\). It checked total sum \(96768\), three class sums \(32256\), exact product bound \(1152/385<3\), and minimal six-prime product \(30030\). Successful output:

`VERIFY_OK: unitary_divisors=64; class_sizes=4,5,55; class_sum=32256; support_bound=1152/385; least_integer=30030`

The code directly verifies finite computations; the proof of exclusion for arbitrary prime powers and the least-integer argument appear in `RESULT.md` and do not depend on a numerical search cutoff. Sources are literature evidence, not an independent audit.
