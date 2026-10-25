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

# Verification record

The finite integral calculation is independently reproducible from `verify_pg3_arc.py`; install `sympy>=1.13` using `requirements.txt` and execute the program with Python 3.11+.

The program normalizes the nonzero ternary vectors to thirteen projective points; enumerates all candidate faces of cardinalities 2–5; computes determinant conditions modulo three; constructs signed integer boundary maps from oriented simplex deletions; verifies the two consecutive-boundary compositions are zero; computes exact Smith normal forms over the integers; and checks all reported invariant factors, ranks, quadrangle counts and no-five-arc condition.

Expected exact nonzero Smith invariant-factor multiplicities: \(\partial_1:1^{12}\), \(\partial_2:1^{66}\), \(\partial_3:1^{165},3^3\). Exact face vector: \((13,78,234,234)\). All four-point faces are enumerated, and all size-five subsets are tested. Consequently \(H_1=0\), \(H_2\cong(\mathbb Z/3)^3\), and \(H_3\cong\mathbb Z^{66}\).

The finite checker does not establish an infinite-parameter generalization, a homotopy splitting of the cap complex, or uniqueness relative to all literature. The conclusion on projective-frame transitivity follows from the elementary projective-coordinate argument in the proof. A recorded successful program run is included as `verification_output.txt`, but the executable program and its reconstructed matrices, rather than that output log, supply the verification.
