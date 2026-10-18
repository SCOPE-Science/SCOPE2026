---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Put the rank-r sandwich matrix into block form diag(I_r,0) by invertible changes of bases preserving ordinary rank. An idempotent X block [P B; C D] obeys P^2=P, PB=B, CP=C, D=CB, factors [I;C] P [I B], and has ordinary rank rank(P). For two such idempotents, direct block products give PQ=QP, PE=QB, CQ=FP, with lower-right CE=FB following from those plus idempotence (no missing constraint). Commuting P and Q diagonalize simultaneously into dimensions a,b,c,d of 00,10,01,11 sectors even over char2; there are GL_r/(GL_a GL_b GL_c GL_d) decompositions. Each off-core column and row has b+c+d independently free coordinates, giving q^((m+n-2r)(b+c+d)) lifts. Thus the full U^(b+d)V^(c+d) polynomial is exact; r=0 gives 1, positive m,n and all finite fields are included. Independently evaluated Gaussian multinomial sum: for (m,n,r,q)=(3,3,2,2) individual idempotents=41 and commuting ordered pairs=409; for (3,3,3,2) they are 58 and 1012. Fixing q,r and increasing tau makes rank-r core leading terms yield probability ~K_r(q)q^(-tau r), with coefficient sum over a=0. Finite checks do not replace unrestricted decomposition proof.

## originality

PASS

Best-of-knowledge originality after independent statement/implication comparison, published-record semantic search and relevant primary material inspection. The known premises and residual risks below are credited, not silently treated as novel.

## value

PASS

The matrix sandwich product is a natural semigroup model in which ordinary linear rank and product idempotence differ. The joint rank polynomial of commuting pairs detects simultaneous eigenspace overlap not recoverable from Dolinka-East univariate idempotent counts; its exact off-core lift exponent and asymptotic probability are mathematically meaningful for size comparisons and commutation phenomena. Unlike generic simultaneous diagonalization, the sandwich lifts and rectangular singular cases are essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
