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

Run `python verify.py` using Python 3 with no third-party packages. It enumerates all possible generator images for \((n,q)=(2,2),(2,3),(2,5),(3,2)\), constructs the full Lie-homomorphism matrices, directly checks the bracket identities and idempotence, and compares each rank stratum with the proposed count. The binary three-generator run additionally canonically reduces all image subspaces and checks the number of distinct retracts and the uniform number of maps per image.

The recorded output is:

```
PASS n=2 p=2 checked=64 idempotents=14 by-rank=[1, 12, 1]
PASS n=2 p=3 checked=729 idempotents=38 by-rank=[1, 36, 1]
PASS n=2 p=5 checked=15625 idempotents=152 by-rank=[1, 150, 1]
PASS n=3 p=2 checked=262144 idempotents=1122 by-rank=[1, 224, 896, 1] distinct-images=[1, 56, 112, 1]
VERIFY_OK free-two-step retracts
```

These are full finite enumerations only for the listed fields and ranks. The unrestricted theorem and exponential limiting inequality are consequences of the proof in `RESULT.md`, not of these finite observations. The verifier covers prime fields; the proof uses only linear algebra and the exterior product and holds over every finite field. No independent audit or external certification is claimed.
