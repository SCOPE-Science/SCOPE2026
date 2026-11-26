---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In counting normalization the Weyl basis has squared HS norm N=q². Expanding gg* and summing the orthogonal conjugation characters over N² group elements yields eigenvalues N|A_g|². Nonzero vertical shifts are always absent. For each nonzero horizontal shift a planar derivative gives exactly one graph overlap, and a nonplanar derivative omits a value, killing an entire required row. The dimension is q² times q(q−1)+1 allowed shifts. For the extremal bound, let a≤b be the two least masses and t=1/(q+1). If ab<t² a singleton overlap forces ambiguity below t. Otherwise concentrate the excess over b in a single mass; the upper bound on the squared-mass sum decreases with b up to (1−a)/(q−1). Substituting b=max(a,t²/a) gives at most (q+3)t² for a≥t, with equality only at a=b=t and all excess in one site. For a<t the feasible z=a/t starts at the lower root z0 of P(z)=z²−(q+1)z+q−1. The scaled deficit factors as (z−1)Bq(z); the identity Bq=2(z+1)P+(q−1)((q+2)z−q), P(q/(q+2))>0 below the root, and Bq′(z)≥q(q−3)>0 on [0,1] give strict negativity there. Parseval in the horizontal zero-shift frequency row now forces some ambiguity at most t, and equality forces the single doubled mass. For that window the other zero-shift frequencies have ambiguity at least t(√q−1)>t, by cancellation of every nonzero derivative term in the squared planar character sum, while the horizontal row achieves t and the zero coordinate achieves 1. Phases do not change magnitudes of zero-shift coefficients or singleton overlaps. This proves the frame-operator and squared-root analysis-map condition numbers and the claimed extremal eigenvalues for every stated q. Read check_algebra.py, check_planar.py and VERIFICATION.md without execution. The recorded auxiliary dimension-nine full Gram check is not implemented in the supplied scripts and is not relied upon; the Weyl calculation proves the normalization.

## originality

PASS

Pass for the sharp weighted minimax on the fixed accessible space and its full equality classification. Weyl diagonalization, the planar relative-difference-set geometry and the uniform indicator spectrum are known ingredients, not independent originality claims. The strongest inspected matches do not cover the joint optimization of planar singleton products and the zero-translation modulation row.

## value

PASS

Fixed maximal operator-space conditioning is a natural quantitative inverse-problem criterion: injectivity alone does not tell how a graph-supported window amplifies error. The exact q+1 analysis condition number and uniquely determined nonuniform amplitude pattern show how to remove the uniform window's extra null directions at optimal cost, uniformly over planar functions, with all phases free. This is an exact design result, not a claim of full-state tomography.

The dated certificate retains the supplied scientific assessment, sources and limitations.
