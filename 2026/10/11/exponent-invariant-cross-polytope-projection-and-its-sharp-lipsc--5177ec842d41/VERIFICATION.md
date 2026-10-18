---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Strict convexity and coordinatewise KKT yield a unique threshold soft-shrinkage minimizer with residual tau independent of p for all real 1<p<infinity, r>0; inside the l1-ball it is identity. On each exterior sign/active-set cell, differentiation gives a sign-conjugate of C_k=I-11^T/k. Continuity and finite polyhedral cell decomposition bound the global Lipschitz quotient by max(1,||C_k||_p), while open full-dimensional cells realize every active k and any maximizing direction. C2 is contractive in every p, Ck orthogonal when p=2. The zero-mean vector (1,1,-2) and perturbation by constants gives strict amplification when p!=2 and n>=3. In k=3,p=4 the zero-sum quartic identity reduces maximizing ||C3 x||_4 to a quadratic constrained by sum x_i^4; Lagrange cubic gives only two-equal-coordinate extremizers above 1, then sharp weighted Hölder gives L^4=(1+2^(1/3))^3/9, numerically 1.0641658628581188. Duality covers p=4/3.

## originality

PASS

Euclidean Duchi et al. gives p=2 thresholding only; it does not imply exponent independence or non-Hilbertian sharp Lipschitz profiles. The later SCOPE weighted cross-polytope theorem gives a general active-subset norm formula including all equal weights, but its first Git import 13:11:30Z was AFTER this unweighted record at 13:11:22Z. This record is first among the inspected SCOPE versions and additionally evaluates the first expansive fourth-power constant in radicals, not stated in the weighted theorem. Priority outside inspected sources remains unverified.

## value

PASS

This gives a sharp exact stability invariant for a fundamental projection used in approximation and optimization, including a clean first dimension/exponent where Hilbert nonexpansivity fails. The p=4 three-dimensional radical is a motivated nontrivial evaluation of an induced centering norm rather than an arbitrary tiny computation; all-n formula also isolates the exact mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
