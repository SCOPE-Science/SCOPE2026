---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For Q=[[-a,a],[b,-b]], a,b>0, the exact projector Q=-(a+b)(I-Pi) yields T=Pi+r(s)(I-Pi), r(s)=(6-2s)/(s²+4s+6), s=(a+b)h. Since 1-r=s(s+6)/(s²+4s+6)>0 for s>0, off diagonals are positive and positivity is precisely F_m(s)=m s²+(6m-2)s+6>=0, m=min(a,b)/(a+b). The discriminant 4(9m²-12m+1) and positivity of its roots yield critical m_c=(2-sqrt3)/3 (rate ratio 5+3sqrt3), two separated admissible step intervals when m<m_c, and quadratic tangency at equality. Also -1<r<1 and 0<=r²<1 give strict stationary-weighted contraction and strictly positive T². Independent direct rational inversions match 60 2x2 matrices, including a=19,b=1, h=1 diagonal -4/243 and identical matrices at h=1/5, 3/2. The infinite parameter result is proved algebraically, not inferred from samples.

## originality

PASS

The primary energy-law theorem gives norm contractivity, not this generator-specific entrywise Markov positivity phase diagram. Complete exact published results for [1/1] Crank-Nicolson, midpoint-square SSP-SDIRK2 and [2/2] Padé use distinct rational stability functions and lack the [1/2] two-state reentrant rate threshold. The exact 5+3sqrt3 frontier and disconnected step intervals survive this implication comparison. This is best-of-knowledge, with inaccessible old RK and recent Fokker–Planck sources explicitly reserved.

## value

PASS

Entrywise positivity is necessary for a numerical Markov propagator to preserve probability even when it contracts in energy. This is a complete sharp minimal two-rate phase classification for a canonical third-order stiff solver, including a nonmonotone gap and exact rate-imbalance boundary; it is motivated by stochastic numerical integration and is not a generic renaming or mere small numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
