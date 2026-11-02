---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Omitting one of the k+1 agents yields exact weights P/g1 and P/gk for end omissions and P(1/g_j+1/g_{j+1}) for an interior omission, where P=product g_i, and realized omitted distances are g1, gk, or min(g_j,g_{j+1}). Sum weights 2P sum g_i^-1 and costs P[k+1+sum adjacent min/max]. At least two of k+1 agents share one of k arbitrary facility locations, so triangle inequality gives OPT>=minimum gap; placing one facility at each remaining report attains that bound. Every omitted agent has positive selection probability, so C=OPT iff every omission is cost-minimal. For an index with minimal gap m, any neighboring ratio u=m/g_neighbor>0 yields C/m<= (2k-1+u)/(2(1+u))<k-1/2. Family (1,T,...,T) tends to k-1/2. Independently enumerated every omission with exact Fraction arithmetic for k=2..5 and gaps in {1,2,3,4}^k (1360 profiles), reproducing the identities and boundaries. Coincident sites have OPT=0 and ratio undefined; not part of the ratio statement.

## originality

PASS

The product-gap selection rule itself and its unrestricted 2k approximation guarantee are known from Jia and Chan–Lin–Wang. The exact n=k+1 closed expectation, sharp k-1/2 frontier, and optimality iff gap pattern are not in accessible abstracts; prior papers’ full texts were inaccessible in this run and could conceal a specialization. A best-of-knowledge qualified PASS, with explicit remaining primary-literature risk.

## value

PASS

Exactly k+1 agents is the smallest population with a nontrivial randomized omission, and the fixed-population welfare frontier materially refines the unrestricted 2k guarantee. The formula describes all profiles, sharp degeneration and exact equality structures; for k=3 it reduces the worst case from published global bound 6 to 5/2 for the four-agent subfamily. No claim for strategyproofness at k>=4 or larger n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
