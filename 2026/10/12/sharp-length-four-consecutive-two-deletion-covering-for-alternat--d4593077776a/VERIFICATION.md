---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Each alternating word (a,b,c,d) has precisely deletion descendants (c,d),(a,d),(a,b), at most three in X×Y, so covering mn pairs needs >=ceil(mn/3) words. For nondegenerate a!=c,b!=d each word is a 3-edge P4 in K_{m,n}. A 3×t block partitions into exactly t paths by decomposing t columns into 2 and 3, using direct 3×2 and 3×3 word tilings. Full finite bases (2,2),(2,3),(2,4),(3,3),(4,4), transposes and (3,4)/(4,3) checked independently. For m>=5 split off three rows, apply induction to the remainder and add exactly n paths; else split three columns, add m. Ceiling compatibility ceil((m−3)n/3)+n=ceil(mn/3) proves all m,n>=2. Independently reconstructed construction, verified distinct codewords, exactly three descendants per word, cover of all mn pairs and optimal count on ALL 1156 rectangles with 2<=m,n<=35. The tests check seeds/replay; unrestricted theorem follows from induction.

## originality

PASS

Teypaz–Rapine Theorem4.1 classifies EDGE-DISJOINT P4 PARTITIONS of Kmn, iff 3 divides mn and both parts>1; those divisible congruence classes are acknowledged prior work. Nondivisible congruence classes require overlapping exact covers rather than partitions, supplied by new base seeds and three-row/column induction. Xie–Sun–Ge (2026) treats general q-ary two-burst deletion covering with a weaker q-ary existence bound and the special binary perfect case; its abstract and identified theorems do not establish the rectangular exact invariant, though the whole paper was not lawfully read here. Published Resultary length-three single-deletion cover for odd q has the same numeric ceiling but different received channel/triangular hypergraph, with no immediate logical implication to this P4 cover.

## value

PASS

Exact optimal size for every m,n>=2 of the natural length-four adjacent-two-deletion covering problem, including all q-ary diagonal cases, with an explicit uniform construction. It solves nondivisible cases where known decompositions cannot apply, and the exact small redundancy 0/1/2 is informative for short synchronization codes. This is a natural complete classification, not just another finite table or arbitrary alphabet slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
