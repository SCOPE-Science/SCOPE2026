---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The source eigenvalues lambda0=e^{-i(1-t)gamma}, lambdaj=-e^{i beta_j t} and on-shell mu=(k-1+(k+1)lambda)/(k+1+(k-1)lambda) imply exactly mu(k,e^{i phi})=(k+i tan(phi/2))/(k-i tan(phi/2)). For j>=1, cot(beta_j t/2)~2/(beta_j t), so mu_j tends to (beta_j xi-2i)/(beta_j xi+2i); beta_j=0 stays -1. Fixed finite alpha keeps j=0 away from singular -1 and mu0->1. Paired j,n-j modes are conjugate, so reflection is real; every nonconstant paired term (beta² xi²-4)/(beta² xi²+4) increases strictly, endpoints are negative to positive, and unique reflectionless xi_n follows. Independent direct double-scaling checks for n=3,4,7,10 and multiple xi confirm analytic limits; independent source verifier n=3..12 checks paired identities and xi3,xi4.

## originality

PASS

A distinct joint singular t*k scaling and unique transparent reflection point were not found in checked published quantum-graph source/results. The original authors’ fixed-t high-energy parity dichotomy, static equi-transmitting theory, and square-lattice band results do not alone specify this exact one-vertex crossover. Source full text remains unavailable, a material residual risk explicitly retained.

## value

PASS

The singular t->0 and k->infty limits do not commute; locating the all-n exact crossover and unique reflectionless transparent point reveals a physically meaningful sharp boundary in this natural scattering family. The result quantifies local vertex transport, not a routine fixed-parameter expansion, and requires a monotonicity proof across Fourier modes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
