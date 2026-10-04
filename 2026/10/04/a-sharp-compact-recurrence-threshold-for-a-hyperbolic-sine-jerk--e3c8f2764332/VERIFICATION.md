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

The checked vector field is
\[
\dot x=y,\qquad \dot y=z,\qquad \dot z=-a x-b^2y-cz+d\sinh x.
\]
For
\[
P=xz-\frac12y^2+cxy+\frac12b^2x^2,
\]
`verify.py` differentiates symbolically and obtains
\[
\dot P=-a x^2+c y^2+d\,x\sinh x
       =c y^2+(d-a)x^2+d\,x(\sinh x-x).
\]
The script also checks cancellation of all \(xz\) and \(xy\) terms and verifies that an equilibrium satisfying \(d\sinh x=a x\) has zero vector-field residual.

The infinite-time conclusions are verified analytically rather than by simulation. For \(d>0\) and \(a\le d\), the power series
\[
x(\sinh x-x)=\sum_{n=1}^{\infty}\frac{x^{2n+2}}{(2n+1)!}
\]
is nonnegative and is zero only at \(x=0\). Therefore the displayed defect is nonnegative and has zero set \(x=y=0\). On a bounded trajectory, \(P\) is bounded and monotone, so its defect is integrable. The defect has bounded derivative on the compact trajectory range; Barbalat's lemma therefore forces it to zero. This yields \(x,y\to0\), and the derivative form of Barbalat's lemma gives \(z=\dot y\to0\) because \(\dot z\) is bounded.

For a bounded complete trajectory, the same integrability and uniform-continuity argument applies at both time ends. The monotone quantity \(P\) approaches zero at both ends, hence is constant and its defect vanishes identically. This proves complete-orbit rigidity and, consequently, compact-invariant-set rigidity.

For sharpness, \(r(x)=\sinh x/x\) is strictly increasing on \(x>0\) because
\[
x\cosh x-\sinh x>0
\]
there. Since \(r(0^+)=1\) and \(r(x)\to\infty\), \(a>d\) gives a unique positive equilibrium coordinate and its negative symmetric partner.

Limits: this verification does not establish boundedness of arbitrary solutions and does not classify the dynamics for \(a>d\) beyond the nonzero equilibria. The symbolic script is a check of exact algebra only; the analytic inequalities and infinite-time argument are part of the proof above, not inferred from computation.
