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

# Verification record

The proof in `RESULT.md` is self-contained. Critical steps are the strict facet-separation upper bound, the projected-width/slack translate construction, continuity from below of Borel measure, and the independent-coordinate construction for parallelotopes. No numerical observation is used to infer a universal theorem.

To reproduce the supplemental exact checks, run:

```sh
python verify_polyhedral_depth.py
```

The program uses only Python's standard library. It constructs rational irredundant facet systems, exact facet-interior points, and rational atomic measures for two- and three-dimensional polytopes, including queries through atoms. It checks each explicit facet-anchored translate and the box-threshold strict inequalities. Its successful run reported `ALL PASSED: 32823 exact rational checks`.

Limits: the checker covers finitely many rational examples and cannot certify arbitrary convex polytopes or measures. The general theorem is established by the analytic proof. The general cutoff is sufficient rather than universally optimal; the half-width cutoff is distribution-uniformly sharp only within the stated parallelotope class. An independent mathematical audit has not been performed.
