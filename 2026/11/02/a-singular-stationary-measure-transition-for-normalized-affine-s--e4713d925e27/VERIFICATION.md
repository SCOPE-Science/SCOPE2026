---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For n>=2, alpha,r in (0,1), write x=h e+sqrt(1-h²)v. The map becomes (f(h),-v) with f=(alpha-h)/sqrt((alpha-h)²+r²(1-h²)), derivative strictly negative. The unique fixed h is alpha/(1+r). The exact period-two factorization is [alpha-(1+r)h][alpha-(1-r)h][alpha²+r²-1]/alpha², with the second candidate invalid because the required positive norm would be -r. An increasing f² has no longer scalar periodic orbits, and monotone iteration plus explicit pole/latitude multipliers gives basin exchange at alpha²+r²=1. Invariant measures away from resonance are mixtures of symmetric pole pair and latitude antipodal pairs, all singular against surface measure. At resonance f(h)=(alpha-h)/(1-alpha h), f²=id, surface Jacobian [r/(1-alpha h)]^n and symmetrization gives rho=(1+J_F)/2. Independent SymPy symbolic identity check and source verifier reading support the algebra.

## originality

PASS

Best-of-knowledge PASS qualified for global basin and complete invariant-probability simplex in n>=2, not for known circle involution criterion. The 2022/2024 Choudhuri–Faraco–Yadav paper Prop.3 already gives meridional resonance condition; inspected higher-dimensional results concern distality/expansivity, not a complete invariant-law classification.

## value

PASS

A full all-dimension classification of invariant probabilities and a sharp exchange of two attractor strata is a natural topological-dynamical result. The presence of smooth full-support invariant probability only on a codimension-one involution locus is mathematically meaningful beyond the known meridian criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
