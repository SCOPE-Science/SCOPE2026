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

The standalone `verify_subdivided_star.py` first constructs unweighted graph distances by breadth-first search. It uses rational arithmetic to compare the original double sum \(\sum_{v,w}\eta_v\eta_wd(v,w)^p\) to the claimed irreducible-sector decomposition for \(q=2,\ldots,8\), twelve nonsymmetric states for each \(q\), and integer powers \(p=1,2,3\). Numerical symmetric-matrix diagonalization independently checks the centered distance-power Gram inertia and endpoint rank for \(3\le q\le16\). A bisection root routine tests the analytic interval and sample large-\(q\) asymptotics.

The analytic proof, rather than finite tests, establishes universal monotonicity, unique threshold and strict sign claims. The numerical zero tests use a finite tolerance and are not exact proofs of a zero eigenvalue; the full quadratic-form identity and determinant factorization supply that proof. Computations use Python 3 with NumPy installed and no network access.

Independent scientific validation has not been performed.
