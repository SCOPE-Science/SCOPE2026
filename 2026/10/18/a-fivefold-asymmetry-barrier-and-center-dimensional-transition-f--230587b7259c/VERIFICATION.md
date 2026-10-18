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

Run `python verify_cut_symmetry.py` with a standard Python 3 interpreter. It uses only standard-library `fractions.Fraction` and `itertools` and prints exactly two `VERIFY_OK` lines when all assertions pass.

The finite checks exhaust the sixteen \(K_5\) cut vectors, sixteen pentagonal switchings, forty triangle switchings, exact left/right support extrema, all one hundred signed-normal Gram entries, and all thirty-two cut vectors of the strict six-vertex \(K_5\)-triangle two-clique-sum at two distinct feasible factor-five centers. The check independently confirms \(\sum q=80\) and full-rank Walsh orthogonality.

The proof for all finite \(K_{3,3}\)-minor-free graphs instead uses the published full facet classification, the exact reflected-containment criterion, and projection monotonicity. Finite enumeration by itself does not certify the graph-wide theorem. Independent mathematical validation is not part of these checks.
