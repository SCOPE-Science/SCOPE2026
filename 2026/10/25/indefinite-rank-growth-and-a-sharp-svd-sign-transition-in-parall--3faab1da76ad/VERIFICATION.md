---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

From the actual parallel augmented source update under transpose-equivariance and matched bases, H=[B,C^T;C,0]; B positive definite and C full row rank s give inertia (r positive,s negative) by Schur-complement congruence. For the specified PSD-preserving gradient flow, exact reduced stages produce H=[[1,0,p],[0,1,0],[p,0,0]], eigenvalues 1+d,1,-d with d(d+1)=p^2; the SVD rank-two sign transition occurs precisely at p=sqrt(2), tie excluded. At gamma=2,h=3/2,tolerance=6/5,c=10, rank-two is chosen, the negative direction remains and neither of two source rejection tests fires. Independently checked symbolic characteristic polynomial and 12 sample parameters.

## originality

PASS

Ceruti/Kusch/Lubich introduce the underlying parallel algorithm and explicitly mention limitations. The structural inertia theorem and precise rank-two SVD sign switch under PSD-preserving dynamics are not stated in the inspected original algorithm or the distinct 2021 serial BUG algorithm; Schur-complement inertia itself is classical.

## value

PASS

Positive semidefiniteness is a motivated invariant in covariance/Lyapunov dynamics. A universally sharp structural obstruction for symmetric rank augmentation plus an exact nonrejected three-dimensional witness are informative numerical-method boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
