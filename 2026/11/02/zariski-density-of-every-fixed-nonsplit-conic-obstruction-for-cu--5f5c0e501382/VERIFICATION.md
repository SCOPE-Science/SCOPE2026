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

Run `python verify.py` with Python 3 and SymPy installed. It checks by exact Gaussian-rational polynomial arithmetic the semilinear conjugation identities for the Hamilton conic, nonzero resultant \(675\), distinct fixed points (discriminant \(27760\)), and distinct fixed-point multipliers (the displayed degree-four polynomial has discriminant \(67927190083003088896000\)). Distinct fixed-point multipliers prove trivial geometric automorphisms for that explicit witness.

The full theorem over *every* nonsplit rational conic follows from the scalar-independent eight-dimensional \(\mathrm{PGL}_2\) linearization, twisting of vector spaces, geometric dominance of the conjugacy quotient, uniqueness of descent on the automorphism-free locus, and density of rational points in nonempty affine opens. The finite symbolic check cannot prove those geometric steps; they are established in the proof.

The assertion does not give height asymptotics, local density, or independent certification.
