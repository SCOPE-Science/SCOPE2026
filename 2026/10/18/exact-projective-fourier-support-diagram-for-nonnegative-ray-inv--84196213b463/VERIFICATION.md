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
The unnormalized finite-field character sum is proved in RESULT.md. A zero-frequency coefficient is strictly positive for nonzero nonnegative input, and every nonzero Fourier coefficient is constant on its dual ray. The algebraic cases for central value positive/zero are verified by the exact identity \(a-S+q b_i\). Constructive weights in the proof establish all sufficiency cases without numerical approximation.

Run `python3 check_support.py` to reproduce finite direct-transform tests and bounded small-weight enumeration. The checker covers sample fields rather than all prime powers; universal correctness follows from the printed proof, not enumeration. All test-dependent assertions are inside the included script. Independent validation has not been performed.
