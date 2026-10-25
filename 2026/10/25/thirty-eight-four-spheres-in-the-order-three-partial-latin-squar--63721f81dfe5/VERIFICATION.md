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

# Reproducibility evidence

The packaged `verify_latin3.py` is fully standalone and uses only the Python standard library. The exact invocation `python3 verify_latin3.py` was run and completed with its final `VERIFY_OK_LATIN3_PARTIAL_SQUARE_HOMOTOPY` marker. Its output is preserved in `verify_output.txt`.

Its assertions independently check all compatible assignment sets, the size and maximal-face distributions, each matching edge, the absence of directed cycles in the 56,619-edge oriented Hasse diagram, the exact integral Morse boundary coefficients \((-1:7,0:23,+1:9)\), and their unit gcd. Independent mod-two ranks corroborate the homology dimension but are not used to prove the integral homotopy equivalence.

The proof's conclusion uses the primitive integral attaching-degree vector and standard CW cofiber equivalences. Only the finite order-three complex is verified, and no independent scientific review or general-order result is asserted.
