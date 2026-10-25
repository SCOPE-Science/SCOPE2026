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

# Reproduction checks

Run the five included Python 3 scripts in one directory, without additional libraries. Compare their standard output against their respective `*_out.json` reference files. `pointless_64.py` reduces the proposed invariant to 64 cases and gives the complete 33-form list; `pointless_orbits.py` independently applies exact polynomial substitutions for all 36 coordinate changes. `independent_orbit_check.py` verifies the orbits by a distinct evaluation-interpolation method over the exact finite field with eight elements. `field_verify.py` checks derivatives at all geometric roots over extension fields; `count_genus3.py` uses polynomial gcds. The extension-field and gcd checks agree for all counted smooth forms.

The enumeration is exhaustive because every pointless equation has all three quartic coefficients among four explicitly specified polynomials. The group-action check covers all 36 factorwise invertible matrix pairs; it is not a test of abstract curve isomorphism. Algebraic smoothness is proved by polynomial derivatives, not merely by checking rational points. Independent mathematical review has not taken place.
