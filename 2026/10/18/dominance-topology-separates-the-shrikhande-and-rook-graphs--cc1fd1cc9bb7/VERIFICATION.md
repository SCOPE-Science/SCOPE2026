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

# Reproduction and limits

Place `verify.py` and `verification_output.txt` beside this document, and run `python verify.py` with Python 3.10 or newer. The program uses the standard library only. It enumerates all \(2^{16}=65,536\) vertex masks twice by complementary predicates, independently validates the strongly regular parameters, constructs every face-poset covering incidence, and verifies that the complete matching-oriented Hasse graphs are acyclic using topological sorting.

The Shrikhande complex has 59,819 faces including empty, 29,904 augmented matching pairs, and eleven unmatched nine-cells. After omitting the pair consisting of the empty face and a singleton, the ordinary Morse vector is one zero-cell and eleven nine-cells. There are 461,568 directed incidences and 59,819 vertices in the verified augmented Hasse DAG. This yields the integral wedge of nine-spheres, not just a homology computation.

The rook complex has 59,747 faces including empty, 29,872 augmented pairs, and unmatched dimensions nine (one) and eleven (two); after omitting the empty-face pair there is also one critical vertex. Its ordinary CW model has no ten-cell, proving the stated integral reduced homology without assuming that eleven-cell attaching maps are null-homotopic. There are 460,672 directed incidences and 59,747 vertices in its verified DAG.

The translation trace calculation uses exact signed fixed-simplex Lefschetz sums on every element of the sixteen-element translation group; exact Fourier inversion verifies nonnegative integer representation multiplicities totaling eleven. A single-run transcript of the resulting deterministic checks is included for convenience, but reproducibility rests on the code and fully specified finite bounds, not on the transcript alone. An independent mathematical audit has not been performed.
