---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The theorem concerns each n>=3 and arbitrary ordered k>=0 including repetitions. Every extensive isotone idempotent endomap has exactly the A_S, B_i, C normal forms: if f(0)=0, each atom maps to itself/top; if f(0)=top then f=C; if f(0)=a_i, monotonicity and idempotence enforce B_i. Compositions yield A_S A_T=A_(S cap T), B_i B_j=C for i≠j, C absorbing, and A_S B_i=B_i A_S=B_i exactly for i in S; otherwise A_S B_i=C but B_i A_S(0)=a_i, so they do not commute. Every commuting collection is contained in F_J for its occurring B_i, and F_J is maximal against any outside B_i (excluded by A_J) or A_S (excluded by B_j for omitted j in J). Therefore 2^n maximal families, sizes 2^(n-|J|)+|J|+1, all closed under composition. For an ordered k-tuple, fix the exactly occurring B-set J, force each B_j at least once and all A_S to contain J; inclusion-exclusion produces the given sum and EGF. For k=0 only J=empty contributes 1; k=2 yields 4^n+(n+2)2^n+(n+1)^2. Independent from-scratch enumeration of the original order axioms and composition graph for n=3,4,5 recovered 2^n maximal families and k=0,1,2,3,4 tuple counts (n=3: 1,12,120,1080,9240; n=4: 1,21,377,6237,100337; n=5: 1,38,1284,41192,1306896). These tests corroborate, not prove, the unbounded formulas.

## originality

PASS

Glück has already established the individual closure-map classification and 2^n+n+1 diamond count; neither is claimed as new. The additional commutation criterion, 2^n maximal commuting families, their sizes, and all-arity tuple enumeration are not consequences of that unrefined count. The inspected general monotone-operator fixed-point work assumes commuting operators without classifying which pairs commute. The modal-multilattice logic paper concerns a different algebraic semantics. This is a qualified best-of-knowledge comparison, not a priority certification. Independent priority check read the full relevant primary sections of Glück (2024), two Cousot (1979) papers, and both specifically compared Resultary published mathematical statements. Best-of-knowledge PASS with explicit unknown unindexed semigroup risk.

## value

PASS

The mathematical problem is natural: a set of idempotent extensive monotone operators can be applied in any order without changing the composite precisely when the operators pairwise commute. The diamond M_n is the simplest natural nondistributive lattice family of unbounded width. This theorem resolves its complete compatibility graph maximal-clique structure and counts all ordered commuting tuples for arbitrary k with repetitions, a genuinely structural and useful infinite-parameter invariant beyond the known isolated closure count. There is no claim of a general finite-lattice classification or downstream application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
