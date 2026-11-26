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

The original Gaussian method's Eq. (12) and Eq. (15) use the stated exponential stage and signed squared shape parameter; a negative value is allowed. The smooth affine-in-state IVP has exact solution g and state Lipschitz constant 1. For h=1/N and t=ceil(N tau)/N, irrationality gives 0<delta=t-tau<h, and t+h<tau+2h<1 for N>=4. At the exact datum the numerator f_t+f_v f equals g'', with g''/g=4/delta^6-6/delta^4. The logarithm of the amplified g is (h^2/delta^6)(8/9-4 delta^2/3-delta^4/h^2). The parentheses exceed 1/2 when h<=1/4 (lower bound 107/144), uniformly for every mesh offset, so the logarithm is at least 1/(2h^4). The amplified term enters the update with positive coefficient 3h/4; the rest of the defect depends only on bounded g and g' at points in [0,1], so an N-independent K exists. This establishes a nonuniform local defect at a moving exact-data node, not failure of pointwise consistency at a fixed nonzero datum, propagated global divergence, or a contradiction of the original bounded-shape convergence theorem. The frozen checker was read, not run; its finite log-domain diagnostics are not used in the bound.

## originality

PASS

The method, quotient, and bounded-shape convergence condition are prior work; the contribution is the quantitative positive divergent exact-start defect on every fine uniform mesh for one smooth globally state-Lipschitz problem with no zero denominator at the tested nodes. Available sources do not establish that result; the older adaptive RBF singularity literature was not fully accessible, so priority is qualified.

## value

PASS

This is a motivated sharp failure mode for a specific published numerical integrator. It shows why even unusually benign smooth, state-Lipschitz solution data cannot replace uniform shape control: the exact-start defect can grow without a mesh node ever hitting the zero. The grid-uniform positive lower bound makes the phenomenon stronger and more actionable than warning of an undefined formula at a zero.

The dated certificate retains the supplied scientific assessment, sources and limitations.
