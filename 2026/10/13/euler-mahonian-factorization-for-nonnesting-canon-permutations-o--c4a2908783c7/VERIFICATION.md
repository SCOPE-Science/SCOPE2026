---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For each n>=1 and k>=3, occurrence-order rank permutations coincide. The absence of nested a,b,b,a or b,a,a,b subsequences forces for consecutive letters a_i,a_{i+1} the inequalities p_(a_i,k-1)<p_(a_(i+1),1) and p_(a_i,k)<p_(a_(i+1),2), leaving exactly independently swappable adjacent block-boundary pairs. For a base word sigma_1^k...sigma_n^k the only existing descents are at positions ki corresponding to descents of sigma. Each boundary swap increases descent count by one and major index by exactly ki: for ascending a<b introduces descent at ki; for descending a>b replaces descent ki with ki-1 and ki+1. Neighbourhoods are disjoint for k>=3. Summing over B and sigma proves A_n(u,q^k)product(1+u q^(ki)). MacMahon specialization then gives the full multiples-of-k support and palindromicity. Independent exhaustive enumeration of all multiset words (rather than the bundled lattice-word code) for n=2,k=3,4 and n=3,k=3 recovered 4,4,24 admissible words and all bivariate terms. The all-parameter proof is structural; no finite extrapolation.

## originality

PASS

Laudone Proposition 5.3 already proves the same nonnesting class has size n!2^(n-1) and gives the independent binary boundary choices; that entire structural normal form is prior and explicitly excluded from novelty. Laudone Section 5.1 studies descent polynomials for other canon avoidance classes and cites Elizalde for unrestricted canon descent statistics. The inspected Laudone text contains no major-index statement and does not spell out the joint descent/major-index factorization for this nonnesting class. Additional information needed is the position-sensitive two-descent transformation at descending boundaries. The retained claim is this joint two-variable all-n/k generating function; priority remains best-of-knowledge due possible independently derived refinement.

## value

PASS

The natural Euler–Mahonian refinement of a canonical pattern-avoidance class resolves the complete joint (des,maj) distribution, not just its already-known cardinality or a scalar descent polynomial. The exact q^k factorization, full major-index support and palindromicity are useful enumerative facts for further comparison and statistics; they have stronger mathematical motivation than merely reprinting the earlier count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
