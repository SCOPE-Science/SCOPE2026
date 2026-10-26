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

# Verification and reproducibility

Execute `python3 verify.py` with Python 3 (standard library only), from the folder containing this file and the verifier. Compare its output with `verify_output.txt`.

The checker constructs each undirected rook graph directly from ordered coordinate pairs and independently enumerates every binary edge assignment for the four finite graphs \(R_{2,2}\), \(R_{2,3}\), \(R_{2,4}\), and \(R_{3,3}\). In that order the exact counts of named two-colourings are \(4,0,0,0\). It also constructs and checks each of the four explicit optimal edge colourings, including the two different four-regular cases, against every edge's adjacent-edge colour counts. Enumeration is complete for these four finite graphs, not an extrapolation to larger parameters.

The infinite two-colour exclusion follows from the proved necessary eigenvector identity and the explicitly derived spectrum. The universal three-colour upper bound at degree at least five is imported from Pękała–Przybyło, arXiv:2608.04122v1, Theorem 4, rather than being computationally certified here. No external independent audit has been performed.
