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

Conditional on a specified chord, N=2n-2 endpoints are uniformly matched. Selecting x cross-pair endpoints, bijecting them, and internally matching parity-matched remaining endpoints gives the normalized factorial PMF on x=a(mod2),...,a. For a<=n-3, direct cancellation yields R_a(x)=[(a+2)(a+1)/(b(b-1))]*(b-x)/(a+2-x), which increases strictly since b>a+2. The additional atom at a+2 and chain transitivity prove the same-parity likelihood-ratio result; R-1 has sign (2n-1)x-b(a+2). X_1 is identically 1 whereas X_2 has positive atoms at 0,2, proving the sharp opposite-parity obstruction for all n>=3. Independent exact matching enumeration and rational arithmetic confirmed 2135 bounded identities; this does not replace proof at all n.

## originality

PASS

The familiar conditional crossing-degree mass and low moments are known from random chord diagrams. The reviewed contribution is a likelihood-ratio comparison between distinct arc lengths with explicit decision threshold and sharp parity obstruction. Targeted published Resultary and primary-literature searches produced no equivalent implication in inspected passages; priority remains qualified.

## value

PASS

Monotone likelihood-ratio dominance is a stronger and usable conditional order than expectation or ordinary stochastic dominance, and yields an exact finite-sample inference threshold for a natural marked-chord observable; its parity boundary is substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
