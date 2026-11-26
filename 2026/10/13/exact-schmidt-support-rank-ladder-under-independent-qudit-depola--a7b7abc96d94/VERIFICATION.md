---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the repaired claim in repairs/5/RESULT.md. The literal frozen Finding that every support rank is uniquely optimal on an interval is false: k=1 gives a product state with zero negativity, so either it loses or all ranks tie. The repair preserves that frozen evidence and restricts unique optima to 2,…,d, explicitly treating k=1. Independently expanding the tensor-product channels gives the ideal term, the two one-side mixing terms with the reduced projector P_k/k, and pq I/d². The partial transpose pairs only ij and ji in the support; in each pair its diagonal h is the sum of the mixing terms and its off-diagonal g=(1-p)(1-q)/k. The possible negative eigenvalue contributes [g-h]_+=[Δ-kΠ]_+/(kd²); summing k(k-1)/2 pairs gives the exact formula, also zero when k=1. Other eigenvalues are nonnegative. For Π>0 and Δ>2Π rank two is positive, so maximizing the truncated score is equivalent to maximizing the untruncated score, whose first differences Δ-2kΠ strictly decrease. This proves exactly the adjacent ties, with no positive tie at k=1. Δ≤2Π yields an all-zero tie, and Π=0 reduces to a nonnegative linear score in k-1. With symmetric noise, x=d(1-t)/t and Δ/Π=x²-2x strictly decreases in t in the positive region; solving x²-2x=2k gives correctly ordered, distinct switches and each entangled rank a nonempty interval. The death and full-support endpoints follow from Δ=2Π and Δ=dΠ respectively. For d=3 and p=q=1/2 the exact pair (Δ,Π)=(3/4,1/4) gives (N2,N3)=(1/72,0). The repaired statement, proof and boundary cases were reread. The verification notes and spectral checker remain scientifically compatible (the interval check already loops over k=2 through d), and no uploaded script was run.

## originality

PASS

For the repaired claim only. The checked earlier work covers the channel-level vanishing region (including the symmetric endpoint and a rank-two extremal witness), a distinct global-noise magnitude formula, or the two-qubit setting. The supported distinct result is the flat-support magnitude comparison and its exact intermediate positive-maximum rank ladder for the independent local channels, not a new entanglement-annihilation boundary. Excluding rank one from the unique-optimum intervals leaves this claim and all literature comparisons intact.

## value

PASS

The repaired result answers a concrete resource-allocation question for the standard controlled-shift conversion under physically independent local noise. Maximal initial entanglement need not maximize surviving negativity: the exact transitions identify every regime, and the rational qutrit witness shows full-support negativity already zero while smaller support remains NPT. The familiar all-input death threshold alone cannot answer which entangled support to choose at lesser noise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
