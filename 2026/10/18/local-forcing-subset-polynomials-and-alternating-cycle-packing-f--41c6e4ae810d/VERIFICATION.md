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

# Verification details

The archive includes the executable standard-library programs `verify_q4_automorphisms.py` and `verify_q4_extension_dp.py` and the independent input certificate `q4_orbit_certificate.json`. Their input is a 16-vertex graph whose edges join vertices differing in exactly one binary digit.

Run:

```sh
python3 verify_q4_automorphisms.py q4_orbit_certificate.json
python3 verify_q4_extension_dp.py q4_orbit_certificate.json
```

Observed successful checks: 272 perfect matchings, 384 automorphisms, eight matching orbits, 69,632 forcing-subset decisions, local subset coefficient totals 2,552, 7,040, 6,080, 2,176 and 272 in degrees four through eight, and 9,955 states of the independent completion recurrence. The direct alternating-cycle search and perfect-matching symmetric-difference cycle search agree on every orbit profile, distinguishing cycles by edge sets and packing them by disjoint vertex sets. The packing spectrum is 232 matchings with packing four, 32 with packing three, and eight with packing two.

These are exhaustive finite computations backed by recursion invariants, not an infinite-dimensional proof. The cited hypercube forcing-spectrum papers already imply the common forcing number four. Earlier coverage of the finer census cannot be conclusively excluded. Independent mathematical audit has not been performed.
