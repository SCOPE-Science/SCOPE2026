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

# Reproduction and limits

Run `python3 verify_witness.py` from the extracted artifact directory. Python 3 standard library suffices; no external files, downloads or mathematical packages are required. The program computes finite rational Taylor jets, checks the degree-three Schwarz map against a finite-Blaschke representation, verifies the exact series identity defining the function, and recomputes the determinant and two rational gaps. Its successful output contains `PASS` and the three fractions.

The verifier establishes the rational arithmetic exactly, rather than using floating-point tolerances. Global Schwarz mapping follows from disk automorphisms, and global univalence follows from positivity of \(\operatorname{Re}\Phi\), starlikeness of the odd part, and the classical close-to-convex criterion. These are mathematical arguments in `RESULT.md`; they are not inferred from finite coefficient arithmetic. The witness is not asserted to be an extremizer for the unknown sharp bound.
