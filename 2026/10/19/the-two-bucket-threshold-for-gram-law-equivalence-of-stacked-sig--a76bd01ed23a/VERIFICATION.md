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

# Reproduction and verification

Execute `python3 check.py` with Python 3's standard library. The actual test execution returned:

```
PASS: 29317 exact-rational assertions including Gram laws for three-coordinate input
```

Tests enumerate the exact collision distribution for the signed-hash blocks, all ordered positive block compositions through twelve output rows, the two-row transformed sign outcomes, and full three-coordinate Gram histograms for one-, two-, three- and four-row single blocks. The last calculation confirms the two smaller block laws agree with independent dense signs and the two larger ones do not. The test suite also checks elementary uniform-normalization variance formulas separately; those are not premises of the width-dependent normalization theorem. The proof in `RESULT.md` supplies the general finite-dimensional conclusions independently of these finite enumerations.

No randomized simulation, high-dimensional exhaustive search, external certificate, or independent mathematical audit is claimed.
