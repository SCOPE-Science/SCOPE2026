---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Set a=p/(1-p). The chain has resets to zero, can reach any state from zero, and has drift 2−a+O(p^x), proving positive recurrence for a>2. The leading cubic drift is 3(4−a)x², with O(x+1) remainder; integrating the drift of min(x³,R), not x³ itself, proves sufficiency without assuming stationarity has a third moment. For necessity, the conditional PGF summed over geometric emigration gives (1−ah)g(h)=(1−h)/(1+h)g(h/(1+h))+(1−a)Bh. Under the respective first- and second-moment hypotheses integrate g′ over [h/(1+h),h] before extracting coefficients; the resulting identities are (a−3)m=2 and (a−4)E[V(V−1)]=4+10m. Their positive right sides exclude equality as well as the subthreshold regimes. The raw second moment is 6a/((a−3)(a−4)), and subtracting the squared mean gives the stated variance; the mean remains bounded at the second-moment boundary, so both pole coefficients are 24/25. Read the frozen Python and output as evidence only. The separate exact conditional-PGF derivative/geometric-sum checks and pole calculation ran with `python3 /workspace/branches/review_reproduction.py 3`; these are finite checks, not the proof. No Lean or expert attestation was performed.

## originality

PASS

Credit Carper for the exact model, recurrence and first-moment results, and exact stationary transform. The supported distinct claim is the stationary one-time second-moment boundary (including equality), its exact formula and pole. A finite-moment expansion of the previously available transform alone does not establish the regime where those coefficients exist. No inspected earlier result supplies the combined higher-moment claim; this is a bounded assessment, not historical-priority certification.

## value

PASS

It separates finite-mean and finite-variance behavior of an existing model tied to an excited random walk. The exact pole quantifies variance growth near the second transition, information neither a first-moment solution nor an excursion bound provides. The drift/truncation and equality obstruction make this more than a numerical evaluation of an invariant; the claim remains about the invariant population only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
