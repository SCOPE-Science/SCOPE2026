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

The standalone programs `verify.cpp` and `verify_symbolic.py` were executed on the actual packaged source. C++ computes entire ordered-triple atomic profiles for the two extraspecial families at quotient dimensions two, four, and six; the Python implementation independently recomputes dimensions two and four. They agree on three rank-three classes in the tested degrees, common signs at order 32, the seven/eight pair-profile sizes for noncentral involutions/order-four elements, and the order-32 rank-four sign witness. All detailed results appear in `verification.log`.

The infinite proof is the local extension-table lemma in `RESULT.md`: an arbitrary third point is either in the preimage of the two selected quotient vectors' span or is generic of one of two possible square types, which both occur outside that span from quotient dimension four onward. The standard nondegenerate four-dimensional quadratic subspace reduction and the explicit plus/minus table then establish full generality. The tests alone would not establish any claim beyond the enumerated degrees.

Limitations: no independent audit; no validation of different first-order languages, larger ranks, or all related group families.
