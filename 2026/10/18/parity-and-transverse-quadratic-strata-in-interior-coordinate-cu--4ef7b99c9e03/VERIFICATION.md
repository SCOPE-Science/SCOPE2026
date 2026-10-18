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

The accompanying `hankel_interior_verifier.py` checks exactly the complementary-minor factorization for \(3\le n\le8\), the convolution-square derivative identity through \(n=5\), and the \(A_5\) normal-form coordinate substitution. It is runnable with `python hankel_interior_verifier.py` and SymPy. The symbolic algebra argument in RESULT.md establishes the theorem for all \(n\ge3\) in characteristic zero; the finite tests alone would not.

Singularity scheme structures and exceptional intersections are not claimed. Independent audit has not been performed.
