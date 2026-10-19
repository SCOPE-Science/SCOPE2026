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

The analytical proof in `RESULT.md` verifies every integer parameter \(n\ge1\) and every finite itinerary. On each side, `D` supplies a full one-step staying branch, `H` supplies a full crossing into the opposite small interval, and that interval returns to the entire opposite half after \(n\) forced same-sign steps; thus no admissible word is omitted. The entropy recurrence and Lambert-W asymptotic follow from these full-branch identities.

Run `python3 verify.py` using the Python standard library. A successful replay tests all 12,276 sign words of lengths 1–10 for parameters 1–6 and compares the exact combinatorial admissibility criterion with positivity of the computed interval image; it checks the root equation, critical-orbit identities and independent renewal counts. Numerical root finding and finite word enumeration are non-certifying diagnostics; neither is substituted for the mathematical proof. The claims do not concern boundary preimage coding or metric entropy.
