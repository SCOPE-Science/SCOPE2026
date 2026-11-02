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

For X=[[c,a],[b,-c]], direct multiplication gives X²=(c²+ab)I, hence X^P=Q^((P-1)/2)X for P odd. Partition triples by common t-adic order v. For primitive length r=m-v, the smooth nonzero cone c²+ab=0 mod t has q²−1 points and exactly q² lifts per new precision, so number satisfying Q=0 mod t^h is (q²−1)q^(3r-h-2). For Pv>=m count ideal t^ceil(m/P) triples; otherwise h_v=ceil(2(m-Pv)/(P-1)) gives exact kernel count. Reduction mod t identifies nilpotents and total q^(3m-1). Primitive Q=t witnesses maximal height, and geometric bounds on low-P kernel fraction establish concentration at logarithmic scale. Original finite source enumerates six small prime truncations; separate independent checks enumerated q=3,m<=3 and q=5,m<=2; no finite proof of all q,m.

## originality

PASS

Chaffe–Topley arXiv:2311.08208v2 Proposition 3.4 identifies eventually restricted-nilpotent elements by nilpotence of the constant term over algebraically closed base; it does not give the sizes of each power kernel or their height laws. This work specializes to finite q and quantitatively refines the nilpotent locus. Classical smooth quadratic lifting is used as a known ingredient. General jet-scheme/orbit-counting literature could implicitly contain the explicit formula, so historical priority is not certified.

## value

PASS

The restricted nilpotency filtration is canonical in modular Lie theory, and the exact kernel sizes and height distribution distinguish exceptional highest layers from typical logarithmic behavior in a family of growing local rings. This is a natural complete distribution, not a one-off finite count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
