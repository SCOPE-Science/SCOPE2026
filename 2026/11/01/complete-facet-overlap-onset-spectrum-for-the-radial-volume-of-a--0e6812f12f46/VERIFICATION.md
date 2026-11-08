---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Unit facet normals have Gram G=((d+1)/d)I-(1/d)J for every k<=d, with inverse (d/(d+1))I+d/((d+1)(d-k+1))J and determinant g. For y_i=<u_i,x>-1>=0 and orthogonal z, |x|²=rho²+2a sum(y)+y^TG^-1 y+|z|² with rho²=dk/(d-k+1), a=d/(d-k+1); Jacobian g^-1/2. Integrating the z-ball yields the exact orthant k-dimensional integral, valid with exponent zero interpreted as an indicator for k=d. Rescaling y by excess T=t²-rho² and dominated convergence over the standard simplex gives power (d+k)/2 and exact coefficient pi^((d-k)/2)(2rho)^((d+k)/2)/[(2a)^k sqrt(g) Gamma((d+k)/2+1)]. The k=d onset is outside the simplex vertex radius d but is a genuine term of global inclusion-exclusion, whose contributions cancel to give CDF1 for t>=d. The d+1-fold exterior is empty since sum normals=0. Independent Gram inverses, determinants, thresholds d=3..9 and the d3,k1 spherical cap coefficient pi were verified.

## originality

PASS

After direct mathematical implication comparisons, no inspected prior theorem gives the entire final claim; positive classification is best-of-knowledge, not an absolute historical priority certificate. For a regular d-simplex (inradius1), all k-fold exterior facet-overlap integrals in concentric balls have sharp ordered onset radii sqrt(dk/(d-k+1)), powers (d+k)/2, explicit positive gamma coefficients, and yield an exact finite radial CDF by inclusion-exclusion.

## value

PASS

The entire ordered k-facet-overlap onset spectrum and coefficients for a natural regular simplex radial statistic provide a motivated exact classification through the terminal vertex threshold, a potentially useful benchmark for finite-dimensional stochastic geometry; the result is not claimed as an elementary closed density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
