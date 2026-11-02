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
# Verification of the mathematical claim

Run `python check.py` with Python 3 and its standard library. The expected marker is `INCIDENCE_ADJOINT_MATROID_CYCLE_OK 17`. The checker implements actual finite-field arithmetic (with \(\mathbb F_4\) represented by the polynomial \(t^2+t+1\)), constructs the arrow-output matrix for each inner adjoint operator on the full algebra, and performs elimination from scratch. It checks the claimed pointwise rank equality for every algebra element in each of 17 small configurations; no graph-rank formula is used to compute the direct matrix rank.

It separately calculates the graphic subset expansion for each configuration, divides element-rank counts by the exactly known center size, and compares them with the two closed formulas for forests and cycles. Tested patterns include a star, a path, a disconnected forest, triangles, four-, five-, and six-cycles, a pendant leaf, and two four-cycles joined at one vertex; the test also reverses the orientation of a cycle. Characteristic two, odd prime characteristic, and a nonprime extension field occur.

Proof limits: exhaustive testing of finitely many fields and quivers does not certify all finite fields. The general proof in `RESULT.md` uses the exact adjoint-matrix rank decomposition and additive-character orthogonality, and is the sole justification for arbitrary sizes and characteristics. It excludes multiple arrows and higher radical powers. An independent mathematical audit has not been performed.
