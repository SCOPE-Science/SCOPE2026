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

Run `python3 artifacts/verify_rook34.py` with Python 3.10+ and no external packages. The included `artifacts/verification_output.txt` is its exact observed output.

The executable independently constructs the twelve open neighborhoods, enumerates 270 nonempty faces and checks the face vector \((12,66,120,60,12)\). It reproduces the 125 matching pairs and 20 critical cells, topologically sorts all 270 nodes of the 792-arc Forman-oriented Hasse graph, recursively eliminates matched edge–triangle pairs over the integers, and checks all 18 critical-triangle boundary degrees equal zero. It also calculates the four binary simplicial boundary ranks \((11,54,48,12)\) directly from the original face collection. All assertions are enforced by exceptions on failure.

The finite calculation is exhaustive for the stated graph; it proves no infinite parameter claim. The homotopy inference additionally uses Forman's discrete Morse theorem and \(\pi_1(S^1)\cong\mathbb Z\). No independent mathematical audit has been performed.
