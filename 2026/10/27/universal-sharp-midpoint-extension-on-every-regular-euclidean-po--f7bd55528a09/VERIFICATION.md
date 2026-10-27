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

# Numerical and analytic verification

Run `python verify_polygon.py` with `requirements.txt` installed. The supplied checker uses an independent Euclidean point-distance construction and explicit linear programming to test all midpoint-separation orbits for orders \(3\) through \(30\). Successful completion reports `POLYGON_MIDPOINT_EXACT_FORMULA_NUMERIC_OK n_cases=28 midpoint_orbits=224`.

The checker verifies normalization and nonnegativity of the proposed weights; distance-potential reproduction; decreasing midpoint shells; a nonnegative cyclic-mixing measure; and optimal transport between each distinct midpoint-orbit pair. Its linear programs are finite-dimensional numerical checks, not proof of infinite-order positivity or optimality.

The unrestricted correctness argument is given in `RESULT.md`: a signed-coefficient lower-bound certificate, an exact cyclic chord-matrix inversion, strict Ptolemy positivity, a Pinney-type differential/convolution identity, a layer-cake monotonicity lemma, and an explicit coupling of two-point measures. All identities hold for arbitrary polygon order under the stated scope. No machine theorem prover or external independent validation is claimed.
