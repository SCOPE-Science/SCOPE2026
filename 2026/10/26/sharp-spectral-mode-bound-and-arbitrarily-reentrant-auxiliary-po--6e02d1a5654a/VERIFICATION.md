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

Eliminate x+ from the original implicit state update to get r+=B(h)/A(h), where A(h)=1+[h/(2Q^2)] ghat^T(I+hS)^-1 ghat>0 and 2Q B(h)=F(h)=2rQ-sum_{i=1}^m c_i h lambda_i/(1+h lambda_i). Multiplying by positive product prod(1+h lambda_i) yields degree <=m numerator with positive value at h=0; k positivity components require at least 2(k-1) positive root multiplicities, proving floor(m/2)+1 bound including tangencies. For arbitrary distinct roots t_j and distinct positive eigenvalues lambda_i, the proposed residue coefficients c_i make F(h) identically 2prod(1-h/t_j)/prod(1+h lambda_i) because poles and value at zero match. Set x=1,G=I,L=diag(lambda),r=Q=1,E_N(z)=1+c^T(z-1)+kappa||z-1||^2, kappa>||c||^2/4; this is everywhere strictly positive and strictly convex, with consistent auxiliary starting data. Independent exact sympy interpolation through m=6, and direct elimination for m=2 gave r+(h)=16(h-1)(h-2)/(609h^2+449h+32) with global minimum E_N=31/320>0.

## originality

PASS

Huang-Liu-Wang-Yan October 2026 establishes the exact original SAV-BE one-step sign criterion (2.10), sufficient positivity condition and one-mode counterexample. It does not classify the topology of all positive stepsizes or construct arbitrary prescribed alternating sign thresholds within positive convex energies. The new sharp mode-count bound and realization are algebraically nontrivial though they use the prior criterion; possible implicit rational-interpolation restatements remain a priority risk.

## value

PASS

Nonmonotone positivity in numerical gradient-flow schemes has direct mathematical and numerical significance: the positive stepsize set can fragment and then recover positivity. The sharp spectral-mode upper bound, minimum two-mode witness, and arbitrary-root interpolation within globally strictly convex positive energies demonstrate a structural pathology, not a trivial scalar sign check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
