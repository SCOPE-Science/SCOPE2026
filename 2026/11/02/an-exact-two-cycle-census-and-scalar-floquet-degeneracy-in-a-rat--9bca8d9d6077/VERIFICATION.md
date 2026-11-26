---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The conjugacy (u,v)=(cx,y) is invertible for either sign of the nonzero c. Closure in the second coordinate of a two-step orbit forces u_1=-u_0; if u_0=0 it is a fixed point. Otherwise each scalar first-coordinate factor must be -1. The two v coordinates have equal square -a/2-1 but differ, so they are opposite and nonzero. This gives a single geometric orbit for a<-2 and none at or above -2, including the collision at a=-2. At its two points the one-step Jacobian is the same matrix with diagonal -1,1 and off-diagonal entries -8t^2/(1+t^2),1. Squaring yields the claimed scalar lambda=-7-16/a, independently of c. Its modulus is below one exactly on (-8/3,-2); the smooth return contracts there and is locally expanding with nonsingular derivative for a<-8/3. At -8/3 the double multiplier is -1 and no nonlinear stability is inferred. For the zero multiplier at a=-16/7, expand the first component u g(v)g(v+u) at (-2t,t), with t=1/sqrt(7), g(±t)=-1, g'(t)=sqrt(7)/2 and g''(±t)=7/4. The quadratic terms for increments (h,k) are sqrt(7)(3h^2/4+hk+k^2), giving exactly the stated nonzero Hessian. Odd symmetry transfers the degeneracy to the other point. The exact algebra verifies the all-real statement independently of the sampled parameters in the supplied verifier.

## originality

PASS

The zero-drive model and numerical appearances of period two are already known. No inspected same-model source supplies the whole-plane exact census, scalar return identity, exact local stability interval, or exact quadratic degeneracy. The closest indexed classification analogues act on different maps; the later same-family escape result uses a disjoint parameter regime and restricted initial states.

## value

PASS

The zero-drive slice is the same fixed-line regime previously studied by numerical bifurcation diagrams. The complete low-period census and exact endpoints turn those observations into a global count and a local stability classification. The scalar return is more informative than coincident numerical eigenvalues: it vanishes at a definite parameter and gives genuine quadratic attraction. The simple algebra addresses a motivated question about this published model rather than an arbitrary isolated slice or parameter sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
