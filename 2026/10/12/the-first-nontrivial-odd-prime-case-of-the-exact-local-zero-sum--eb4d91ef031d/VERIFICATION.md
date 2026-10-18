---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: For units R modulo 25, exact-five-position subset sums S_j update as S_j'=S_j union (r+S_{j-1}); the pruning invariant S5∩{5,10,15,20}=empty is hereditary under extensions, and sorting makes enumeration of nondecreasing multisets exhaustive without omitting repeated positions. I independently reimplemented the state recurrence and traversed all such multisets; witness-free counts for depths 0..10 are 1,20,210,1540,8855,35700,78700,89100,58350,21600,3900, and depth 11 is empty. The explicit 10-multiset (1,1,1,1,2,2,2,2,17,21) has no targeted five-position sum among all 252 position subsets. Thus s1(5)=11; no assertion for p>=7.

## originality

PASS

PASS (best of knowledge): Gao--Jiang--Lei--Lin--Yang formulate the exact-p local zero-sum problem and give upper bound 3p-2=13 at p=5; Sun gives an ambient lower bound 2n+1=11 and conjectures equality, not the p=5 upper 11. Flexible-cardinality local zero-sum literature does not cover an exact five-term subset. Resultary's s1(4) exact computation is a different modulus. Relevant full Gao and Sun primary papers remained inaccessible after lawful OA/arXiv and authorized institutional attempts; no absence-of-overlap claim beyond inspected material is warranted.

## value

PASS

PASS: The smallest odd prime p=5 where the published 3p-2 upper bound is weaker than the conjectured 2p+1 value is a canonical test of the explicitly open local zero-sum conjecture. The exact uniform upper bound and complete 3,900-extremal-multiset count are independently meaningful finite theorems; no general prime theorem is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
