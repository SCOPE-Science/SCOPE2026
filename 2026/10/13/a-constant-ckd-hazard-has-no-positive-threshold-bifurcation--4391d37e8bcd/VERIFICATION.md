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

Reading actual AIMS Mathematics (2026) PDF section 3.2 and Appendix B4 confirms its printed CKD-only equations Sdot=Lambda-(lambda_k+mu)S; Ikdot=lambda_k S+gamma_h H-phi Ik; Hdot=zeta_k Ik-psi H, phi=zeta_k+mu_k+mu, psi=gamma_h+mu_h+mu. Set D=phi*psi-gamma_h*zeta_k=zeta_k(mu_h+mu)+(mu_k+mu)(gamma_h+mu_h+mu)>0 for all positive death/outflow rates. Then S*=Lambda/(lambda_k+mu), I*=lambda_k Lambda psi/[(lambda_k+mu)D]>0 and H*=zeta_k I*/psi>0 for EVERY positive lambda_k. The EXACT affine Jacobian has characteristic polynomial (r+lambda_k+mu)(r^2+(phi+psi)r+D), hence all eigenvalues have negative real parts for all lambda_k>=0 and the unique equilibrium attracts globally exponentially. I* increases continuously with lambda_k, with I*(0)=0; no positive-hazard exchange of equilibrium branches. Original Ck=1 corresponds to positive lambda*=mu D/[Lambda(psi+zeta_k)], not a zero eigenvalue; the printed Appendix B4 assertion of such an eigenvalue and transcritical bifurcation cannot hold. A separate symbolic differentiation and residual check reproduced the matrix and fixed point exactly.

## originality

PASS

Rao et al DOI:10.3934/math.2026707 already print the affine system and the correct positive equilibrium coordinates. Their Theorem 3.8 and Appendix B4 nevertheless claim a forward transcritical bifurcation at Ck=1 using a non-equilibrium reference state. The new claim is a motivated falsification and globally valid correction of that specific printed theorem, not ownership of the elementary linear-system technique or of the equilibrium formula already printed. Full section 3.2 and Appendix B were inspected at the published primary source. Other COVID-CKD models with prevalence coupling have different Jacobians; no other comparable correction was identified in Resultary prior-record searches.

## value

PASS

This is not a generic sign check: a published threshold and bifurcation result in a biomedical dynamical model is mathematically incompatible with the actual constant-hazard equations. Establishing an all-positive-hazard stable equilibrium and monotonicity gives the exact qualitative alternative and prevents treating a nonexistent positive-hazard disease-eradication threshold as a policy bifurcation. Scope explicitly excludes claims about the full nonlinear seven-compartment coupled model or real clinical outcomes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
