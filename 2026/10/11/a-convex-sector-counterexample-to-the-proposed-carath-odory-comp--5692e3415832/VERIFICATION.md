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
# Exact verification

`verify_counterexample.py` (Python 3 standard library only) reconstructs the rational-complex witness, both derivative expressions and the component formula. The program evaluates all Gaussian-rational divisions exactly, checks the branch selection through \((1+z)/(1-z)=T^2\) and \(\operatorname{Re}T>|\operatorname{Im}T|\), and proves
\[
|z_0|^2<1,\quad \operatorname{Re}P_f(z_0)>0,\quad
-\frac12<\operatorname{Re}h_{1/2}[f](z_0)<-\frac14.
\]
The program also cross-checks the formulas for \(A_f\), \(P_f\), and \(h_{1/2}\) using two algebraically distinct substitutions. The real part is an exact negative fraction reported in `RESULT.md`; its sign needs no rounding. Normalization and convexity are analytic results supplied in the proof, not inferred from code. This verifies a **counterexample**, not a classification of the entire class, and does not assess any independent audit.
