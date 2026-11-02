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

Reconstructed the circular-Gaussian Laguerre expansion Cov(log|X|,log|Y|)=Li_2(q)/4. Jensen radial differentiation yields the exact convergent Bessel series rs Σ_k exp[-k(r²+s²)] [2rs I0(2krs)-(r²+s²)I1(2krs)]. For r=R+a,s=R+b, asymptotics for scaled I0,I1 produce the stated Li_{3/2}-2d²Li_{1/2} function with O_A(R^-1) normalized error, including d=0 by a summable k^-3/2 diagonal term and bounded d²Li_{1/2}. Write x=d²; g(x)=Li_{3/2}(e^-x)-2xLi_{1/2}(e^-x), g'(x)=-3Li_{1/2}+2xLi_{-1/2}. Tilting a geometric law by decreasing k^-1/2 bounds Li_{-1/2}/Li_{1/2}≤(1-e^-x)^-1, proving strict decrease through x=1/2; for x≥1/2 each term of Σ e^-kx k^-3/2(1-2kx) is negative. Exactly one root follows; 9 independent mpmath finite-radius and sign diagnostics passed, not the universal proof.

## originality

PASS

Kiro–Nishry (2021) Theorem 1.4 gives the single-circle asymptotic variance, including the same ζ(3/2)/(4√π) coefficient, while its Appendix A derives one-disk zero-count formulas. Buckley–Sodin (2017) addresses argument-increment covariances on fixed curves under homothetic dilation; its stated fixed-curve limit does not automatically give a two-curve family whose separation shrinks on the scaled geometry as 1/R. Existing planar GEF two-point correlation functions can in principle be integrated to recover finite two-disk covariances. No primary statement actually inspected establishes the moving-radius Li-polylog crossover with rigorously unique sign threshold. This is best-of-knowledge, not a declaration that such an implicit calculation cannot be in older literature.

## value

PASS

Negative correlation of zero counts in nested disks is a nonobvious structural phenomenon of a canonical hyperuniform point process. The full continuous crossover function, its one rigorous threshold, and diagonal consistency provide a naturally motivated exact two-scale statistical invariant useful for studying fluctuations of expanding windows; it is not a small arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
