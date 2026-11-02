---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

With prescribed SSPRK(3,3) stages A and c, order-1/2 conditions give precisely ((1-v)/2,(1-v)/2,v). R_v(z)=1+z+z²/2+v z³/4 follows by powers of A. For any 2-state generator Q, write Q=-(a+b)(I-Pi); choosing v=0 at s<2 and 4(1-s+s²/2)/s³ at s>=2 keeps R_v(-s) in [0,1] and 0<=v<=1, hence nonnegative stochastic endpoint for every step. For equal-rate three-state pure-birth Q, nonnegative first-column middle and last entries force v>=4(z-1)/(3z²) and v<=1/z, inconsistent for z>4 even over reals. Piecewise v constructions for 0<=z<=4 keep all entries nonnegative, and both inequalities at z=4 force v=1/4 and exactly identity endpoint. Independently recomputed symbolic generator products and rational 2- and 3-state examples, including z=4 and z>4. Formal order only for each fixed v; intermediate stage positivity is not claimed.

## originality

PASS

Best-of-knowledge PASS for universal all-two-state existence and sharp three-state failure for this EXACT explicit SSPRK(3,3) stage matrix under adaptive order-two weights. Nüsslein–Ranocha–Ketcheson introduce the same variable weights and a two-state example; no all-chain impossibility frontier is established there. A separate implicit SSP-SDIRK2(2) two/three-state threshold at numeric 4 is mathematically distinct and does not entail this polynomial family.

## value

PASS

Gives an exact minimum-state obstruction to endpoint-positivity LP feasibility while retaining formal second order, with sharp step-size and unique stagnant boundary. This is an actionable mathematical feasibility boundary for adaptive numerical integration, not a claim of useful large-step accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
