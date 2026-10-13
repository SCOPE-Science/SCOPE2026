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

The symbolic proof uses only the crown neighborhoods. With current white-index sets \(I,J\subseteq[n]\), vertex \(a_r\) has exactly \(|J|-\mathbf 1_{\{r\in J\}}\) white neighbors and vertex \(b_r\) has exactly \(|I|-\mathbf 1_{\{r\in I\}}\). These formulas prove that a side with at least three white vertices cannot be reduced and give explicit forces when a side has at most two white vertices.

`verify.py` independently constructs each crown graph for \(3\le n\le8\), tries every initial subset, simulates the skew rule to closure, and compares the result with the symbolic criterion. It separately simulates ordinary zero forcing to check that the only skew-but-not-ordinary states are \(I=J\) with two omitted indices. It also forms the expected square polynomial coefficient dictionary and compares every coefficient.

Expected deterministic output:

`VERIFY_OK n_range=3..8 subset_checks=87360 skew_sets=3120 ordinary_comparison_checks=87360 coefficient_checks=30 max_order=16`

The finite range reaches graphs of order sixteen and exhausts \(87{,}360\) initial subsets across the tested family. This is a regression check, not an exhaustive proof for arbitrary \(n\). No matrix-rank computation or external certificate is required by the symbolic theorem.
