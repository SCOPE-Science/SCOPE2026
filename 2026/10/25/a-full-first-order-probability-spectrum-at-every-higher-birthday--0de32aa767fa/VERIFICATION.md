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

Run `python verify.py` using the Python standard library. The checker exhaustively compares exact falling-factorial moment formulas with direct enumeration for every tuple `(n,m,j,r)` with `1<=n<=5`, `1<=m<=4`, `0<=j<=n`, and `r` in `{1,2}`; it also checks critical-scale finite-size first moments and rare larger-star tail sums for `k=2,3,4,5` and `c=0.75,1,2`. It prints `CRITICAL_STAR_OCCUPANCY_EXACT_OK 184 checks` on success.

The proof of the infinite Poisson convergence, the exhaustive first-order probability spectrum, and originality are not computationally certified by this finite test. The exact factorial moment formula and canonical structures for model checking are fully specified in `RESULT.md`. The named statuses correspond only to self-review; independent validation has not been performed.
