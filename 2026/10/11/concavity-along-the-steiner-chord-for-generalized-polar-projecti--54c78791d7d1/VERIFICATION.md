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

Let
\[
A_\nu(t)=\nu\!\left(\Pi^\circ_{Q,p}(K_u(t))\right).
\]
The lead proof represents this as the marginal over \(z\in\mathbb R^{nm}\) of a density supported on a convex set \(\mathcal C\subset[-1,1]\times\mathbb R^{nm}\). The convexity of \(\mathcal C\) comes from the source's joint convexity of the relevant \(L_p\) mixed-volume gauge.

If the ambient density is \(\gamma\)-concave on its convex support, then its restriction to the convex joint support remains \(\gamma\)-concave there. Applying the Borell--Brascamp--Lieb marginal theorem over \(d=nm\) variables gives the exponent
\[
s_\gamma=\frac{\gamma}{1+d\gamma}
=\frac{\gamma}{1+nm\gamma}.
\]
The admissible threshold is exactly \(\gamma\ge-1/d\). At \(\gamma=-1/d\) the output exponent is the quasi-concave endpoint \(-\infty\); at \(\gamma=0\) it is logarithmic; and as \(\gamma\to\infty\) it tends to \(1/d\).

The source's reflection calculation gives \(A_\nu(-t)=A_\nu(t)\). If \(0\le s\le t\) and \(t>0\), then
\[
s=(1-\lambda)(-t)+\lambda t,
\qquad
\lambda=\frac{1+s/t}{2}.
\]
Therefore power concavity and evenness imply
\[
A_\nu(s)
\ge
M_{s_\gamma}(A_\nu(-t),A_\nu(t);\lambda)
=A_\nu(t).
\]

For Lebesgue measure and for Lebesgue measure restricted to \(R B_2^{nm}\), the density is constant on a convex support. These are the \(\gamma=\infty\) cases, so the corresponding \(1/(nm)\)-th roots are concave in \(t\).

The proof is analytic and universal; no finite enumeration or numerical certificate is used. The verification does not establish strictness or classify equality cases, and those statements are not part of the claim.
