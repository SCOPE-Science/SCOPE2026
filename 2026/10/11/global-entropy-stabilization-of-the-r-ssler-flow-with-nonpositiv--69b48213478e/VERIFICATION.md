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

# Verification record

The attached `check_identity.py` is a standalone Python/SymPy source file. Running `python check_identity.py` verifies the equilibrium substitution, translated vector field and exact entropy derivative, symbolically reducing the residual to \((ap^2-cp+b)(z-p)/z\). It also tests the unique positive root and \(ap-c<0\) at four illustrative rational parameter triples. These samples are diagnostic only; they do not establish the universal theorem.

The analytical proof verifies every parameter in \(a\le0\), \(b,c>0\) by monotonicity of the equilibrium polynomial, the positive scalar integrating factor for height, compact logarithmic-entropy sublevel sets, and LaSalle's invariance principle. Crucially, at \(a=0\) the derivative vanishes on all \(z=p\), but only \(E\) can remain on that surface; this extra invariance step is required. Integration of \(\dot V\) gives the stated identity after convergence. The compact fully invariant and compact stationary-measure assertions follow from maximality and invariance of the dissipation identity, respectively.

Boundary conditions: the exact initial-value dissipation formula requires \(z(0)>0\), while initial \(z(0)=0\) enters \(z>0\) immediately and then converges. Nothing is claimed for negative initial height, \(a>0\), \(b\le0\), or \(c\le0\). No external independent audit has been conducted.
