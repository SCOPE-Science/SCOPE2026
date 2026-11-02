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

# Mathematical verification

Run `python3 check_firebreak.py` next to `RESULT.md`; no third-party Python packages are required.

Actual result on the included source: `PASS: 2968 independent exact/finite checks`. The checker enumerates all intrinsic ignition assignments for small rings, checks the adjacent-difference identity in exact rational arithmetic, compares numerically isolated roots over numerous ring sizes, and verifies exact four-regime examples at eight patches.

The infinite-size theorem is established by the symbolic factorization and the continuous one-peak argument in `RESULT.md`. Numerical root approximation is not presented as proof of ordered roots at arbitrary ring size. No external or independent audit is claimed.
