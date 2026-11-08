---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For exactly five line agents, sort gaps a,b,c,d>=0. Two unconstrained facilities have OPT2=min(b+2c+d,a+c+d,a+b+d,a+2b+c). Distance-proportional pair sampling has normalizer Z=4a+6b+6c+4d and weighted expected-cost numerator N. The two polynomial envelopes U1,U2 of N are obtained by choosing one endpoint service distance for each pair-client term; both dominate min. Expanded coefficients of 9 Z T1-4 U1 and 9 Z T2-4 U2 are ALL nonnegative, and reflection handles T3,T4. Thus E[SC]<=9 OPT2/4 for all real gaps, including coincidences and zero-opt cases. Independent SymPy slack coefficient re-expansion and exact enumeration of many integer gap quadruples confirmed, not substituted for polynomial proof. Gaps (T,1,0,1) give ratio (18T+22)/(8T+20)->9/4, strictly not attained for finite positive-optimum profiles.

## originality

PASS

Global Pair/Pairwise-Distance mechanism and general factor-four guarantees appear in 2026 work of Ma–Peng, Chan–Lin–Wang, and Jia. Those accessible abstracts do not establish this exact five-agent 9/4 line factor or its polynomial certificate; exact theorem is a narrow sharp population-specific improvement. No novelty claim for mechanism or incentive proof.

## value

PASS

Sharp n=5 randomized strategyproof line-facility efficiency benchmark improves a general 4 approximation and is below known deterministic lower bound n-2=3; the additional agent creates nontrivial four median cuts and ten sampled pairs. A natural exact small-market invariant, not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
