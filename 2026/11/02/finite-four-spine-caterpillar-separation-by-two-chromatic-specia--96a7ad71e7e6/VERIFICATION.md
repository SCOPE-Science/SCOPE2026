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

The exact finite certificate is in `verify.cpp`. It enumerates every canonical four-spine type of total order between 6 and 200 inclusive, then compares two 64-bit residue evaluations of the fourth principal specialization within each order. The complete replay returned `RESULT N<=200 CLASSES=31060953 COLLISIONS=0`. The independent small checker `verify_small.py` returned `INDEPENDENT_SMALL_OK 40` by comparing spine-sum formulas to direct vertex-coloring enumeration through order eight and by checking larger reversal cases.

The explicit closed class count is \((\binom{198}{4}+4851)/2=31{,}060{,}953\). Zero modular signature collisions prove the required separation because exact polynomial equality implies equality of modular evaluations. Randomness, statistical collision estimates, and floating-point approximations are not used. There is no claim for more than 200 vertices, for spine lengths other than four, or for independence of the present review.
