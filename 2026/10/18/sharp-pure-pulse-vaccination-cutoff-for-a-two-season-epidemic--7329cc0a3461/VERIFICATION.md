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

The analytical verification consists of the cyclic-arc renewal representation, its strict-convexity consequence, the impulse-response directional derivative, and the two endpoint derivative inequalities. All assumptions and equality cases are stated in RESULT.md.

Running `python3 verify.py` checks 54 independent finite-difference first variations of exact period maps and 150 parameter families with arbitrarily redistributed vaccine pulses, including strict improvement above the predicted threshold. The checker also confirms the published example's cutoff numerically. The printed `VERIFY_OK` reports only these finite checks; it is not an exhaustive search over measures, a formal proof system, or an independent audit. The full mathematical conclusion follows from the accompanying analytic proof. No independent review has been performed.
