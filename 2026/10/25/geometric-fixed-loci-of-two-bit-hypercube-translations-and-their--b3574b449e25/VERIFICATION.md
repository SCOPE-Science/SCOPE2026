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

The standalone script `verify_translation_fixed.py` uses only the Python standard library and may be run as `python verify_translation_fixed.py`.

It exhaustively checks all 27 pairs consisting of a cube dimension from 2 through 7 and a nonzero translation support weight, across integer scales 0, 1, and 2. For each present orbit graph it independently enumerates every orbit and all cross-distances, tests every possible orbit edge, checks absence of triangles, verifies connectivity and integer cycle rank, and compares the result with the explicit cube-graph coordinates.

For each weight-two case it calculates the character multiplicities by finite Fourier inversion on the complete signed vertex/edge trace and checks the closed weight formula. It also constructs and verifies 1,404 integral triangular fillings of elementary cube squares at scale three, checking admissibility and exact signed boundaries.

The observed final line is `VERIFY_OK support_cases=27 scale_three_square_fillings=1404; all orbit-graph, homology, and character checks passed`.

The checks are finite corroborations; the complete proof is the uniform orbit-complex, cube-square filling, and character arguments in RESULT.md. They do not establish unexamined later-scale topology or independent validation.
