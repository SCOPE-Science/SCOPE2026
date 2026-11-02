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

# Finite certificate verification

Run `python3 verify.py` with `pf_cert.json` in the same directory. Python 3.9+ standard library is sufficient; no solver is needed.

The script independently generates the regular-paperfolding prefix with the odd-part arithmetic definition; enumerates all nonempty substrings at each of the four lengths; forms the distinct-factor set; checks that some occurrence of every factor crosses one of the specified upper-bound positions; reconstructs every lower-weighted factor and all its exact occurrences; and verifies the integer per-position load bound and numerator totals.

Expected terminal marker: `PAPERFOLDING_ATTRACTORS_VERIFY_OK`. The complete exact factor counts are \(6479,25775,102767,410351\). The rational certificate denominator is \(16\), with packing numerators \(80,92,96,102\). Each is sufficient after ceiling to match the corresponding upper witness size \(5,6,6,7\). These checks cover the *entire* finite word in each case. Exact enumeration is a valid finite proof but makes no inference about infinitely many prefix lengths.

Only self-review has been performed. Independent mathematical audit: not performed.
