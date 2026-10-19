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

# Verification notes

The standalone Python 3 standard-library program `verify.py` constructs prefixes in two independent ways (iterated substitution and a base-\(q\) trailing-digit formula), verifies their equality for \(25{,}000\) entries at each \(q=2,\ldots,9\), and compares all directly observed minimal absent factors through length \(75\) to the stated parametric formula.

To replay, run `python3 verify.py`. The expected success line is `VERIFY_OK q=2..9 independent_generators_N25000 full_absent_factor_enumeration_lengths_1..75`.

The finite computation enumerates factors of a particular long prefix; it does not by itself certify that all infinite-word factors at these lengths have appeared. Infinite completeness follows instead from the mathematical proof, which handles arbitrary lengths and all \(q\ge3\). No independent scientific audit has been performed.
