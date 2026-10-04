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

The proof is analytic and covers the entire integer lattice.

The accompanying `verify_lattice_cantelli.py` script uses exact rational
arithmetic. Across a grid of rational variances and positive integer
thresholds, it checks that:

1. \(j=\lfloor v/k\rfloor\) gives nonnegative extremal masses;
2. those masses sum to one and match mean \(0\) and variance \(v\);
3. the tail mass equals the asserted sharp bound;
4. the exact difference from classical Cantelli equals
   \[
   \frac{r(k-r)}
   {(k+j)(k+j+1)(v+k^2)};
   \]
5. the quadratic certificate dominates the tail indicator at every tested
   lattice point.

Finite replay does not establish the infinite-lattice statement. That step is
proved directly because a product of consecutive integers is nonnegative, and
the certificate is monotone once \(x\ge k\).

Originality was assessed by statement-level comparison with general
moment-bound literature and the closest accessible Cantelli-type results.
Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK cases=29040 lattice_checks=4094640`.
