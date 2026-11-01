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

# Verification

To reproduce the finite proof, execute `python3 verify.py` using the Python standard library. The expected complete stdout is in `verification_output.txt`. The verifier builds the coordinate-defined graph, enumerates all 262,144 vertex subsets against two equivalent but independently coded face conditions (one using induced degrees, another using 108 minimal three-element forbidden subsets), constructs a complete staged element matching, and explicitly verifies a directed topological sort of all 8,564 nonempty-face vertices and all 42,786 cover relations. It then independently calculates the exact simplicial boundary ranks over the two-element field. All reported assertions pass.

The decisive homotopy certificate consists of 4,273 verified acyclic matched pairs and exactly eighteen critical faces, one in dimension zero and seventeen in dimension five. This is sufficient by integral discrete Morse theory; the mod-two ranks are supplementary. No higher-degree or infinite-parameter extrapolation is made. A second reversed-pivot examination independently found the same critical distribution, but it is not needed for the certificate.

An external independent audit has not been performed.
