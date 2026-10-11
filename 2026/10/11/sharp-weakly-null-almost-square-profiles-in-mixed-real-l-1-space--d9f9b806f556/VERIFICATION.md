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
# Verification of the exact weak-null profile

The lower bound is derived from the exact scalar identity \((|u+v|+|u-v|)/2=\max(|u|,|v|)\), contractive atomic projection, and Schur's property of \(\ell_1\). The existence proof bisects the diffuse finite measure to make independent Rademacher signs; orthonormality and \(L^2\)-approximation prove \(\int f r_n\to0\) for every \(f\in L^1\), which in turn proves weak nullity of \(g r_n\) for every \(g\in L^1\). The scaling \(y_n=(t/b)x_{\mathrm{dif}}r_n\) handles \(b>0\); a disjoint diffuse unit function handles \(b=0\). Each signed norm converges to the exact lower envelope. The tolerance and distance consequences follow by direct inequalities.

Run the embedded `verify.py` with Python 3 to independently replay finite exact-rational algebraic sanity checks. These computations check formulas on finite rational inputs only; they do not prove weak convergence or the all-measure assertion, which are settled analytically above.
