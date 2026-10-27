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

Run `python verify_symbolic.py` (Python standard library) to check the exact identity between the Laplacian rank-one update and every displayed type potential. It proves signs of all 80 nonzero signed edge-class voltage differences by coefficientwise positivity/negativity after substituting \(t=m-2\), verifies exact orbit sums by cross multiplication, then certifies every strict maximizing-orbit and deletion-response inequality for the appropriate integer range. This is an all-parameter algebraic check, not a bounded numerical enumeration.

Run `python check_projection.py` to build the grounded Laplacian from scratch, invert it with exact fractions, construct every surviving edge column, and compare the resulting cut and cycle norms with the formulas for \(m=2,3,4,5,6\). The two graph versions contain 535 edge columns in total. These finite checks corroborate, but cannot replace, the proof for all \(m\ge2\).

The proof also explicitly handles the limiting baseline at \(m=2\), the exceptions at \(m=3\), and all integer \(m\ge4\). Neither script supplies independent human mathematical validation. No statements are made about nonorthogonal minimum projections or weighted/multiple-edge perturbations.
