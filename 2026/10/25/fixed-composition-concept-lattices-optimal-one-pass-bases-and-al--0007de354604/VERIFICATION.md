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

The standalone `verify.py` uses exhaustive model intersection, rather than the proof's quota-closure routine, as its oracle. It constructs all models independently, checks every one-round implication outcome from every possible input set, checks that the proposed premises are exactly all inclusion-minimal nonclosed sets, checks closed-set counts and checks each interval Möbius value by the recurrence.

Tested multiplicity vectors and outputs:

- \((1,1,1)\): 6 models, 36 rules, 17 closed sets, 49 nontrivial intervals, signed feasible sum 4.
- \((2,1,1)\): 12 models, 64 rules, 56 closed sets, 277 intervals, signed feasible sum -5.
- \((1,1,1,1)\): 24 models, 144 rules, 114 closed sets, 609 intervals, signed feasible sum -15.
- \((3,1,1)\): 20 models, 100 rules, 157 closed sets, 1251 intervals, signed feasible sum 6.
- \((2,2,1)\): 30 models, 135 rules, 247 closed sets, 2061 intervals, signed feasible sum 6.

The final checker reports `VERIFY_OK closure=PASS minimal_premises=PASS direct_basis=PASS interval_mobius=PASS`. It enumerates finitely many examples; the theorem's universal quantifiers are established by the proof, not by that output. An external independent audit has not been performed.
