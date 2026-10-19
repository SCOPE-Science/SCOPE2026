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

# Reproducible checks

Run `python3 verify_unrooted_pd.py` with Python 3 standard library. The script enumerates every independent-survival pattern of two small weighted unrooted phylogenetic trees. It separately computes expected diversity from direct survivor sets and from edge-event probabilities, tests two-taxon mixed finite differences against the closed-form cut identity, and checks that guaranteeing an anchor makes subsequent pair interactions nonpositive.

On the included script the exact run completed with:

`VERIFY_OK edge_probabilities=120 pair_hessians=39 anchored_margins=369 homogeneous_three_leaf_threshold=1/3 heterogeneous_normalized_increase=PASS`

The proof in `RESULT.md` establishes the exact edge contribution at each split and strict monotonicity of the normalized interaction over the entire parameter interval. Finite rational tests are consistency checks, **not** exhaustive tests of every phylogenetic tree or extinction-risk function. The code does not attempt any external certification or empirical validation. The comparison literature leaves a residual risk of an overlooked equivalent pairwise formulation.
