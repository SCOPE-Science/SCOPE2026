---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For Saiki–Takahasi–Yorke two-dimensional twisted baker on centered square with normalized uniform probability, each inverse branch Jacobian is 2; the Perron operator is P f(u,v)=[f((u−1)/2,v)+f((v+1)/2,−u)]/2. Direct expansion gives Pq=(5/8)q−u/4+v/4 for q=u²+v²−2/3 and exact eigenfunction e=q−10u/11+2v/11 with eigenvalue 5/8. Orthogonality to centered affine coordinates and E[q²]=8/45 give all k≥0 covariances 8(5/8)^k/45. Geometric summation proves variance 104n/135−128(1−(5/8)^n)/81 for all n≥1. Polynomial transfer characteristic polynomial is λ²(λ−1)(λ−5/8)(λ²−3λ/4+1/4), so centered degree≤2 decay is sharply 5/8, affine eigenspace modulus 1/2. The bounded polynomial h=5q/3−4u/3+2v/3 solves (I−P)h=Pq; d=q+h−h∘F has Pd=0 and ∫d²=104/135; using the original Bernoulli ergodicity theorem and standard reverse-martingale CLT, coboundary correction O(1) gives N(0,104/135). Independently recomputed exact SymPy transfer, characteristic, branch martingale and integrals.

## originality

PASS

PASS qualified to quadratic-energy exact stationary correlations/variance/CLT and degree-two versus affine spectral gap; original twisted map, Bernoulli coding, linear correlation and periodic Jacobian real-spectrum are acknowledged previous mathematics.

## value

PASS

The squared distance from the center of an invariant square is a natural geometric energy observable. Exact all-lag memory and Birkhoff-sum variance together with a sharp contrast between affine and quadratic observables give a meaningful quantitative invariant for the twisted map, not merely an application of the generic CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
