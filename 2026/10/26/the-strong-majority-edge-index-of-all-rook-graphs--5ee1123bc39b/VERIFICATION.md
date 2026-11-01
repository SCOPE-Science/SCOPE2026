---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For rook R_{m,n}=K_m square K_n, 2<=m<=n, degree d=m+n-2. In a two-colour strong-majority edge colouring each edge sees exactly d-1 of each colour among 2d-2 other incident edges. With r(v) red degree and s(v)=2r(v)-d, red/blue edge sums are +2/-2, giving adjacency eigen-equation A s=(2-d)s for a nonzero vector. Rook adjacency eigenvalues are d,m-2,n-2,-2, so spectral necessity leaves m+n=4 or6; m+n=5 has missing -1 and >=7 has 2-d<-2. At m+n=6, the -2 eigenvectors have row and column sums zero. R_{2,4} column cancellation forces forbidden edge-sum zero; R_{3,3} odd triple of +/-2 row entries cannot sum zero. The only two-colour case is C4=R22 with exactly four named colourings. Independently all 2-colourings of R22,R23,R24,R33 were exhausted (4,0,0,0); explicit 3-colour certificates checked in R23,R24,R33, and for m+n>=7 the published Pękała-Przybyło theorem delta>=5 gives the 3-colour upper bound. Thus Maj=2 iff (2,2), else3, with exact two-colouring multiplicity. No finite enumeration is used for the infinite range.

## originality

PASS

Qualified PASS for exact two-parameter index and absence/count of two-colour colourings. General minimum-degree-five theorem already supplies three colours whenever m+n>=7, so the upper bound is not new; new content is global optimality via a spectral obstruction and degree-3/4 sharp boundary. Resultary published complete-graph strong-majority index concerns K_n, not rook K_m square K_n. The separate recent majority C-colouring of Cartesian products colours VERTICES and is not the same invariant.

## value

PASS

The exact strong-majority edge index of the natural two-parameter lattice/rook graph family is a mathematically motivated class classification. The spectral obstruction distinguishes two from three colours over all parameters and the explicit degree-four boundary demonstrates meaningful behavior outside the general sufficiency theorem. The exact two-colouring multiplicity is also determined.

The dated certificate retains the supplied scientific assessment, sources and limitations.
