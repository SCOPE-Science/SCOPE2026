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

# Reproduction and limitations

Run `python3 verify.py` with Python 3.10 or newer. Only Python's standard library is needed. The expected final line is `VERIFY_OK`; the packaged `verification_output.txt` contains the output recorded when these exact source bytes were executed. The program enumerates all 65,536 subsets, both face and facet counts, 1,514 Morse matches, and the entire 13,584-incidence directed Hasse graph; it builds and cancels the signed integral simplicial boundaries and confirms every unit pivot. It independently recomputes the original mod-two simplicial boundary ranks and reconstructs a 92-simplex top cycle. Finally it evaluates all 384 graph automorphisms on that cycle and compares all 384 Lefschetz traces with a closed rational character formula.

The verified claims concern only the four-cube's first higher-independence complex. Exhaustive finite verification is not an infinite-dimensional or arbitrary-cube theorem. The full integral homotopy and the rational group action are mathematical conclusions of the finite proof and the stated topology lemmas; the integer-lattice group representation is not separately classified. There has been no independent audit.
