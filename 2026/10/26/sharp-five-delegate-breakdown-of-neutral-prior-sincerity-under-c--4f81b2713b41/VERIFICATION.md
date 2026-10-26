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

# Verification record

Run `python3 verify_cpsr.py` with Python 3, without external packages. The checker recomputes normalized CPSR payments from every opponent-ballot pattern with exact rational arithmetic, including weighted ties and the rule requiring at least a numerical majority in the winning coalition.

Expected exact outputs:

- Five-member conditional-on-state transfer advantage divided by budget: `-616489/33459375`.
- Five-member conditional-on-good-signal transfer advantage divided by budget: `-2465956/167296875`.
- All 32 possible five-member weighted-majority splits have no tie.
- Analytic three-member formula matches direct enumeration, with positive differences, on 5,184 rational profile–representative comparisons.

The universal three-member statement is established by the elementary inequalities in the accompanying proof, not by the finite code checks. The complete five-member witness is certified by the finite sixteen-pattern expectation and its independent binomial derivation. All calculations condition on sincere voting by the other representatives; no independent review has been performed.
