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

The executable `verify_orbit.py` uses only the standard library's exact rational arithmetic. It checks the four displayed rational orbit points, the branch of each point, the four exact image identities, primitive least period four, and \((84/25)(16/25)^3=344064/390625<1\). It also checks exact rational instances of the necessary bound and confirms the threshold comparison \((4-3/4)(3/4)^4=1053/1024>1\). Execution completed successfully.

The mathematical exclusion for all integers \(k\ge4\) and every parameter is proved symbolically in `RESULT.md`. The finite rational tests are not an exhaustive search through parameters and are not used as a substitute for the proof.

The relevant sections of arXiv:2510.11441v1 were inspected for the map definition, previously established itinerary statements and Question 8.1. An equivalent result under unrelated terminology remains a bibliographic risk. Independent audit has not been performed.
