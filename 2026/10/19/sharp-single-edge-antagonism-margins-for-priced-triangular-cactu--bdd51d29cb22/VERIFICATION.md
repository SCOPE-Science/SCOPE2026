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

# Verification and limits

Run `python3 VERIFY.py` with Python 3 (standard library only). The program checks symmetry improvement for 500 randomly generated *rational* asymmetric triangle allocations, 10 exact formula and cost equalities across price regimes, five exact plateau points at price \(4\), 11 direct rational full-matrix and budget assertions on an eight-vertex cactus with three triangles and one bridge, and 36 exact-rational whole-cactus competitor comparisons. It reports 562 exact rational assertions.

The main theorem is independently reconstructible from four analytical steps given in `RESULT.md`: rank-one Laplacian positivity, block locality, the unrestricted triangle symmetrization inequality and scalar derivatives, and the sharp sum of blockwise necessary budgets. Finite checks cannot exclude counterexamples at untested parameters; full correctness relies on these universally quantified arguments. The literature comparison is a self-review and does not constitute independent novelty certification.
