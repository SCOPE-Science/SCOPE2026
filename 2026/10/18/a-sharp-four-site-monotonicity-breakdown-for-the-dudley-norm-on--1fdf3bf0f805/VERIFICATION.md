---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For the zero-mass measure (-1,1-t,-(1-t),1) on the unit four-path, cumulative fluxes are (1,t,1)>0. Reflect f by -f(3-i) and average to obtain a norm-nonincreasing representative (-a,-b,b,a) with the same pairing. Its norm is max(|a|,|b|)+max(|a-b|,2|b|), and pairing 2[a+(t-1)b]. The sixteen linear halfplanes have exactly six vertices ±(3/5,1/5), ±(1/3,-1/3), ±(1/3,1/3); evaluating each proves the exact unrestricted max{(4-2t)/3,(4+2t)/5} for every 0<t<1. Restricting to monotone representatives a>=b>=0, the scalar quotient 2[1-(1-t)u]/[1+max(1-u,2u)] (0<=u<=1) peaks only at u=0 or 1/3, giving max{1,(4+2t)/5}; strict mismatch for t<1/2. For <=3 sites, negative endpoint slopes may be flattened to zero: positive flux strictly improves the pairing without increasing sup-norm or path Lipschitz norm, proving minimality. Independent Fraction enumeration reconstructed 6 vertices; numerical t samples are not the universal proof.

## originality

PASS

Hille and Theewis previously supplied the general finite-space Dudley-norm linear program and norming-potential theory. That framework can in principle compute this finite instance but does not by itself state the analytic two-branch family or the minimal strictly-positive-flux monotonicity obstruction. The Resultary equiradial-star theorem also has a piecewise Dudley norm but is a distinct metric graph and does not imply the four-site path sawtooth phenomenon. Best-of-knowledge PASS limited to the closed sharp obstruction, not novelty of general LP computation.

## value

PASS

Strictly positive transport flux normally motivates monotone Kantorovich potentials for transport seminorms; the bounded sup plus Lipschitz penalty defeats this intuition first at four sites. The exact parameter crossover and cardinality minimality are motivated, sharp structural facts in a natural finite metric, not an arbitrary table slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
