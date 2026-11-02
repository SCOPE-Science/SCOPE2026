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

# Reproducibility

From the package root, compile `verification/census.c` with a standards-compliant C11 compiler:

`cc -O3 -std=c11 -Wall -Wextra verification/census.c -o census`

Then execute `./census 19` to enumerate all binary host words through length nineteen and print maximum counts, tie multiplicities, first maximizing hosts, and per-length score sums. Execute `python3 verification/crosscheck.py` for an independent exhaustive reconstruction through length sixteen.

The C implementation enumerates all \(1,048,574\) hosts, including \(524,288\) at length nineteen, using exactly represented subsequence sets. The shorter independent Python computation tests all candidate hosts up to length sixteen with separately generated Lyndon-pattern sets. No finite enumeration is used as evidence of an infinite optimum. Independent audit: not performed.
