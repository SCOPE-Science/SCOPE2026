---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS. The path matching determinant identity det(I-sA-tA*)=1-S st+P(st)^2, standard mixed-shadow generating formula and the second/fourth absolute moments recover exactly (S,P) from the full shadow; compact support makes all mixed moments measure-determining. Fixing P and S, let v=x+z∈[2√P,S], then x=(v+√(v²-4P))/2 and y=S-v. Squared operator norm max(x,y) is max of increasing and decreasing branches, yielding exact L/U endpoints with transition S=3√P. The Schatten-fourth power x²+y²+z²=v²-2P+(S-v)² is convex, so its minimum crosses at S=4√P and maximum is endpoint v=S; continuity fills intervals. Reduce universal squared norm ratio U/L to r=S/√P; monotonicity makes unique maximum at r=3 equal φ². Fourth-Schatten power ratio maximizes at r=2+√2 with value 1+√2. Explicit valid squared weights attain both. Independent exact 4x4 determinant expansion and branch optimization tests succeeded. Boundary S=2√P, b=0 included.

## originality

PASS

PASS, restricted to quantitative optimization. Dunkl–Gawron–Holbrook–Puchała–Życzkowski (2010/2011) already establish general numerical shadow moment theory, rotational equivalence, scaled Jordan-block shadow reductions and possible matrix nonrigidity. Those known statements directly cover the (S,P) invariant and are not credited as novel. New asserted part is entire within-shadow interval/classification and optimal pair of distortion ratios. Related Resultary 2026 Schatten-fourth weighted shift numerical-radius results concern a different observable/norm and do not imply this fiber optimization as inspected. Unindexed operator-norm refinements could exist.

## value

PASS

PASS. Full numerical shadow is a canonical random quadratic observable; quantifying exactly how much operator and Schatten-four norms can vary while its entire distribution remains fixed is a motivated inverse-spectral stability invariant. Different extremizing fibers give genuinely distinct sensitivity scales, not a mere rename of shadow equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
