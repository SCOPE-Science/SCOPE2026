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

The exact calculation uses local factors for 27, r^2 and q to obtain q(r^2+15r-14)=14(r^2+1), hence 0<q<14. The finite discriminant table for all prime q below 14 yields only q=5, r=7. Run `python3 verify.py` for independent standard-library integer replay; its optional finite prime enumeration is not used as the infinite proof. No independent audit has been performed.
