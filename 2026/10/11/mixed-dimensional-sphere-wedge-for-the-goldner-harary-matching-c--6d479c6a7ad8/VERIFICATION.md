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

# Verification of the Goldner–Harary matching-complex decomposition

The package contains the complete integer Morse certificate `MORSE_CERTIFICATE.json` and two stand-alone verifiers. From the package directory run:

`python verify_goldner_harary.py MORSE_CERTIFICATE.json`

`python verify_independent.py`

The first verifier reconstructs the eleven-vertex, twenty-seven-edge graph, enumerates all 1441 nonempty faces, regenerates the matching, validates 662 nonempty pairs, and confirms acyclicity by a directed topological sort over all 4677 face incidences. Its 49-by-67 integral Morse boundary is reconstructed by oriented simplex incidence and signed gradient-path elimination. It checks rational rank 19 and recomputes a maximal integer minor with determinant 1. The critical CW cells are one zero-cell, 49 two-cells and 67 three-cells, so elementary homotopy-theoretic reasoning gives \(\bigvee^{30}S^2\vee\bigvee^{48}S^3\).

The second verifier does not use the certificate or Morse matching. It independently enumerates pairwise disjoint edge sets by combinations and checks mod-two boundary ranks \((26,193,390,72)\) and reduced mod-two Betti numbers 30 in dimension two and 48 in dimension three. This corroborates the enumeration but cannot by itself establish the integral homotopy type.

The two verifiers were executed from the embedded package files. Reproducibility is limited to the specified finite complex and mathematics used to translate signed cellular data into homotopy. An independent scientific audit and independent formal validation were not performed.
