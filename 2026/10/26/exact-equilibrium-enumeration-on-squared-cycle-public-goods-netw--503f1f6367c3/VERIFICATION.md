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

The self-contained `verify.py` uses Python 3 and only the standard library. Execute it in the same directory with `python3 verify.py`.

The script calculates the sixteen directed local-rule transitions without copying the claimed decomposition; compares every transition against the listed two directed five-cycles, five-state branching component, and single dead state; checks transfer-matrix traces against the binomial count through order 120 using integer arithmetic; and independently exhausts all binary action profiles for each squared cycle with 5 through 17 vertices.

These checks returned `PASS` at review. Mathematical verification of all network sizes comes from the transfer-matrix proof in RESULT.md, not from finite enumeration. Neither independent audit nor independent external validation has been performed.
