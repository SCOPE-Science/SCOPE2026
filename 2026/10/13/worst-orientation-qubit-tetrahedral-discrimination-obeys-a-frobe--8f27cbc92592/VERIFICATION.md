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
# Reproducible verification

Run `python verification/verify.py` with Python 3 and NumPy. The script recomputes the regular-tetrahedron frame Gram sums, constructs principal-axis orientation matrices for eight physical Bloch quantum channels, checks four-outcome POVM positivity and completeness against the actual output density matrices, and independently obtains the smallest enclosing ball from all possible affinely independent 1-to-4-point supporting sets. It verifies exact-form numerical evaluations of the claimed worst-orientation probability and compares against 288 seeded alternative rotations.

Expected concluding output: `VERIFY_OK channel_cases=8 random_rotations=288 frame_and_POVM=passed geometric_minimax=passed`.

The proof is analytical and covers every qubit CPTP channel, every input rotation and equality orientations. Finite floating-point tests are supplemental checks, not proof for the continuum of channels or numerical certification of priority. The geometric-radius enumeration only tests finite examples. An independent scientific audit has not been performed.
