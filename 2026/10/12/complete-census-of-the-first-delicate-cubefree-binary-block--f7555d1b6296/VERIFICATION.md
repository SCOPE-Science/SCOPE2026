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

Run `python3 verify.py` beside `certificate.json`.

Engine 1 generates cubefree prefixes by checking only newly created cube suffixes. Engine 2 independently rescans every whole candidate after each extension. The complete level sets must agree through length \(22\).

Every cubefree word through length \(22\) is then tested for delicacy by flipping each position and scanning the whole mutated word for a cube. The verifier checks that no delicate word occurs below length \(20\), and that the complete counts at lengths \(20,21,22\) are \(2,4,2\).

Finally, it checks the exact listed words and recomputes their reversal/complement orbits, of sizes \(2,4,2\).

Independent audit has not been performed.
