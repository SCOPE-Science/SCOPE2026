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

# Computational verification and mathematical limits

Run `python3 verify.py` with the Python 3 standard library. The script constructs reduced Farey fractions as exact rational numbers. It confirms the stated exact counts of the three central intervals for \(6\le m\le25\) (220 interval cells), independently searches for every attaining badly ordered pair at 32 orders from \(120\) through \(200\), and evaluates the positive margin of the explicit published error inequality at the lower endpoint \(n=5{,}504{,}798\) using high-precision decimal arithmetic.

Observed output:

`VERIFY_OK exact_interval_cells=220 brute_order_cells=32 analytic_bound_margin=0.01549569 rational_arithmetic=PASS finite_samples_only=YES`

The brute-force tests are finite; they cannot exclude an exceptional larger order. The infinite exclusion of all off-center cases relies on Wang–Xie–Zhao's published uniform analytic estimate, which is quoted with its exact effective cutoff in `RESULT.md`. The symbolic strict-inequality witnesses in that file handle all near-center cases. The external analytic lemma has not received independent validation in this package.
