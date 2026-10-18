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

Run `python verify_coxeter.py` (Python >= 3.10 and NetworkX 3.x). The code uses exact integer, set, bit-mask and permutation arithmetic. It verifies all 196,009 augmented independent faces; all 97,999 unit Morse pairs; acyclicity of the complete matched Hasse diagram; the eleven critical cells; the integer Morse boundary matrices and their ranks; all 336 group automorphisms; direct signed-face traces for one representative of every possible order; and irreducibility both for 336 automorphisms and the 168 Fano collineations. The finished, embedded verifier was extracted and executed before acceptance, and the reported assertions passed.

The direct traces cross-check the orbit-quotient Lefschetz signs. Character inner-product computations are exact sums of integers. The finite group calculation uses all automorphisms enumerated by graph isomorphisms; no claims are made about representations of larger graph families or about the integral equivariant lattice. Scientific originality retains the explicitly named full-text access uncertainties.
