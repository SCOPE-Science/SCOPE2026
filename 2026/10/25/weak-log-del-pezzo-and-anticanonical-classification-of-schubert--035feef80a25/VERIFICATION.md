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

# Verification of the anticanonical classification

Run `python3 verify.py` using standard Python 3. The checker models total exceptional transforms as a diagonal intersection lattice and verifies both canonical-pullback identities, anticanonical volumes, intersections with the strict infinity curve and every exceptional curve in representative Kronecker profiles. It enumerates 304 small profiles, ending with `VERIFY_OK`.

The mathematical proof of positivity for arbitrary irreducible nonexceptional curves uses their positive degree and nonnegative intersection with the distinct effective infinity curve on the smooth blow-up. Finite enumeration cannot prove that universal geometric step. The theorem uses the established resolution and cyclic-quotient description in Galgano–Gesmundo–Keneshlou and standard characteristic-zero base-point freeness. There is no independent audit or computer-algebra certification of the source's geometric theorems.
