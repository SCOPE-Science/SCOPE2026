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

# Verification scope

The proof's nonstandard step is an explicit boundary-layer change of variables. It uses \(y_1=R^{1-1/p}u\), \(y_2-y_1=h\), and two inward horizontal distances. Its Jacobian is exactly \(R^{1-1/p}\), while the two local normal deficits converge to \((a+b)|u|^p\). Strict convexity and uniqueness of the support points provide a global positive lower bound by a multiple of \(|u|^p\), yielding the integrable majorant
\[e^{-h^2-(c|u|^p+s+t)^2}.\]
This justifies dominated convergence for all real \(p>1\) and local uniformity in nonnegative gaps. The exact constant follows from integration of the two inward distances and the tangential coordinate. The Gaussian Fock normalization includes one factor \(\pi^{-1}\) for each spatial integral.

Run `python3 contact_checker.py` with a Python standard-library environment. It performed 55 numerical assertions involving the exact finite-size normal integral, zero-gap gamma values, positivity, gap monotonicity, and increasing-scale convergence for superellipses at orders \(p=2,4,6\). The largest normalized radii used were \(R=320\); the largest relative error among the largest-scale tests was less than one percent. These are quadrature checks, not validated error bounds on the infinite-dimensional theorem. There is no external certification or independent proof.
