---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The rank-one linear map is trace(BX)A with a unique output line. Direct coefficient comparison of the Rota–Baxter identity yields A²=lambda A, BA=mu B, AB=(lambda-mu)B and mu(mu-lambda)=0 in any characteristic. For lambda=0, B is any nonzero map V/im A to ker A; rank-r square-zero A count is [n r]_q[n-r r]_q |GL_r|, divided by q-1 for output lines. For lambda!=0 the unique idempotent E on the output line has complementary eigenspaces, and B lies in one of the two disjoint nonzero off-diagonal blocks. Hence S_nq+I_nq counts each operator once, and R²=0 follows from tr(BA)=0. The q-degree of the rank-one square-zero term is n²-2, strictly above all other ranks for n>=3. Independent integer evaluation reproduces n=2,q=2:3+12 and n=3,q=2:315+336. Finite samples cannot establish the symbolic generality.

## originality

PASS

Best-of-knowledge originality for the exact stated theorem only; public primary comparison and published-record semantic searches found related methods but no prior statement implying the complete final claim. This is not proof of worldwide priority. No located database or exact table for all n; published Resultary exterior algebra census is for a different 4-dimensional algebra

## value

PASS

The all-n finite-field census of a natural operator identity distinguishes nil image products from nonnil image subalgebras, gives rank-refined exact counts and leading asymptotics; not merely a rephrased M_2 orbit list. An algebraist needs these precise quantities to compare matrix identities and finite-field moduli; no claim about higher-rank operators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
