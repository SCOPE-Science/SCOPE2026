---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

From the incidence basis x_i=e_{u,v_i}, y_i=e_{v_i,w}, z=e_{u,w}, the sole nonzero products are x_i y_i=z, so squares span kz and give hyperbolic quadratic form q(x,y)=x^T y. A bijective square-preserver must fix the square-span line up to multiplier and induce q-similitude on A/kz; its shear is arbitrary. Associative product preservation forces coordinate block diagonal M=diag(P,cP^{-T}). Linearization of D(a²)=D(a)a+aD(a) produces S=λI−P^T and alternating off-diagonal Q,R with zero diagonals even in characteristic two; ordered derivation identity forces Q=R=0. Dimension counts then follow. Hyperbolic bases count O^+(2r,q) recursively by S_r=(q^{r−1}+1)(q^r−1) isotropic nonzero first vectors and q^{2r−2} mates; multiplier surjectivity and central shears give both group orders and index. Independently generated linear constraints (not using supplied normal-form checker) returned ordinary/Jordan dimensions (r+1)^2,2r²+r+1 for r=1..4 over F_2 and F_3, including zero-diagonal char-2 restrictions. These checks corroborate the all-field proof.

## originality

PASS

Classical split-orthogonal similitude orders are not new; the asserted contribution is identifying full square-preserving versus genuine associative symmetries and their infinitesimal difference for the branching diamond radical uniformly in all characteristics. The closest triangular-ring Jordan theorems concern unital/2-torsion-free algebras or full niltriangular chain rings; inspected statements do not classify this sparse nonunital branching radical. The two closest 2010/2011 complete articles remained inaccessible despite lawful access attempt (institutional VPN disconnected), leaving specific material priority risk. Their inaccessibility alone does not negate a best-of-knowledge PASS.

## value

PASS

The branching diamond is a canonical height-three incidence-poset family, and its radical has a natural non-symmetric multiplication despite a highly symmetric quadratic square map. Classifying the full Jordan/associative symmetry gap in every characteristic and its r(r−1)-dimensional infinitesimal defect exhibits a structural phenomenon, rather than an arbitrary numerical slice. The explicit finite-field index quantifies this distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
