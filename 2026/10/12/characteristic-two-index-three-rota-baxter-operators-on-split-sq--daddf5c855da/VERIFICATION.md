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

Let A=k1⊕V, V²=0 and k be any char-two field. For a weight-zero k-linear Rota–Baxter operator P, use x=y=1 to force the scalar part of P(1) to vanish, and x,y∈V to force any scalar functional part P|_V→k to vanish. Write P(1)=v∈V and P(u)=T(u)∈V. The (1,u) identity becomes T²u=0 and in characteristic two (1,1) gives no constraint on T(v); conversely P(a+u)=av+Tu with T²=0 satisfies the bilinear RB identity for arbitrary v. Thus P³(1)=T²v=0 and P²(1)=Tv can be nonzero: index 3 is possible for rank(T)>=1, while char-zero Farooq requires Tv=0. Classify T²=0 up to GL(V) by r Jordan 2-blocks and s=n-2r zero blocks. The centralizer acts transitively on v in the four relative positions v=0; imT\{0}; kerT\imT; V\kerT (omit empty types), with orbit sizes 1, q^r-1, q^(n-r)-q^r, q^n-q^(n-r), and rank-r square-zero T count |GL_n|/(q^(r²+2rs)|GL_r||GL_s|). Summing yields 2n+1 orbit types for even n and 2n for odd n. Independent complete F2 rank/square-zero matrix counts for n=1,2,3 are (2,0),(16,6),(176,84) operators/index-3, corroboration only.

## originality

PASS

Farooq arXiv:2605.15670v1 Theorem 3.4 treats the identical algebra but assumes characteristic zero and imposes both T²=0 and Tv=0; its proof visibly divides by 2. Hence it cannot imply the char-two index-3 stratum or unconstrained v orbits. The 2014 Guo/Rosenkranz/Zheng semigroup Rota–Baxter classification concerns a different object and characteristic. Resultary has a finite-field four-dimensional exterior algebra classification, but that exterior algebra is not the square-zero local A=k⊕V with V²=0; no stronger matching full orbit census was found. Risk: an unindexed positive-characteristic classification of split local square-zero algebra might exist.

## value

PASS

The characteristic jump in nilpotence index on the SAME natural square-zero local algebra is a structural boundary of a known theorem, not an arbitrary change of coefficient field. Exact general-q rank strata, orbit numbers, and sizes provide full classification for every radical dimension, locating the mechanism Tv≠0 and giving a natural refinement with potential reuse in modular operator theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
