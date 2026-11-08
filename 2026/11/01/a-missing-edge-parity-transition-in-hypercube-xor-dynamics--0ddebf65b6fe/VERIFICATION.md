---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For d>=2, A=sum S_i over commuting cube-coordinate involutions gives A^2=(d mod 2)I, and the half-cube block form gives rank(A) or rank(A+I)=m. With removed edge u-v, B=A+uv^T+vu^T; the invariant W=span{u,v,Au,Av} has dimension four and explicit local action Bu=v+Au, Bv=u+Av, B(Au)=(1+delta)u, B(Av)=(1+delta)v. For even d W is an invertible four-dimensional C((X^2+X+1)^2), complement is m-2 J2(0). For odd d the kernel span{Au,Av} is two-dimensional and semisimple; on Im B, ranks (B+I)^2=2, (B+I)^3=1, (B+I)^4=0 force J4(1) plus m-3 J2(1). Fitting decomposition supplies exact periods, fixed-space dimensions, cycle and transient counts for every characteristic-two extension. Independent GF2 bit-matrix checks d=2..7 verified ranks and fixed-space dimensions. Finite checks are corroboration, not infinite proof.

## originality

PASS

Best-of-knowledge comparison of final mathematical statement and implications; background results and exact prior coverage distinguished from the stated contribution. The already established abstract even similarity is NOT claimed new. The defective *graph edge* dynamical model, odd nilpotent partition, and consequent exact fault-specific entry-time profile are not prior corollaries of the distinct diagonal-feedback model.

## value

PASS

Single-edge fault tolerance is a natural graph-dynamical perturbation question. The parity split reverses the unmodified cube behavior, creating 3/6 cycles in even dimension and a semisimple zero component with sharp one-step transient in odd dimension. The complete arbitrary-d and arbitrary-characteristic-two-field Jordan/time/orbit census is a nontrivial structural classification, distinct from textbook A² identity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
