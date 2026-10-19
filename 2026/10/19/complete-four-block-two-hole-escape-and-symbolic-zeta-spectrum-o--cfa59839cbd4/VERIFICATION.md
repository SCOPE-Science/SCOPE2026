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

# Reproducibility and checks

Run `python3 certify_binary_pair_holes.py` with Python 3 (standard library only). The script constructs all \(\binom{16}{2}=120\) binary four-word hole pairs and the corresponding integer \(8\)-state adjacency matrices. It computes their characteristic polynomials through exact integer Faddeev–LeVerrier recurrence; exact rational polynomial gcd and Sturm sequences certify each Perron radius interval and strict separation. It also compares direct enumeration to matrix survival counts at \(n=0,\ldots,7\) for every pair, producing \(960\) independent finite-time integer comparisons.

The script checks the exact multiplicity vector, the number of distinct characteristic polynomials and spectral radii, and the complete pair lists attaining the extremal roots. All tests must terminate with no assertion errors and a `CERTIFIED` output. The code uses no numerical eigenvalue approximations and no external libraries. The infinite-time escape limit and symbolic zeta formula are consequences of nonnegative-matrix spectral theory and the trace-log determinant identity, not of extrapolation from finite trajectories.

Scientific limitations: the result is exactly a finite classification of two fixed length-four binary holes. Symbolic periodic orbit counts are not asserted to equal geometric interval counts where two binary boundary codings coincide. Independent validation has not been performed.
