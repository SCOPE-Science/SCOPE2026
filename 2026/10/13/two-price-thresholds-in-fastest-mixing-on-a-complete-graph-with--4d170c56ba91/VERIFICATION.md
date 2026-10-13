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

# Analytical and executable verification

The proof in RESULT.md derives all eigenvalues of the invariant weighted Laplacian, reduces the global optimum to an invariant one using group averaging, and minimizes an explicit convex piecewise-linear cost. The two positive derivative breakpoints and the explicit transition equality intervals establish the theorem for all integral \(s,r\ge2\) and all real \(t>0\). For the example \(s=4,r=2,t=7/3\), the edge rates \(a=1/30,b=1/15,c=0\) spend precisely the unit budget and give gap \(4/15\).

Run `python3 verify.py` with Python 3 standard library. It computes exact Fraction-valued weighted graph Laplacians for all sizes from 2 to 10 in each vertex class and a set of prices including each threshold, and checks all reported orthogonal eigenvector equations, required rate-budget identities and minimum-cost breakpoint inequalities. Its successful reference output is `VERIFY_OK 955 exact rational two-block Laplacian eigenvector, budget and global breakpoint tests`.

This finite checker validates specified examples and identities but is not an exhaustive or infinite-domain proof. In particular it does not establish historical priority, non-invariant-optimizer uniqueness, or robustness under other optimization objectives. No independent audit has been conducted.
