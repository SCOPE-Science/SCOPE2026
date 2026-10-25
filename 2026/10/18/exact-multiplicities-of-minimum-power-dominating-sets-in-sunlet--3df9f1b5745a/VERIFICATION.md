---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For simple sunlet S_n=C_n circle K_1, n>=3, a cycle-vertex sensor can cover at most 3 core positions, a selected leaf at most 2: any core with unselected private leaf cannot force a second core while its leaf is unobserved. Thus n<=3a+2b and minimum size ceil(n/3) is attained by core dominating sets; b<=3ceil(n/3)-n. Cyclic distances between selected cores record deficiencies relative to disjoint three-block coverage. For n=3q, all gaps three (3 sets); n=3q+2, one gap two or one gap five assisted by one leaf (counts n,2n); n=3q+1, gap partitions give n(q+2)/2 zero-leaf, n(2q+1) one-leaf and 2nq two-leaf solutions for q>=2. n=4 has separate profiles (6,12,4). Independent implementation simulated initial N[S] and all legal unique-neighbor forces for every optimal-cardinality subset on n=3..13 and exactly matched all b-profiles. Finite range is not infinite proof; complete deficit/gap classification is.

## originality

PASS

Same-object Saibavani–Parvathi 2019 Theorem 3.1 gives only cardinality gamma_P(S_n)=ceil(n/3); the assigned contribution determines every optimal-placement multiplicity and pendant profile. Known graph-specific counting results concern nonisomorphic families. Best-of-knowledge PASS, not a claim that negative searches prove priority.

## value

PASS

Counting every minimum-cost power-monitoring deployment in the classic sunlet network is mathematically and practically distinct from knowing its size. The exact b-stratification detects effects of pendant sensors and a sharp exceptional four-cycle. Constant, linear and quadratic multiplicity regimes are structural, natural, all-order results rather than a single small graph calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
