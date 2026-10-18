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

# Verifiable mathematics

Run `python verify_census.py` using Python 3 and its standard library. The program constructs cyclotomic polynomials exactly and computes determinants of **every** three-by-three cyclic Fourier minor at the moduli specified in `RESULT.md`. The remainder of each determinant modulo \(\Phi_N\) is zero if and only if the complex Fourier determinant is zero, since \(\Phi_N\) is the minimal polynomial of the chosen primitive root. This eliminates floating-point singularity thresholds.

When the determinant vanishes, the program detects rank one by the equivalent necessary-and-sufficient condition that every two-by-two Fourier minor vanishes, implemented by exact divisibility of row/column difference products. The independent divisor formulas are evaluated using integer arithmetic and Möbius inversion, then compared against direct cyclotomic counts. The record `verification_output.txt` is a captured successful replay of this exact packaged program.

The universal determinant-rigidity and Möbius inversion steps are proved in `RESULT.md`; finite verification does not establish an infinite theorem on its own. No external audit has been performed.
