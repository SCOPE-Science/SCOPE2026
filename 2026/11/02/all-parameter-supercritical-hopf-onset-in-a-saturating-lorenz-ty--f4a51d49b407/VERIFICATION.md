---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For sigma>0,kappa>epsilon>0, unique equilibrium (-r/sigma,0,0) follows from q=y+iz satisfying qdot=(phi(x)-1+ix)q. Eigenvalues -sigma, phi(-r/sigma)-1 +-i(-r/sigma) cross at |r|=sigma/sqrt(delta), delta=kappa-epsilon. Positive crossing derivative 2delta^{3/2}/(kappa*sigma). At positive threshold, center manifold u=a q+conj(a q)+O(|q|^2), a=sigma/[2(sigma+i omega)], omega=-1/sqrt(delta), with h11=-2c|a|^2/sigma, c=-2delta^{3/2}/kappa and d=delta^2(kappa-4epsilon)/kappa^2. Quadratic elimination gives resonant real cubic nu=|a|^2(2d-2c^2/sigma-2c/omega) = -sigma delta^3[sigma(kappa+4epsilon)+4delta]/[2kappa^2(1+sigma^2delta)]<0. Independent symbolic simplification confirmed generic identity, normal form and signs; Hopf theorem gives unique nearby attracting limit cycle for |r|>rH, amplitude asymptotics and period 2pi sqrt(delta). Sign conjugacy maps +/- r thresholds. No global orbit assertion.

## originality

PASS

Best-knowledge PASS restricted to universal explicit negative physical-amplitude cubic and all-parameter supercritical conclusion, beyond Khodabandehlou–Maes model/linear crossing/numerical Hopf observations. Full source unavailable, thus priority qualified; related Resultary Lorenz, Sprott and four-scroll Hopf calculations are different vector fields.

## value

PASS

Provides an exact and uniformly negative nonlinearity coefficient across the entire admissible family, rules out generalized-Hopf points on the stated surfaces, quantifies stable oscillation amplitude and upgrades numerical supercritical indications to a theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
