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

# Verification of algebraic local conicality

The symbolic proof first localizes at one nonzero homogeneous coordinate and all other nonzero coordinates. It then divides the polynomial by a unit, making the defining function \(e_{k-1}(x)+c e_k(x)\). The denominator-safe transformation \(y=x_k/(1+cx_k)\), with inverse \(x_k=y/(1-cy)\), yields the exact identity \((1-cy)(e_{k-1}(x)+c e_k(x))=e_{k-1}(x_1,\ldots,x_{k-1},y)\). This establishes the local analytic algebra assertion without invoking numerical evidence.

The executable file `checks/banana_local_checker.py` requires only Python's standard library. Run it from an extracted package with `python checks/banana_local_checker.py` and compare against `checks/output.txt`. Exact rational tests cover 1,002 coordinate-support/Jacobian configurations and 176 transformed equations; direct standard-monomial counts give 135 Hilbert-function comparisons. The tests are finite; the proof for all integer parameters uses the displayed identities and standard properties of hypersurfaces. No independent audit was undertaken.
