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

# Reproducibility and limits

Run `python3 verify.py` in a directory containing the attached checker. The program constructs 28 zero-cells, 96 one-cells and 72 two-cells, evaluates integer differentials and tests their composite for zero. Modulo 1009 it computes differential ranks 27 and 60 and independent-torus rank 12, and directly checks all eighteen torus chains have zero *integer* boundary. Combining these rank bounds gives exact rational ranks. The 1152 signed cubical automorphism traces agree with the two-Specht formula; their character inner product is one, and the full average trace is zero.

This check is finite and exact but is not independent external validation. The top-homology module is rational; integral lattice decompositions and quotient torsion are outside the claim.
