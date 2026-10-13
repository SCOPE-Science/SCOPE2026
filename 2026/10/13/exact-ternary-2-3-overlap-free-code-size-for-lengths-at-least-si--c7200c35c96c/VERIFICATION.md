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

# Reproduction of the finite certificate

Run `python3 verify.py` from the directory containing this file and the verifier. No network or third-party dependencies are needed. The program checks all \(3^9=19683\) disjoint-label assignments on the nine ternary ordered pairs. For each assignment it computes the number of shared candidate length-three strings and optimizes the integer prefix/suffix allocation across its complete range. It verifies a global maximum 132, six maximizing label assignments, and the active-pair maxima vector \((0,0,9,18,36,54,81,108,121,132)\). An independently indexed bitmask enumeration also gives maximum 132.

The program constructs the stated eleven prefixes and twelve suffixes, verifies the disjointness conditions directly, enumerates all resulting length-six and length-seven words, and checks forbidden overlaps of lengths two and three. Successful execution prints `VERIFY_OK`.

The all-length conclusion comes from the general proof: middle symbols are arbitrary once the first three and last three symbols are chosen. Length-six/length-seven word checks are not used as a substitute for that argument.
