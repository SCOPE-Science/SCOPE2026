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

Run `python3 verify.py` next to `certificates.json`.

The replay performs the following exact checks:

- regenerates the canonical concrete classes of sizes \(90\), \(120\), and \(180\);
- enumerates all thirteen matchings of the length-six coordinate path and hence every allowed radius-one channel action;
- checks that the explicit center lists have sizes \(9\), \(15\), and \(17\) and cover their entire classes;
- checks every dual weight is a nonnegative exact rational number;
- checks every possible center has total dual ball weight at most \(1\);
- checks the three dual totals are exactly \(9\), \(15\), and \(17\).

These checks establish both sides of each equality. The verification does not address the two other multiset types in the motivating table and does not claim a global value for \(K_q(6;1)\).
