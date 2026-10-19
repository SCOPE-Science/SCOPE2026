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

The exact formulas follow analytically from the two half-weight inequalities defining a median, preservation of the sorted opinion order, and solutions of constant-coefficient linear equations. The full argument covers all positive real times, arbitrary initial opinions (including ties), and every permitted homogeneous self-weight.

To reproduce finite consistency checks, use Python 3 standard library and run `python3 verify.py` in the same directory. The script independently recomputes the weighted median for each agent from the weight inequalities and checks the time derivative of the displayed formulas at several rational values of the exponential time variable. It also checks ordering. A successful run reports 1,755 rational input profiles and 56,160 individual exact-rational equation checks. These samples are not an exhaustive test over all real weights or opinions; the preceding analytical proof establishes the universal conclusion.

Scientific constraints: this theorem is specific to a homogeneous full influence graph with nearest-own tie breaking. Literature overlap beyond the inspected sources remains possible. Self-review does not constitute independent audit.
