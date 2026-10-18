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

# Verification of the Heawood cubical top cycle

Execute `python3 artifacts/verify.py` using Python 3 and only the standard library. The program builds the original Fano incidence graph and its edge bisection from the formulas in RESULT.md. It independently forms both integer cubical three-boundaries, performs exact sparse elimination modulo three, constructs a signed integral kernel vector from the original modular nullspace, and checks every integer boundary equation on the original and subdivided vectors.

The verified exact counts are: original three-cell rank \(644\), nonempty boundary rows \(1680\), boundary rank modulo three \(643\), and primitive top-cycle support \(392\); subdivided three-cell rank \(9072\), nonempty boundary rows \(24654\), boundary rank modulo three \(9071\), and primitive lifted top-cycle support \(3136\). The original support test covers all \(644\) cubes. Every one of the \(336\) Fano incidence automorphisms was checked against the signed original cycle, and all six original cube orbits were recomputed.

The modular rank bounds combined with the **exact integer** nonzero cycles prove rank-one rational kernels. Unit coordinates prove integral primitiveness, with no need to infer integral results from finite-field experiments alone. The cubical subdivision deformation retract is invoked only after verifying its published sufficient-subdivision hypotheses. No lower-degree integral homology, subdivision-independent cell-minimality, or independent scientific audit is claimed.
