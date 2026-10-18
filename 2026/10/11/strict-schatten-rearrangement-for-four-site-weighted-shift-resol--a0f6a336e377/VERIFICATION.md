---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For nonzero complex a,b,c, unitary diagonal conjugation removes phases. The exact upper triangular R=(I-N)^-1 has entries 1,a,ab,abc; 1,b,bc;1,c;1. Setting x=|a|²,y=|b|²,z=|c|², independently expanded Gram characteristic polynomial P_A(t)=t⁴-A t³+B t²-Ct+1 with A=4+x+y+z+xy+yz+xyz, B=6+2(x+y+z)+xy+xz+yz, C=4+x+y+z. For fixed multiset only A varies, strictly increasing with central y: exchanging central squared weights x<y changes A by z(y-x)>0. Positive tridiagonal irreducible inverse Gram matrices ensure four distinct positive roots at realizable endpoints. The equation A=H(t)=t+B/t-C/t²+1/t³ has at most three positive critical points by Descartes; the four-intersection horizontal-level interval between endpoint A values retains simple positive roots. Implicit differentiation gives d/dA Σlambda_j^q=q times third divided difference of t^(q+2), whose third derivative q(q+1)(q+2)t^(q-1)>0 for q=p/2>0. Hence all positive p power sums strictly rise; alternating P_A' signs give singular-value pattern (+,-,+,-), and operator norm grows too. I independently calculated exact Gram characteristic polynomials for rational positive triples and spot-checked p=1/2,4 moment orderings. This finite sample is not the all-real-p proof.

## originality

PASS

Best-of-knowledge original simultaneous permutation ordering across all positive Schatten power moments of a 4-site nilpotent resolvent. Chang–Wang studies numerical radius of weighted shift N rather than singular values of (I-N)^-1, Higham supplies generic inverse norm bounds, and Li–Gu–Parlett addresses singular-value algorithms. Similar Resultary weighted-shift entries concern infinite shifts or numerical radii, not the exact four-site resolvent.

## value

PASS

Natural minimal dimension for nontrivial placement-dependence (three sites have transpose/reversal invariance). A single exact ordering theorem simultaneously handles all S_p norms, positive quasi-norm moments and operator norm despite individual singular-value crossings, a useful spectral-rearrangement fact rather than a finite numerical anecdote.

The dated certificate retains the supplied scientific assessment, sources and limitations.
