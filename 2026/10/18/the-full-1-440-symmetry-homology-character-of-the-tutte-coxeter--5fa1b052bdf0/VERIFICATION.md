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

# Verification of the finite scientific claim

Execute `python verify.py` using Python 3 and its standard library. The program directly reconstructs the 15 duads, 15 synthemes, 45 incidence edges, all 476186 nonempty independent faces, and their 3461400 nonempty-face Hasse covers. It checks an acyclic discrete-Morse matching with 238088 pairs, 1 critical vertex, and 9 critical eight-cells. These facts establish the known integral wedge-of-nine-eight-spheres homotopy premise for this specific graph.

Independently of choosing homology generators, an exact reduced Lefschetz computation enumerates orbit-conflict graphs for all 720 six-letter permutations and all 720 color-swapping automorphisms. The computation checks the signed invariant-face identity, the natural S6 character equality to the sign-twisted duad-minus-letter fixed-point function, the irreducible character norm, and the four cycle-type trace and multiplicity statements for the full outer coset. The same computation verifies that every proposed transformation preserves graph incidence.

The tested program terminated successfully with the markers `INTEGRAL_MORSE_OK`, `S6_IRREDUCIBLE_OK`, and `VERIFY_OK`. No finite experiment is used to extrapolate to other graphs or a wider infinite family. Originality remains literature-bounded, including a general incidence-graph duality source whose full text was not inspected. This verification does not constitute an independent scientific audit.
