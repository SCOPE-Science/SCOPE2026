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

The algebraic core was replayed from `verify.py`, which implements exact sparse-polynomial arithmetic over rational coefficients and verifies the five identities
\[
L_F(x^2/2)=ax^2-xyzuv,
\quad
L_F(y^2/2)=-by^2+xyzuv,
\]
\[
L_F(z^2/2)=-cz^2+xyzuv,
\quad
L_F(u^2/2)=-du^2+xyzuv,
\quad
L_F(v^2/2)=-ev^2+xyzuv.
\]

The remainder of the proof is analytic: invariance of a compactly supported probability measure makes each mean Lie derivative zero. No finite simulation is used as evidence for the infinite-time claim.

Verified scope: \(a,b,c,d>0\), \(e\in\mathbb R\), compactly supported invariant Borel probability measures. Not proved: global convergence of every trajectory, boundedness of every orbit, or a classification of all compact invariant sets.
