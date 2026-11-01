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

# Reproducibility

Run `python3 verify_c8_k4.py` using Python 3. No external libraries or network access are required. The output must end in `CYCLE8_K4_INTEGRAL_MORSE_VERIFIED`. The stored `verification_output.txt` is the successful exact run.

The checker reconstructs the 32-vertex 96-edge graph, generates all 196226 nonempty faces and face-vector entries, builds 98087 pairs by deterministic vertex-stage matching, topologically sorts all 1457216 oriented Hasse incidences, verifies one critical vertex and 24/27 critical cells in degrees 4/5, computes the exact integer Morse boundary, checks rank 21 by Fraction elimination, and verifies a 21-by-21 determinant of -1 by fraction-free Bareiss elimination. It additionally checks Euler characteristic -2. The printed integer boundary is an inspectable certificate.

Exactness and limits: these are exhaustive finite computations for the specified graph, not probabilistic tests or inference from a sample. An acyclic discrete Morse matching and unit Smith certificate justify the integral homotopy claim using standard algebraic topology. The checker is ordinary reproducible code, not an independent external certification or a statement about other graphs.
