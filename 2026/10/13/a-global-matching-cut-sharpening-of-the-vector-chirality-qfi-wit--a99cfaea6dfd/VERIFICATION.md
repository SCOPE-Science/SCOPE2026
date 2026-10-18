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

Starting from the displayed local variance allocation in the actual Shimokawa source A_u=(n_u²+c_u)/16, in either of two disjoint-edge perfect matchings each crossing edge is incident to exactly two partition blocks, so sum_u c_u=2C. If largest block m>N/2, a crossing matching edge must use one of the N-m external vertices and no external vertex serves two matching edges; hence C<=N-m. For m<=N/2 use sum c_u<=N. For k>N/2, if m<=N/2 sum n_u²<=N²/2 and the numerical bound is <=f(k); if m>N/2, sum n_u²<=m²+(N-m)² and f(m)=m²+(N-m)²+2(N-m) increases for integer m>=N/2+1. With m<=k, f(k)=k²+(N-k)²+2(N-k). At k<=N/2 the existing qk²+s²+N remains. The QFI square-root triangle inequality applied to odd/even matching, followed by convexity for mixed k-producible states, gives the displayed all-k formula. Independently enumerated all integer block partitions for every even N=4..24 and all 1<=k<=N and confirmed the exact combinatorial maximum. That enumeration checks only the relaxation; the unrestricted proof depends on the combinatorial cut and source variance allocation.

## originality

PASS

The source paper proves F_Q<=qk²+s²+N for even periodic spin chains, explicitly replacing c_u<=n_u before summing, whereas the proposed global matching cut counts the c_u jointly and subtracts 2k-N for k>N/2. The general linear single-site k-producible QFI theorem of Hyllus et al does not apply to this two-site vector chirality. The improvement is a new inequality relative to these inspected sources; a different entanglement partition argument could imply it under another name, which remains a risk.

## value

PASS

This is a physically motivated tightening of a published entanglement-depth certification threshold for the large-block regime, not an arbitrary small integer improvement. Although the bound need not be exactly attainable, the strengthened finite-size witness can certify depth in the window excluded by the older numerator. The endpoint k=N yields the natural N² estimate. The gain is limited to k>N/2 and the same local inequalities may remain loose, explicitly limiting practical effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
