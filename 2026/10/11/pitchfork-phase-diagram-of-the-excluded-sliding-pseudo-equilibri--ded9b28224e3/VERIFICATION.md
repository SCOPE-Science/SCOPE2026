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

Start from the exact strict-sliding equations
\[
\dot s=-(1-H)-2\mu\frac{d^2}{s}+\frac{\kappa}{2s}(s^2-d^2),\qquad
\dot d=d\left(\frac{1+H}{s}-2\mu\right).
\]
For \(\kappa\le0\), every term after \(-(1-H)\) in the first equation is nonpositive on \(s>0\), \(|d|<s\), so a zero is impossible.

For \(\kappa>0\), \(d=0\) gives exactly \(s=2(1-H)/\kappa\). If \(d\ne0\), the second equation gives \(s=(1+H)/(2\mu)\). Substitution gives
\[
\frac{d^2}{s^2}=\frac{\kappa-\kappa_c}{\kappa+4\mu},\qquad
\kappa_c=\frac{4\mu(1-H)}{1+H}.
\]
This ratio is positive exactly for \(\kappa>\kappa_c\), and then is strictly below one, so exactly two strict-sliding solutions occur.

The exact Jacobian is
\[
J=\begin{pmatrix}
\kappa/2+(2\mu+\kappa/2)d^2/s^2&-(4\mu+\kappa)d/s\\
-(1+H)d/s^2&(1+H)/s-2\mu
\end{pmatrix}.
\]
At the central branch its eigenvalues are \(\kappa/2\) and \((1+H)(\kappa-\kappa_c)/(2(1-H))\). At either off-axis branch the determinant is strictly negative. This proves all stated local types.

At threshold, translating by the exact central branch and writing \(a=1-H\), \(b=1+H\), the center manifold begins with
\[
u=\frac{4\mu}{ab}d^2+O(d^4).
\]
The reduced equation is
\[
\dot d=\frac{b}{2a}(\kappa-\kappa_c)d-\frac{16\mu^3}{ab^2}d^3+O((\kappa-\kappa_c)^2|d|+|\kappa-\kappa_c|d^3+d^5).
\]
The unfolding and cubic coefficients are nonzero with opposite signs. The exact off-axis formula independently confirms the supercritical square-root branch. No numerical approximation or finite enumeration is used.
