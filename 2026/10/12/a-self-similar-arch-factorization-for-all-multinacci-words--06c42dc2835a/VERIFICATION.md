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

PASS: Reconstructed sigma_m^h(0): for h<m, length 2^h and a unique terminal h, then Q_j=sigma_m^(m-1)(j) is concatenation of lower-index sigma_m^h(0) avoiding letter m-1 with length 2^(m-1)-2^(j-1). Expanding sigma_m^m(x) exactly gives x=P B_{x0}B_{x1}..., each block has all m letters only upon its unique terminal m-1 and so is a shortest greedy arch. The standard arch-subsequence theorem gives U_m(N)=the rare-letter prefix count at every N, not only special substitution boundaries. Letter preimage equations give U_m(L_n)=L_(n-m), while primitive incidence matrix equations lambda f0=1,lambda f_j=f_(j-1) give f_(m-1)=lambda^-m and arch frequencies lambda^-(j+1). Independent regeneration of substitution words for m=2..7 over 30,000-symbol prefixes matched arch endpoints to rare-letter positions and verified first 2000 coded gaps; finite tests only corroborate the all-m morphism argument.

## originality

PASS

PASS (best knowledge): The general greedy arch characterization is prior work, and episturmian return-word theory already provides abstract return-word decomposition and derived-word coding. Having inspected Justin–Vuillon Theorem 4.4 and its corollaries in full, its palindromic-prefix return-word result does not itself assert the complete every-prefix scattered-subsequence universality identity for this particular multinacci substitution, nor calculate all exact arch lengths and frequencies. The specific algebraic identification is the assessable original content; priority for isolated gap lengths remains a risk.

## value

PASS

PASS: The multinacci word is a canonical family of recurrent morphic words, and exact scattered-subsequence universality of EVERY finite prefix is a natural complexity statistic. The self-similar decomposition does more than list gap lengths: it codes the entire infinite fixed point, recovers exact morphic-prefix counts, and yields a density. This is a motivated structural theorem rather than a recomputed finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
