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

# Verification details

The attached `rolefree_dd_checker.py` evaluates set-valued concepts directly on finite structures, including local singleton selection and global broadcasts. For every possible truncated color-count vector at \(k=0,1,2\), all available pointed colors were tested. Separating formulas at each stated depth were evaluated and both directions of correspondence to the proposed invariant were checked. The verified pointed theories were local: \((1,2,2)\), \((2,6,8)\), and \((4,36,112)\); and global: \((1,2)\), \((2,10)\), and \((4,188)\). The number of tested pointed cases across these classifications was \(1725\).

A further \(48{,}000\) deterministic random comparisons checked invariance of arbitrarily nested formulas under changes to non-singleton multiplicities, for \(k=0,1,2,3\). All checks passed. Run `python3 rolefree_dd_checker.py` with Python 3 and standard-library dependencies only. The final line is `ROLEFREE_DD_CHECKS_OK pointed_comparisons= 1725`.

The full conclusions for all \(k\ge0\) and unbounded formula depth are established by the mathematical proof in `RESULT.md`, not by extrapolation from these finite tests. Historical priority for an equivalent generic monadic-logic theorem has not been independently established. Independent audit is not performed.
