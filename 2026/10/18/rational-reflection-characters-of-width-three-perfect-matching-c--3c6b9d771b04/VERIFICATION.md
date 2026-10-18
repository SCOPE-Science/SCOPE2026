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

# Exact finite verification and boundaries

The proof relies on an exhaustive finite discrete-Morse certificate and signed fixed-simplex enumeration, each exposed in source code under `verification/`. Install no third-party packages. With both files in that directory, run `python verification/verify_three_row_perfect_matching.py`, then `python verification/verify_reflection_characters.py`.

The first program independently counts domino tilings via recursive vertex-pairing and a three-bit-column transfer, enumerates all faces, chooses every greedy matching stage by its stated deterministic rule, builds the full directed Hasse graph implicitly, checks all indegrees and completes a topological sort, and computes direct mod-two reduced homology for widths \(2,4,6\). It prints `VERIFICATION_OK four exhaustive grid cases` only if every assertion holds. The Hasse directed incidence counts are \(34,1679,62994,2101259\) and every face is processed; the remaining critical augmented faces have dimensions \((),(1),(2),(3,3)\), respectively.

The second program constructs the exact edge-ID permutation induced by each grid reflection, verifies every permutation is an involution, tests setwise stability of every nonempty face, computes inversion parity of the induced vertex order, adds the reduced empty-face contribution \(-1\), and checks the four traces and rational irreducible multiplicities. The respective signed reduced Lefschetz vectors for widths \(2,4,6,8\) are \((0,0,0,0)\), \((-1,1,-1,1)\), \((1,-1,-1,1)\), and \((-2,0,0,-2)\). It prints `VERIFICATION_OK 16 exact signed fixed-simplex sums` on success.

The exact proof uses the standard discrete-Morse theorem and Hopf trace formula, not a probabilistic search or extrapolation. The finite programs do not prove any result for widths beyond \(8\), nor do they certify literature priority, integral equivariant representation, or equivariant homotopy classification. Independent audit has not been performed.
