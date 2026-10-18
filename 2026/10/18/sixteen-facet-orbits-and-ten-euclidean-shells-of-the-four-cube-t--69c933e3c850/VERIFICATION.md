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

# Exact finite verification

Run `python3 verify_q4.py`. The standalone script uses only Python 3 standard-library modules `collections`, `fractions`, and `itertools`. It requires no network, local tables, or other files.

The first enumeration covers **every** assignment of fifteen signs on a fixed spanning tree of the four-cube, and explicitly tests all thirty-two graph edges. It obtains 990 admissible potentials. The second enumeration grows Hamming-weight layers by intersecting all parent constraints; it gives exactly the same set independently of the first tree parametrization. A third phase generates all \(2^4\cdot4!=384\) cube automorphisms and both signs, exhaustively partitions the 990 potentials into sixteen disjoint orbits, and checks the sixteen exact representatives with their orbit sizes and squared Euclidean norms. The group-action result is cross-checked by Burnside's fixed-point sum of 12,288. Exact rational arithmetic verifies the ten squared-norm shell counts and their total of 990.

The saved script was run to completion, emitting `ALL EXACT CHECKS PASSED`. Its exhaustive coverage proves the finite-domain assertions conditional on the mathematical identification of polar vertices with all-edge-tight functions and on the correctness of simple integer program semantics. The proof and script do not address higher-dimensional cubes or independent scientific validation.
