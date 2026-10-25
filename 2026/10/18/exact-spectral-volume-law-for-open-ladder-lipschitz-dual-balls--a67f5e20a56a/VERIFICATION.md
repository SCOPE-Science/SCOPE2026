---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For L_n=P_n□K2 with f(1,0)=0, the triangular unimodular change to rung slopes s_i∈[−1,1] and horizontal top slopes u_i makes each u_i admissible on an interval of length 2−|s_i−s_{i−1}|. Fubini yields V_n=<1,T^(n−1)1>, T having positive-semidefinite Gram kernel 2−|x−y| on [-1,1]. The resolvent u=(I−zT)^−1 1 solves u=−2zu with the even Robin-type endpoint equation, giving GF 2sin(sqrt(2z))/[sqrt(2z)(cos(sqrt(2z))−sqrt(2z)sin(sqrt(2z)))]. The even eigenfunctions cos(ρ_jx) satisfy tanρ_j=1/ρ_j; spectral weights 4/[ρ_j²(ρ_j²+2)] are strictly positive, giving exact series, strict Cauchy–Schwarz log-convexity and ratio limit 2/ρ_0². Independently computed 240-point Gaussian–Legendre discretized-kernel iterates for n=1..7 and compared every V_n to given exact rational values (relative errors <5e−5); finite quadrature only checks the analytic proof, not exhaustive n.

## originality

PASS

The duality with the polar symmetric edge polytope and generic graph-metric volume methods are prior art, explicitly credited. The fully inspected D’Alì et al. 42-page primary paper has polar-dual lattice point formulas (e.g. Proposition 65) but not the identified open-ladder continuous anchored-volume generating function, spectral decomposition or strict consecutive-ratio law. Those constitute a new evaluated family on the available evidence; unindexed ladder-specific formulas or general transfer-operator corollaries remain residual priority risks.

## value

PASS

The real Lipschitz potential polytope of a natural graph strip is a meaningful transportation-cost metric invariant. An all-length rational generating sequence, continuous spectral interpretation, strictly increasing volume ratios and explicit geometric growth rate provide reproducible exact structural information beyond generic polar lattice-point formulas or isolated small-graph computation; downstream theorem is not needed for its value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
