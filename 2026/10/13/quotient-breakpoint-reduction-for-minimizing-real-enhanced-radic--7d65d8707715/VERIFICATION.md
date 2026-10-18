---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For each prime valuation m and degree d, the exact exponent is m-floor(m/d)(d-1). If the quotient is unchanged from d to d+1, its exponent falls by floor(m/d). At every 2<=d<M not in the union of integer-quotient plateaus, all prime quotients are unchanged and at least one positive, so P_(d+1)<P_d. The endpoint M is itself floor(M/1). There are at most 2 floor(sqrt(m)) distinct floor(m/q) values per prime. This proves every global minimizer is in the candidate set for M>=2, without assuming monotonicity at breakpoints. If M=1 all d>=2 give exponent 1. Independently tested 4368 exponent vectors of lengths 1..3 with entries 1..16 using integer prime products and checked full argmin containment, strict omitted-step descent, and the count; the Reyssat valuations 10,5,1 give candidates {2,3,5,10} and minimizing degree 5.

## originality

PASS

The exact real enhanced-radical degree objective and a full finite search were already published by Laniewski–Müller, and de Weger originally defined and tabulated the degree dependence. The present constraint to union of distinct integer quotients uses a standard floor-division trick, but no identical pruning claim was found in material inspected. The highly relevant new paper full text was inaccessible through arXiv/OA and authorized institutional access, so originality is only best-of-knowledge, with material risk. No claim that ordinary floor-quotient enumeration is original.

## value

PASS

The enhanced-radical objective is a genuine exact finite optimization in a number-theoretic presentation problem. Eliminating every non-breakpoint degree yields a proof-backed reduction from potentially M candidates to at most 2 sum sqrt(m_l), directly useful for large valuations and across all triples; no factorization, abc bound or global conjecture is claimed. It adds a structural answer to a specifically motivated degree-search question, not merely the previously tabulated Reyssat optimum. Its mathematical depth is modest because the mechanism is a short floor-quotient observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
