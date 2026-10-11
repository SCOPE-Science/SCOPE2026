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

# Reproducible finite checks

Run `python3 verify.py` with the standard library. The checker uses rational arithmetic for the projection matrix and integer arithmetic for flow conservation, forest tests, and squared polar norms. It checks all balanced trinary circulations in orders \(4\), \(5\), and \(6\) after safe partial-balance pruning (which does not discard feasible completions), then tests the forest criterion exactly. Polar-vertex totals are \(14\), \(24\), and \(3594\), with squared-norm distributions \(\{3:8,4:6\}\), \(\{10:24\}\), and \(\{10:1584,11:1440,12:570\}\) respectively. The origin-centered inradius squares are \(1/4\), \(1/10\), and \(1/12\) in these orders, and the enclosing radius squares are \(1/2\), \(3/5\), and \(2/3\).

A separate halfspace-intersection calculation, using a fundamental-triangle coordinate basis rather than the trinary enumeration, reconstructed the \(14\) and \(24\) polar vertices in orders \(4\) and \(5\), with no nonintegral coordinate residue at the reported precision. That supplementary numerical check is not needed by the proof and is not an independent mathematical audit. Finite checks are not exhaustive over all orders; the all-order theorem is supported by the forest, parity, and symmetry arguments in `RESULT.md`.
