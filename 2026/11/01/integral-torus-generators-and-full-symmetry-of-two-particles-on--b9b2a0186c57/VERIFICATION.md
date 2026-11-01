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

# Computational verification and limitations

Execute `python k44_verify.py` with `sympy` and `numpy` installed. The program constructs the finite cell complex from definitions; no external precomputed matrices are required. It verifies the boundary-square-zero equation, both boundary ranks, all integral Smith factors, the primitive span of eighteen torus generators, the full automorphism character for 1152 graph symmetries, and independent signed Lefschetz trace comparisons for all symmetries. Its output ends with `VERIFY_OK`. The supplied `verification_output.txt` is from an actual run of this exact script.

The exact finite calculation proves this single instance and does not extrapolate to larger graphs. The use of the discrete cubical model relies on the graph's standard subdivision conditions for two particles. Literature-priority limitations are described separately in `REVIEW.md`; no independent scientific audit has been performed.
