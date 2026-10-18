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

# Verification record

The exact proof certificate is the binary-compressed JSON object `grid4_morse_certificate.json.gz`; its keys identify the six rectangular grid sizes and store all elementary simplicial removals plus critical-face declarations. `grid4_morse.py` loads the certificate and independently reconstructs the graph, every independent four-set, every nonempty face, every codimension-one incidence, and all matching incidences. It checks that matched free faces satisfy unique remaining coface constraints, that all declared critical faces are maximal, and that **all** oriented Hasse arrows form a directed acyclic graph. This checks full finite validity, not merely a random sample. The reduced Euler identity and all eight square-symmetry signed fixed-simplex character computations are then recomputed, followed by exact integer character-table inner products.

Execution of `python grid4_morse.py` on the files packaged here succeeded, for face counts 389, 1415, 3641, 4811, 11727, 27597 and matching-pair counts 192, 697, 1792, 2363, 5753, 13518. The Morse critical profiles are one degree-zero cell and respectively 4, 20, 56, 84, 220, 560 degree-five cells. No theorem about sizes outside this finite range and no equivariant homotopy equivalence is certified. An independent audit is not performed.
