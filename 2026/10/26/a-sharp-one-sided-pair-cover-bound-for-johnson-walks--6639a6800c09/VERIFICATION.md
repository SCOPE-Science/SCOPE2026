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

For a fixed pair, the Markov intersection count is lumpable until first hit into states 0,1. Direct delete/insert counting gives Q=[[1−a,a],[b,1−b−c]] with a=2/(n−r),b=(n−r−1)/(r(n−r)),c=(r−1)/(r(n−r)); its positive Perron vector (1,h) bounds survival from above/below. Summation over all m pairs gives E U_t inequalities; Markov union bound and geometric tail give only the expected cover-time limsup upper constant. Independent full-state rational transition checks verified 5≤n≤8 in selected r cases and six finite horizons. No lower cover-time constant, limiting Gumbel law, or r-growing asymptotic is proved.

## originality

PASS

The exact pair-avoidance Perron calculation supplies the conjectured one-sided cover constant in the dependent r>2,s=2 Markovian model. Original conjecture remains unresolved in this regime; independent-round and r=s results do not imply this theorem.

## value

PASS

The conjectured sharp upper constant for a genuinely dependent Markovian super-coupon pair collector is an independently useful one-sided result, with finite-time estimates and the critical unseen-pairs mean. It cannot be mistaken for a proof of the full conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
