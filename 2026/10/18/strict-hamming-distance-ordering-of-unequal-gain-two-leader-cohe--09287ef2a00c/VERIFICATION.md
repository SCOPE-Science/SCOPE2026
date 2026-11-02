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

From frozen RESULT.md, the two-column determinant lemma for (L+zI)^-1 with 1/(Nz) pole yields tr(M^-1)=2Ng+[N(1-ab B^2)-2ab C]/[a+b+2ab B]. Walsh eigenvalues 2j and odd-intersection character counts produce the stated binomial B,C,g. Product cube heat kernel 2^-d(1+e^-2t)^(d-k)(1-e^-2t)^k is strictly decreasing in k at every t>0, so B and C strictly increase. The potential w=L^+(e_u-e_v) solves Lw=e_u-e_v, is harmonic off u,v and satisfies w_u=B,w_v=-B. Connected discrete maximum principle gives |w_x|<B at other x, whence 2C=||w||^2<NB^2. At fixed C, derivative in B is -2ab[N(1+(a+b)B+ab B^2)-2ab C]/(a+b+2ab B)^2<0 and derivative in C is -2ab/(a+b+2ab B)<0. Thus all adjacent Hamming classes strictly improve for all independent a,b>0. The last-distance heat-kernel beta integrals give Delta B=1/(Nd), Delta C=H_d/(2Nd); expansion a=eps alpha,b=eps beta yields the exact finite penalty. Independent exact-rational checker verified 256 spectral-order and small direct-matrix identity comparisons for d=2..11 and four gains, plus all-endpoint and maximum-principle inequalities; reconstructed all seven Git blob entries into the assigned tree hash. Finite checks are corroboration; the above analytic argument proves the unrestricted quantifiers.

## originality

PASS

Qualified best-of-knowledge. The oldest exact-model source Fitch–Leonard fixes a COMMON leader gain (arXiv:1407.1569, section II and Theorem 2) and establishes antipodal optimality for cycles and maximum resistance for equally central vertices (Corollary 2). The later resistance-network treatment permits variable gains in a general representation but explicitly restricts its multi-leader solved classes to unit gains, paths/cycles/trees (arXiv:1708.06873, p.4 and Theorem 15). These antecedents do not prove strict ordering of EVERY Hamming separation for two arbitrary independent finite gains, nor the exact weak-gain last-bit gap. No equivalent covering theorem was identified in fresh mathematical search or Resultary; this is a qualified priority assessment, not a novelty certificate.

## value

PASS

The target is a natural control-design optimization: robustly placing two asymmetrically weighted leaders on an infinite high-dimensional product graph to minimize stationary isotropic-noise error. A strict complete distance preference ordering independent of both gain ratio and scale is more informative than the prior common-gain farthest-pair optimum. The explicit nonzero weak-gain near-antipodal regret gives sharp sensitivity to a one-coordinate placement error despite individual trace divergences. Neither ranking nor precise asymptotic is a routine renaming of existing equal-gain results, and both can inform network placement and benchmark more general graph classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
