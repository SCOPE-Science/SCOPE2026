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

# Reproduction

The file `verify.py` requires Python 3.10+ and the standard library only. Run `python3 verify.py` in the same directory. Its exact terminal output appears in `verification_output.txt`.

Checks actually executed: construction of all independent subsets of the sixteen-vertex hypercube, all seven simplicial boundary ranks over \(\mathbb F_2\), reduced Euler characteristic, exact orientation signs of all fixed simplices for each of the \(384\) graph automorphisms, the equality of the signed Lefschetz character with the stated closed formula, translation Fourier multiplicities, and the invariant-space average. The calculation checks every element of the specified finite graph automorphism group.

The verifier is an exact finite calculation, not a formal machine-checked proof assistant. Rational homology concentration follows from the boundary-rank bounds and Euler characteristic; the representation identification and quotient statements additionally use standard finite-group character theory and rational transfer. Integral representations, all higher hypercubes, and independent scientific audit are not evaluated.
