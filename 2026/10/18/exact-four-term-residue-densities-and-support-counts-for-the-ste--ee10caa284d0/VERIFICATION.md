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

Run `python3 verify.py` with Python 3 standard library. It checks all residue quadruples for moduli 2 through 12 against exact rational formulas, both support counts and total mass; it also independently checks Stern's even/odd four-term identities for 4096 parent indices. One finite empirical check is diagnostic, not an infinite proof. The mathematical derivation uses the published primitive-pair equidistribution theorem and an explicit summable tail. No separate external audit has been performed.
