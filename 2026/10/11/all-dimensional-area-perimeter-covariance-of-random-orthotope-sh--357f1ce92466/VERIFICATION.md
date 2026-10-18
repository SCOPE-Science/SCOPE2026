---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The projection is the planar zonotope with exact \(A=\sum_{i<j}a_ia_j|D_{ij}|\) and \(P=2\sum_i a_ir_i\). The Haar row law \(r_i^2\sim\operatorname{Beta}(1,(d-2)/2)\) and uniform conditional minor direction give \(\mathbb E[|D_{ij}|r_i]=\alpha_d\), \(\mathbb E|D_{ij}|=1/(d-1)\); conditioning on a third row yields \(\mathbb E[|D_{ij}|r_k]=(\pi/4)\alpha_d\). Expanding incidence patterns produces the joint moment and covariance. Maclaurin yields \(e_1e_2\ge3d/(d-2)e_3\), with equality iff sides agree. The package proves \(\alpha_d>\beta_d\), and the key gamma-ratio recurrence for the positive coefficient was independently verified symbolically; the negative recurrence increment with positive limiting value establishes every dimension (including its separately treated \(d=3\) anchor). Gamma asymptotics yield the claimed exact power/constant. Direct independent gamma numerics through dimension 499 and the inspected Monte Carlo verifier are checks, not the infinite proof. Boundary \(d=3\) uses a valid two-frame in dimension 2.

## originality

PASS

The cited exact three-cube mixed moment, the four-cube numerical benchmark, the published four-dimensional orthotope special case, and the projection-volume CLT do not recover a closed formula for every positive side vector and dimension. The disjoint-index incidence moment plus uniform sharp covariance inequality are the genuine added content; one must compare the earlier 4D special result rather than mistake different numerical parameters for novelty.

## value

PASS

The exact mixed area/perimeter moment and sign of covariance for a common random plane are natural stochastic-geometric statistics. A sharp all-shape bound with cube equality in every dimension and a nontrivial high-dimensional coefficient establishes new structural control, not merely a re-expression of the known cube benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
