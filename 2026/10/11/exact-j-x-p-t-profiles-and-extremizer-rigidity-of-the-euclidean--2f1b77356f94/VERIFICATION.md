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

Let \(Q_1(z)=(1+\lambda)z_1^2+z_2^2\) and \(Q_2(z)=z_1^2+(1+\lambda)z_2^2\). The exact identities are
\[
N_\lambda(z)^2=\max\{Q_1(z),Q_2(z)\},\qquad
Q_1(z)+Q_2(z)=(\lambda+2)\|z\|_2^2.
\]
For \(N_\lambda(z)=1\), therefore \(\|z\|_2^2\le2/(\lambda+2)\), and equality holds if and only if \(|z_1|=|z_2|\). With \(u=x+ty\), \(v=x-ty\), equal-index quadratic branches obey
\[
Q_i(u)+Q_i(v)=2Q_i(x)+2t^2Q_i(y)\le2(1+t^2).
\]
The mixed branch obeys
\[
Q_1(u)+Q_2(v)=(\lambda+2)(\|x\|_2^2+t^2\|y\|_2^2)+2\lambda t(x_1y_1-x_2y_2)
\le2(1+t^2)+\frac{4\lambda t}{\lambda+2},
\]
with the analogous swapped-branch estimate. Thus
\[
\frac{N_\lambda(u)^2+N_\lambda(v)^2}{2}\le1+t^2+\frac{2\lambda t}{\lambda+2}.
\]
For \(1\le p\le2\), the \(p\)-power mean is at most the quadratic mean, giving the desired upper bound.

For the concrete unit vectors
\[
x_*=\frac{(1,1)}{\sqrt{\lambda+2}},\qquad
y_*=\frac{(1,-1)}{\sqrt{\lambda+2}},
\]
one has
\[
Q_1(x_*+ty_*)=Q_2(x_*-ty_*)=1+t^2+\frac{2\lambda t}{\lambda+2}.
\]
These are the active branches, since each exceeds its unused branch by \(4\lambda t/(\lambda+2)>0\); the two output norms are equal. Equality in the sharp mixed-branch bound forces \(x,y\) to be unit diagonal vectors and forces Euclidean equality between \(y\) and a reflected \(x\). This yields the stated orbit and no others.

The 2009 quadratic Hilbert-comparison upper bound, for the same \(p\)-range, exceeds the exact profile **after squaring** by
\[
\frac{2(\lambda+1)(1+t^2)}{\lambda+2}-\left(1+t^2+\frac{2\lambda t}{\lambda+2}\right)
=\frac{\lambda(t-1)^2}{\lambda+2}.
\]
This vanishes only at \(t=1\), matching the exact 2011 example. The derivative at the origin is \(\lambda/(\lambda+2)\), so the space is not uniformly smooth when \(\lambda>0\).

The algebra was independently checked by symbolic substitution of the diagonal witness into both quadratic forms and by exact simplification of the historical-bound gap. Finite randomized stress tests over multiple \(\lambda,t\) choices supported the candidate but are not used to prove any uniform bound or equality classification. All proof obligations are discharged by the displayed elementary identities and inequalities.
