---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n>=2 and 0<tau<=1, the cyclic shift P and anticyclic Q have unit 2-norm condition number; E=I+tau e0 e0^T has kappa2<=2. Both F1=Q-P and F2=E-I are nonzero rank one. The pair X=I,Y=-I solves PX+YQ=-F1 and X+YE=-F2. Homogeneous elimination gives PU-U(E^-1 Q)=0; sigma(P) on |z|=1 while sigma(E^-1Q) has radius (1+tau)^(-1/n)<1, proving uniqueness. Both solutions have n flat singular values 1. For K_k rank k, (K_k,-K_k), R1=e_k e_{k-1}^T -e0 e_{n-1}^T (norm sqrt 2), R2=0; normalized max residual sqrt2/(2sqrt k+2); Frobenius relative forward error sqrt((n-k)/n). Choosing n=m²,k=m yields small residual with near-unit forward error. Independently reconstructed exact shifts and residual norms at n=2,5,8 and k=1,n-1. Uniform spectral separation and well-conditioned coupled operator are NOT asserted.

## originality

PASS

Counterexample combines two nonzero rank-one forcings, disjoint but dimension-collapsing generalized spectra, bounded individual coefficient condition numbers and explicit low-rank trial pairs giving vanishing normalized residual despite poor forward error. Known Sylvester examples establish only general low-rank forcing failure; the new conjunction is distinguished, subject to uninspected latest primary source.

## value

PASS

Termwise normalized residual is a practical numerical diagnostic; this explicit adversarial near-resonant family demonstrates a sharp scope limitation that low-rank forcing or residual smallness cannot overcome. No algorithm-specific iteration claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
