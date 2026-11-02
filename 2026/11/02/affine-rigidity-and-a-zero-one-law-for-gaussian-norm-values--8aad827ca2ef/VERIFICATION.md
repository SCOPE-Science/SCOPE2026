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

# Reproducible checks and boundaries

Run `python3 verify_affine_norms.py` with the Python 3 standard library. The program independently enumerates ordered residues modulo each squared prime for fourteen parameter combinations with primes 3, 7, 11 and 19, verifying the exact count `q*(q*q-1)` each time. It then checks all 194481 ordered coordinate pairs modulo 441 to establish two-prime CRT independence at q=3 and q=7, and verifies explicit positive and negative affine maps on finite sums of two squares.

The recorded successful command emitted `VERIFY_OK local_q_cases= 14 CRT_exact_pairs= 194481 direct_affine_witnesses=6` and displayed local densities 8/27 and 48/343. These checks establish finite statements only. The complete zero–one limit and classification rely on the proof in `RESULT.md`, the classical two-square theorem, and divergence of reciprocal primes congruent to 3 modulo 4. No rate of decay, independence from external mathematical review, or stronger source-priority certificate is asserted.
