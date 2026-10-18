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

# Verification details

The proof reduces the boundary covering-radius minimax to two squared Euclidean distances from a point on one rhombus side to its two opposite vertices, with the other two distances pointwise dominated. Their unique crossing is in the side for \(1\le r\le3\), and outside it for \(r>3\). The squared-radius formula, center coordinates, and all equality cases are reconstructed directly from that crossing and the endpoint. Differentiation yields the two global sharp shape inequalities. No step uses an inference from a finite grid to a continuum.

Execute `python3 checker.py` from this directory to reproduce exact rational comparisons. A completed run checked 10 distinct diagonal-squared ratios and 10,410 rational edge parameters against distances to all four vertices; every comparison passed. The checker also tests the crossing identity and representative phase endpoints. It does **not** check all real ratios or replace the all-parameter proof.

Scientific limits: Euclidean metric, strictly positive half-diagonals, boundary-constrained centers, rhombi only. The published square endpoint is cited as prior work. Bibliographic searching was not exhaustive, and Walter's older full text was not inspected. There is no independent scientific audit or external certification.
