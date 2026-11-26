---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A nilpotent partial injection is a disjoint union of chains; index n forces one chain through all n vertices. For the preserving calculation put m=n−1, b=g(0), d=g⁻¹(0), a=g⁻¹(m). The successor recurrence increments by one except at i=a or i=d−1. If d−1<a, then g(d−1)=b+d−1 but the deletion of 0 forces b=g(d−1)+1, impossible. Thus a≤d−1 and g(a)=m=b+a, giving b+d>m. From d onward g(i)=i−d, and if the middle interval is nonempty, the recurrence starts it at g(m)+1=m−d+1. This proves the three branches; substituting verifies the converse. Their rotation first-return description is valid because an overshoot into (m,b+d) returns to [0,m] on the next step; every gcd(b,d) residue class meets [0,m]. Thus one cycle means coprimality and precisely a Farey gap. For reversal, any reversing partial bijection between the two circle subsets extends over their gaps to a reversing circle homeomorphism. Its decreasing lift yields exactly two fixed points and it exchanges the intervening open arcs. The even subsequence is a strictly monotone orbit of its increasing square in the first arc, and the odd subsequence runs in opposite order in the second. These give exactly the two displayed words, both satisfying anti-order after deletion. All rotations give n distinct labeled placements; preserving and reversing are disjoint on a domain of size at least three. The summatory-totient estimate gives the stated asymptotics. Independently enumerated preserving/reversing/union results at n=4,…,8: (16,8,24), (30,10,40), (60,12,72), (84,14,98), (144,16,160).

## originality

PASS

Pass is for the semigroup classification including the reversing branch and full oriented maximal-index census, not the preserving numerical sequence or the Sós recurrence. Those are explicitly credited and exactly match older Sós/Farey combinatorics. The inspected closest same-monoid Resultary theorem restricts its counts to adjacent endpoints and has no reversing branch. The two cyclic parity words and exactly 2n extra maps are not consequences of the inspected Sós classification of increasing order or of the endpoint result. This is a bounded assessment of the distinct claim, not a priority certificate.

## value

PASS

Maximum nilpotency index selects a canonical extremal layer of the two monoids. The exact classification up to rotation explains why a substantial Farey family is possible for one orientation but only two parity orders for the other, and fully determines the oriented count. The useful increment is this structural distinction, not the already tabulated preserving numbers or the standard totient asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
