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
# Exact finite verification

To check, run `python3 phylo_sampling_verify.py` using Python 3 with no additional packages. It enumerates every nonplane rooted full binary tree shape with at most ten leaves, generates each complete bivariate rooted phylogenetic-diversity enumerator twice by independent methods (recursive child-edge counts and direct unions of root-to-tip edge sets for every subset), and checks equality coefficient by coefficient. It also checks binomial normalization for all sample sizes, the unique ambiguous pair at depth two for ten leaves, all nine collision counts for individual depths and the list of nine optimal two-depth designs.

Observed executable result: `VERIFY_OK shapes_through_10=192 direct_subsets=131726 pair_ambiguity_10=1 admissible_two_depth_designs=9`.

This is a finite exhaustive certificate, not random testing, but it does not prove claims for more than ten leaves. The theorem does not concern unequal branch lengths, multifurcating phylogenies, real observational data, or independent experimental validation.
