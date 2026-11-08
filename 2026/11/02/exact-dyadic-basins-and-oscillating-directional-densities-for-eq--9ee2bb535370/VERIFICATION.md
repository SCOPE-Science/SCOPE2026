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

Compute exact projection distances sqrt(3)|1-t|/2 and sqrt(3)|t|/2, yielding branches T(i,t)=(i+1,(1-t)/2) for t<1/2 and (i-1,1-t/2) for t>1/2, with tie at midpoint fixed. Center p=t-1/2; outer |p|>1/2 gives sign flip and r_next=r/2-1/4, so r_m+1/2=2^-m(r0+1/2). Inner 0<|p|<1/2 keeps sign and contracts by -1/2 to s/6: two globally attracting 3-cycles, while exact dyadic shell boundaries hit fixed midpoint. Alternating shell lengths (1/2,1,2,4,...) yield the two limit densities 2/3 and 1/3. Nonperiodic points are nonrecurrent; Poincare recurrence forces invariant probabilities onto 9 periodic points and hence five extremal orbit measures. Independently checked 28 exceptional positions, 15 exact shell endpoint equalities. The phase space is complete lines, not finite sides.

## originality

PASS

Earlier qualitative convergence and exact existence of two equilateral three-cycles are acknowledged as covered. The new claim is the global labelled basin partition, dyadic exceptional set, nonconvergent one-sided basin densities and all invariant probabilities. Published cycle classification does not imply a full global basin answer.

## value

PASS

The complete transient-basin and invariant-measure census for an established discontinuous projection system reveals logarithmically oscillating directional basin proportions despite convergence of every orbit. Exact 1/3,2/3 accumulation values form a natural sharp global dynamical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
