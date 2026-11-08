---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For exactly one eastbound H and one northbound V car, ordered east-then-north updates on m>=2 by n>=2 torus reduce by (a,b)=(xV-xH,yH-yV) to R(1,0)=(1,-1), R(1,1)=(0,1) and otherwise R(a,b)=(a-1,b-1). Free classes labeled a-b mod g=gcd(m,n) and exceptional jumps fully yield: g>=3 at most one block and eventual full period L=lcm(m,n), exactly 2L-1 blocking initial relative positions; g=2 one H and one V block every L+1 complete moves; coprime g=1 one-species blocks with inverse r of m mod n: H only if 2r>n period m(n-r)+1, else V only period mr. Verified full-position closure by displacement multiples and no shorter relative recurrence. Independently physically simulated all 4,125 valid relative placements on 100 grids 2<=m,n<=11, matching periods and block counts; the infinite statement rests on congruence proof.

## originality

PASS

The published BML rectangle literature treats many-car aspect-ratio dependent jammed states, and square-grid small-cardinality results establish eventual flow for a different geometry. Neither inspected work classifies all two-car rectangular states via gcd, modular inverse, and exact periods.

## value

PASS

The exactly two-car regime is the smallest nontrivial interaction model; a sharp gcd1/gcd2/gcd>=3 change displays persistent congestion at arbitrarily low density and precise speed deficits, clarifying limitations of square-grid free-flow intuition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
