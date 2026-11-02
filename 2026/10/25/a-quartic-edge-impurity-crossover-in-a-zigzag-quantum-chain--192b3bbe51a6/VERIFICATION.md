---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Exact dispersion E=E_pi+8eta u-(1+4eta)u², u=1+cos k, yields band top E_max=2−2a for a≤1/4 and 2a+1/(4a) for a>1/4. A positive rank-one perturbation creates exactly one simple exterior eigenvalue via 1=epsilon G_a(E), monotonic with divergent G at the upper band edge. At a=1/4+s epsilon^(2/3), E=E_pi+epsilon^(4/3)y, k=pi−epsilon^(1/3)x, the exact denominator rescales to y−4sx²+x⁴/4 and admits uniform compact-y domination by C/(1+x⁴). Thus epsilon G converges locally uniformly to 1/[2 sqrt(y) sqrt(sqrt(y)−4s)], and monotone root bracketing gives t²(t−4s)=1/4, t>max(0,4s). Exact edge shift gives actual band-gap coefficient; s=0 coefficient 2^(−4/3); asymptotic tails checked. Independent numerical quadrature at s=−2,0,1 confirmed limiting Green function=1 near exact roots to ~1e−12.

## originality

PASS

The 2015 same-lattice work gives dispersion, impurity state and critical hopping ratio; these known components are excluded from the novel claim. The claimed fixed-detuning double scaling and exact crossover cubic were not identified in accessible full/abstract evidence. Earlier long-range transfer-matrix paper could contain an implicit equivalent specialization; its full text was inaccessible, and priority assessment is explicitly qualified.

## value

PASS

The band top undergoes a quartic merger at a=1/4; weak rank-one binding then changes its exponent. The epsilon^(2/3)/epsilon^(4/3) scaling and continuous analytic cubic crossover describe this canonical spectral transition, including exact critical coefficient and two asymptotic sides. This is not arbitrary parameter tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
