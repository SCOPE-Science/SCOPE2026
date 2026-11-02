---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed the exact indexed-word/closed-walk bijection using states abcd and edges abcd->bcde iff c=1_{a+b+d+e in {0,2}}. All 16 states split into two simple length-5 cycles, a recurrent 5-state component with 3- and 5-cycles, and one dead vertex; det(I-zA)=(1-z^5)^2(1-z^3-z^5). The logarithmic derivative yields precisely the labeled count, with the formal z^3 contribution removed for n>=5. Coin representation 3a+5b covers all n>=8, excluding n=7; primitive irreducible 5-state Perron component gives E_n/rho^n->1. Independent direct binary-state/trace and brute-force checks n=5..18 passed, but do not replace proof.

## originality

PASS

Exact radius-two, nonmonotone threshold CA fixed-word count on labeled cycles is narrower than public-goods general complexity, but computes new explicit all-n formula, unique forbidden n=7 and growth. Closest prior sources treat complexity, ordinary cycles, random networks, or general radius-two CA consensus rather than this evaluated graph/rule count; priority qualified for unindexed exact cellular automaton enumeration.

## value

PASS

The 0-or-2 nonmonotone response has hard arbitrary-graph equilibrium existence, yet a natural infinite family of degree-four networks admits a complete labeled census and unique minimal-size obstruction. The 3/5-cycle transfer component produces an explicit exponential growth rate and structural obstruction, a useful exact benchmark rather than a routine graph-size substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
