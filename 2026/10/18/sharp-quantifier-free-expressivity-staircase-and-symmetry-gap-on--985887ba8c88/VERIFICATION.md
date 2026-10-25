---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For any ordered tuple, the equality partition on k coordinates into j blocks and the induced adjacency graph on its j distinct vertices determine the complete parameter-free atomic diagram. On C_n, proper j-subsets induce disjoint unions of r paths with 1<=r<=min(j,n-j), while a full n-subset induces the labeled n-cycle; f_{j,r}=j!/r![z^j](z+z^2/(2(1-z)))^r. Thus T_{n,k}=sum_j S(k,j)a_{n,j}, and any union of atomic types is definable. As n increases, the missing-vertex bound adds strictly positive path-forest strata for n<2k, stabilizing exactly n>=2k (k>=2); least separation arity floor(n/2)+1. For the automorphism orbit count, D_n acts freely on ordered tuples with >=3 distinct entries, while 2-distinct tuples have floor(n/2) distances; Burnside/orbit counting gives O_{n,k}, and for fixed k>=2 this is ~n^{k-1}/2, yielding invariant-vs-definable fraction 2^{-(1/2+o(1))n^{k-1}}. Separate direct induced-graph enumerations n<=9,j<=4, staircase k<=6 and explicit dihedral tuple orbits n<=7,k<=3 all agreed. No extrapolation from tests.

## originality

PASS

Compared this final statement and its strict logical implications against the actual pinned source proof and the named primary prior results. Exact arity-dependent expressive power and sharp inverse distinguishing threshold for a natural family of homogeneous finite structures, plus the superexponentially vanishing quantifier-free fraction of dihedral-invariant relations. Nontrivial combination of graph-induced substructure geometry and model-theoretic definability, rather than just known forest enumeration.

## value

PASS

Exact arity-dependent expressive power and sharp inverse distinguishing threshold for a natural family of homogeneous finite structures, plus the superexponentially vanishing quantifier-free fraction of dihedral-invariant relations. Nontrivial combination of graph-induced substructure geometry and model-theoretic definability, rather than just known forest enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
