---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For finite graphs with positive edge weights and gamma>0, R(f)=max(f,0) is linear on each sign orthant, giving global two-point Lipschitz modulus max_S ||D_S||_A (attained locally). For A=I+gamma L, cut blocks X,Y,B, a Schur complement gives ||D_S||_A=(1-rho(S)^2)^(-1/2) with rho=||X^-1/2 B Y^-1/2||<1. Edgewise Cauchy–Schwarz plus crossing degrees c_i<=Delta yields rho<=gamma Delta/(1+gamma Delta), hence Lip<=(1+gamma Delta)/sqrt(1+2gamma Delta). Equality propagates positive maximizers to a whole bipartite component with weighted degree Delta, and any such component supplies equal singular vectors. Unit star Schur elimination gives exact sqrt(1+n gamma^2/[1+(n+1)gamma]); one-point energy contraction and nontrivial two-point expansion are compatible. Edgeless, isolated/disconnected boundary cases accounted for.

## originality

PASS

Best-of-knowledge originality qualified by material actually accessed. The example directly rules out any implication that normal contraction supplies two-point nonexpansiveness, supporting the mathematical distinction. Relevant literature not wholly indexed or accessible; see source_inspections and residual_risks.

## value

PASS

Quantifies a natural stability failure of a standard normal contraction under the graph-Sobolev metric. An exact graph-specific cut spectral formula, sharp degree-only bound, rigidity of extremizing graphs, and divergent irregular-star contrast answer precise, useful stability questions not mechanically implied by one-point Dirichlet contraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
