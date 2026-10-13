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

The proof is analytical. A local exact-arithmetic check supplies finite corroboration, not a replacement for the convexity, Riemann-sum, or critical-window arguments. To replay, place `verification.py` alongside this file and run `python3 verification.py` in Python 3. The program has no dependencies outside the standard library.

The checker reconstructs the full \((n+1)\)-vertex weighted wheel Laplacian with rational edge conductances; forms \(L+\mathbf1\mathbf1^T/(n+1)\); inverts it by exact Gauss–Jordan elimination; and compares the resulting Kirchhoff index with a second expression involving the \(n\)-cycle Laplacian. It separately checks the derivative at the hub-only star using an exact matrix-inverse derivative identity, the boundary derivative formula, and the first two cycle Laplacian moments. The run produced: `VERIFY_OK 196 exact finite wheel/index/derivative instances; cycle traces and thresholds; general proof is analytic`.

This covers \(3\le n\le9\), prices \(1/4,1,3/2,2,9/4,3,5\), and three rational feasible allocations at each price. The proof's quantifiers range over all \(n\ge3\), all real \(t>0\), all admissible real conductance vectors, and all fixed real critical-window shifts. Nothing about an infinite system is inferred from a finite test.

The original optimization paper provides an unpriced symmetric wheel spectral reduction (DOI: 10.1137/050645452); the present proof independently applies the Laplacian eigenmode calculation to the priced budget and derives the threshold and asymptotic formulas. Historical weighted-wheel sources remain a bibliographic originality risk; no independent validation was performed.
