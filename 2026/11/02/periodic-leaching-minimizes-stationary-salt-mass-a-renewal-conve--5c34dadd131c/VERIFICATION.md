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

The mathematical proof in `RESULT.md` is the basis of the result. The included `CHECK.py` uses Python 3, its standard library, and SymPy (external dependency) to check independent regenerative-reward algebra, a symbolic formula and derivative for positive uptake, a finite collection of exact rational interarrival laws, and seeded simulations of stationary time-integral rewards. Run `python CHECK.py` in a directory containing the extracted files, with SymPy installed. A random simulation is not a universal infinite proof; its sole role is to test formula consistency.

The proof specifies all quantifiers: \(a>0\), \(0<r<1\), \(\mu\in(0,\infty)\), \(b\ge0\), and strictly positive iid interevent times with mean \(\mu\), sampled in stationary renewal equilibrium. Strictness for the mean follows from strict convexity or interarrival variance. Higher risk-function expectations may be infinite; the stated inequality is interpreted in the extended sense, with a finite right baseline. The full increasing-convex order is **not** asserted for positive uptake. All fixed-threshold exceedance comparisons are expressly unproved and generally false.

The proof is mathematical and exact within its assumptions. Independent scientific audit, formal verification, and field-data validation have not been performed. The source-priority comparison remains non-exhaustive.
