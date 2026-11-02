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

Install Python 3 and SymPy. In the directory containing the accompanying scripts, run `python verify_symbolic.py` and `python verify_incidence.py`. These programs depend on no external datasets or network access.

The first checker reconstructs the exact defining polynomial, checks the nonsingularity of the second conic, verifies all four tangents of the first conic and the four cycle vertices of the second, and checks the squared intersection divisor of the two conics. It also substitutes an explicit homogeneous degree-four syzygy into the Jacobian identity and computes over the exact rationals that the degree-three syzygy map from \(S_3^3\) to \(S_{10}\) has zero kernel. This provides an independently replayable witness for \(\operatorname{mdr}=4\). It does not invoke floating-point calculations.

The second checker enumerates abstract pair-incidence assignments for the only numerically possible singularity baskets; it independently finds only six labeled configurations, all relabelings of the four-cycle. This combinatorial finite check is redundant with the proof. It does not certify the nonexistence of geometrically unrealizable configurations by itself, nor does it establish projective equivalence; those are addressed by the exhaustive case argument and pencil calculation in the theorem.

Published inequalities and the near-freeness criterion are applied under their stated hypotheses; external independent mathematical auditing remains unperformed.
