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
# Reproducible verification of the integral Morse-complex calculation

Run `python3 verify_cube_morse.py` in the directory containing this document. Only Python 3 and the standard library are required; no network, external data, or other package files are read.

The script exhaustively compares two distinct constructions of all simplicial faces; verifies the mod-two boundary ranks; constructs an explicit matching on all nonempty faces, then checks acyclicity against the **entire** directed Hasse graph. It explicitly recomputes the critical-cell dimension count, all signed integral gradient-path attaching coefficients, and a unimodular integer reduction of the critical degree-six to degree-five differential. It asserts the existence of exactly 43 unit pivots and a zero residual block. `verification_output.txt` is the recorded stdout of an actual successful checker run.

The checker establishes the exact finite integer chain and matching claims. The corresponding integral homotopy equivalence requires the standard discrete Morse CW equivalence and the Hurewicz/attaching-map argument provided in RESULT.md. This verification does not establish a general theorem for higher-dimensional hypercubes or certify bibliographic uniqueness. External independent audit has not been performed.
