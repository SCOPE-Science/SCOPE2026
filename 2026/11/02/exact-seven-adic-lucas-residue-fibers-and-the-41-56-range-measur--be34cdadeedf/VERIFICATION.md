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

The independent-from-formula computation `artifacts/verify_lucas7.py` uses the defining Lucas recurrence to enumerate one shortest period at all moduli \(7^k\) for \(k=1,2,3,4,5,6\). It independently checks all target frequencies, support sizes, and matrix-period minimality. The exact program was executed successfully. The result was:

```text
LEVEL_OK k=1 modulus=7 period=16 image=7
LEVEL_OK k=2 modulus=49 period=112 image=37
LEVEL_OK k=3 modulus=343 period=784 image=253
LEVEL_OK k=4 modulus=2401 period=5488 image=1759
LEVEL_OK k=5 modulus=16807 period=38416 image=12307
LEVEL_OK k=6 modulus=117649 period=268912 image=86137
VERIFY_OK full_fibers=137256 levels=1..6 minimal_periods_and_exact_multiplicities
```

The unrestricted theorem uses the precise matrix binomial lift, square identity, and isometry arguments in `RESULT.md`. Exhaustive computation through six finite moduli is not infinite certification. Source comparison is qualified: the 2010 and 2011 related primary PDFs were not read in full; their accessible abstracts explicitly concern primes other than seven. There is no independent audit or external proof certification.
