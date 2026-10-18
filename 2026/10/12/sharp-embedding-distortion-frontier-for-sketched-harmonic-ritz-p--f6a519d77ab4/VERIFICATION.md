---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For Hermitian positive definite A with spectrum in [mu,L], C=A^(-1) has spectrum [1/L,1/mu]. The elementary operator inequality (C-aI)(bI-C)>=0 implies for every nonzero x, Re<x,Cx>/(||x||||Cx||)>=2sqrt(ab)/(a+b)=2sqrt(kappa)/(kappa+1), with equality at an endpoint-eigenspace mixture. The (1±epsilon) subspace embedding on span(B,AB) bounds inner-product error by epsilon||u||||v||, so the Hermitian part of G=(SAB)^*(SB) is strictly positive for epsilon<c_kappa and F=(SAB)^*(SAB)>0. An eigenpair Fy=theta Gy has theta=(positive real)/(right-half-plane denominator), giving Re(theta)>0; invertibility of G follows from strict accretivity. The explicit A=diag(1,q^-2), x=(q,1)/sqrt(1+q²), B=A^-1 x, S* S=I-epsilon J (q=sqrt(kappa), 0<=epsilon<1) is an exact embedding on the plane and gives G=q(c_kappa-epsilon), F=1-epsilon*c_kappa; equality is singular, above it one negative Ritz value. Independently reconstructed rational Gram products for q=2,3,7,13, including kappa=9,epsilon=2/3 giving -3. This establishes sharpness for kappa>1; kappa=1 has threshold epsilon=1, the excluded embedding endpoint. Sketching probabilities and nonnormal A are outside scope.

## originality

PASS

Best-of-knowledge new statement/implication after source-specific primary comparison and targeted published-record searches; residual priority and access risks are itemized below.

## value

PASS

The exact condition-number-dependent positivity threshold for the sketched harmonic pencil improves the known general positive-real-matrix sufficient SPD specialization epsilon<1/kappa by an asymptotic factor 2sqrt(kappa), and supplies matching singular and negative-eigenvalue sketches. It resolves a natural failure boundary for harmonic Ritz values, not an arbitrary narrow sample computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
