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

# Reproducibility

From this directory, run `python3 verify_kneser_triple_vc.py` with the standard library. Successful execution reports explicit witness traces for samples of cardinalities one through six and validates the complete profile enumerations for five, six and seven edges. In particular the seven-edge search checks exactly 9177 profiles, at most 124 of 128 possible traces per profile, no profile admitting 128. An independent generating-function coefficient calculation verifies the 9177 count.

The completeness of the finite obstruction depends on the proved reduction: every shattered seven-triple family yields a loopless seven-edge multigraph, possibly with parallel edges, with a vertex cover of at most three points; ordering that cover yields the complete three-core-plus-periphery encoding checked by code. The script does not infer global impossibility from a bounded number of ground-set sizes.

Explicit sample triples are also checked directly by iterating every center triple of their finite ground sets. A separate hand proof gives the small-ground lower bounds and the sequence of thresholds.

Checks performed: direct execution with exit code zero and terminal success marker; source comparisons documented in REVIEW.md. Independent audit is not performed.
