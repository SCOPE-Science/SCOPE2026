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

Run `python3 artifacts/verify.py` from a directory containing the embedded artifact. The verifier uses only the Python standard library and rebuilds block components and all test graphs locally.

It independently enumerates \(2^{|V|}\) vertex subsets and tests every omitted vertex's adjacency count to verify the univariate three-state recurrence. This covers every labeled block graph on at most six vertices and 700 reproducible randomly glued clique-block graphs. It separately evaluates the multivariate circuit at vertex-dependent positive integer weights on 562 test graphs and compares with direct weighted subset sums. Finally, it checks the \(K_1\vee tK_m\) closed form for \(1\le t\le10\), \(2\le m\le6\).

Actual replay output:

`ALL CHECKS PASSED; small_labeled_block_graphs=8368; random_glued_block_graphs=700; vertex_subsets_checked=3536955; weighted_specializations_checked=562; generalized_windmill_profiles=60; all_labeled_graphs_n<=6`

The arbitrary-order result is a mathematical induction on the clique-block incidence forest, not an extrapolation from these finite tests. The runtime counts refer to arithmetic operations; the output coefficients can have substantial bit length. No external audit is claimed.
