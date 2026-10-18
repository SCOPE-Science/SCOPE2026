---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Reconstructed section-2 contact Theta=(sum k J_k)/(sum k N_k) and demographic N_k prime=Lambda-mu N_k, hence at DFE N_k=S_k=Lambda/mu. Differentiating normalized Theta gives DTheta=(mu/(Lambda L)) sum k DJ_k, so the boundary incidence beta k S_k DTheta cancels Lambda/mu. With survival pi(a)=exp(-integral (mu+gamma+r)), infection inflows form a rank-one renewal operator whose positive-real growth characteristic equation is 1=beta (Q/L) int exp(-lambda a)pi(a) da. Under positive constant rates the age-integrated six-dimensional system closes exactly: independent symbolic differentiation of the nonlinear 6-vector at DFE (2,2,0,0,0,0) gives infected block [[-5/6,1/3],[1/3,-1/3]], eigenvalues -1 and -1/6, and all four other eigenvalues -1/2. Exact rational threshold Rcontact=5/6 versus printed Rsource=(Lambda/mu)5/6=5/3. The characteristic representation also bounds infection-age L1 via decaying boundary influx and positive survival loss >=mu+gamma, establishing local asymptotic stability of this constant-rate subfamily, not general PDE stability. No unproved sign from simulations is used.

## originality

PASS

The open-access primary paper explicitly defines normalized Theta and equal per-class recruitment in Section 2, but Section 3 and Appendix (7.1) print/propagate an uncancelled Lambda/mu in R0 and Theorem 3.1 declares instability for >1. The source itself is exactly the target: the contribution is a falsifying admissible positive-parameter counterexample and corrected threshold for those literal equations, not invention of the classical degree second-moment factor. Other network epidemiology threshold papers use distinct models/contact normalization and do not supply this source-specific contradiction.

## value

PASS

The source’s disease-free stability theorem gives the wrong yes/no conclusion for a fully admissible constant-rate six-dimensional subcase: a published supercritical verdict 5/3 becomes a demonstrably stable DFE with actual invasion 5/6. Correcting a theorem-level threshold and illustrating a sharp normalization consequence are substantial mathematical quality-control results, without making unverified empirical claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
