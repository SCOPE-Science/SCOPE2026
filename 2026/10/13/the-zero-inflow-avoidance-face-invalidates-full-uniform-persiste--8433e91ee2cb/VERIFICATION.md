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

The proof has two independent algebraic checks.

First, at \(p=v=0\), the avoidance equation is exactly \(A'=-q(t)A\) with \(q(t)\ge\mu>0\). Integration yields \(A(t)\le A(0)e^{-\mu t}\), so an interior trajectory approaches the boundary face \(A=0\).

Second, on that invariant face and for \(R_0>1\), direct substitution of
\[
S^*=R_0^{-1},\qquad A^*=0,\qquad I^*=\frac{\mu(1-R_0^{-1})}{\mu+\phi},\qquad P^*=\frac{\theta}{\lambda}I^*
\]
annuls every right-hand side. `verify.py` performs this check symbolically and also verifies the exact witness \(\mu=\gamma=\theta=\lambda=1\), \(\phi=w=p=v=0\), \(\beta=4\), for which \(R_0=2\) and the boundary endemic equilibrium is \((1/2,0,1/2,1/2)\).

The calculation does not test or assert disease-only uniform persistence, and it does not establish a complete repaired theorem under \(p+v>0\).
