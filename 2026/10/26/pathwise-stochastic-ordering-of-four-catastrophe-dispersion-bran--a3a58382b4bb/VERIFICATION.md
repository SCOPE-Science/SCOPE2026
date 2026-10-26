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

Run `python3 dispersion_order_verification.py` with the Python 3 standard library; expected output: `PASS 13989 exact rational assertions`. The program evaluates independent multinomial occupancy against uniform weak compositions, general nonuniform multinomial profiles with zero coordinates, the exact two-occupied-site gap, and the capacity-two binary-branching fixed-point example. Every comparison is performed using `fractions.Fraction`.

The code tests finitely many capacities, survivor counts, and probability vectors and does **not** prove the unbounded assertions. The analytic proof in RESULT.md uses pairwise balancing, a Dirichlet mixture, and quantile coupling for the universal conclusions. Prior sources establish low-capacity special cases; broader unindexed majorization coverage is possible.

Self-review: passed. Independent audit: not yet performed.
