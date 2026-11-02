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

For each unselected vertex its multiset of distances to the selected landmarks is determined exactly by (number of selected same-part vertices, indicator that its one deleted partner is selected), since all ordinary cross distances are one, same-part distances two, deleted cross distances three for p>=3. A side may therefore have at most two unselected vertices, and two on the same side require opposite deleted-partner indicators. For three or four outside vertices the two-part same-side-distance count creates the boundary q=p+1 and prohibits four omissions when p=q; complete combinatorial case analysis gives A2=t(p+q-2t)+(pq if p<q else 2t(p-t)), A3=t(t-1)+t(p-t)(q-1)+1_(q!=p+1)[t(t-1)+t(q-t)(p-1)], A4=1_(p<q)t(t-1)[t-2+(p-t)(q-t)]. The crown p=q=t=n coefficients A2=A4=0 and A3=2n(n-1) prove the missing cardinality layer. Independently enumerated all subsets by BFS over 43 distinct parameter triples (3<=p<=5,p<=q<=6,0<=t<=p), reproducing the entire polynomial; finite tests only corroborate the all-parameter combinatorial argument.

## originality

PASS

The 2019 foundational outer-multiset paper and the 2022/2023 primary follow-up do not state the deleted-matching all-cardinality enumerator. Published complete-multipartite results cover only t=0, where no distance-three marker exists. The balance-dependent missing cardinality layer for t>0 is additional and not a corollary of known scalar results. The October 2026 circulant/diameter paper is a residual abstract-level comparator.

## value

PASS

The complete polynomial of resolving landmark sets for a canonical infinite near-complete bipartite family is a natural robustness invariant, and the unexpected crown endpoint skips the entire cardinality layer just above its minimum, exhibiting nonmonotonicity of outer multiset resolving property. Exact balance transitions p=q and q=p+1 are structural, not arbitrary slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
