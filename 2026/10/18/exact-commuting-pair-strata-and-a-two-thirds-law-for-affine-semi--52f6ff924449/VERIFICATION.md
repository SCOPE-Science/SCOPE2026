---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The frozen proof uses r=rank(A+I), not rank(A-I). Coefficient comparison gives AB=I, A²+B=0 and (A+I)c=0. Hence B=A^(-1), A³=-I and A-A^(-1)=A(A+I); for each first input there are q^(n-r) commuting second inputs. The translation multiplicity is independently q^(n-r), and distinct coefficient triples are distinct labelled operations. Off characteristic three the cube polynomial is squarefree with either three linear factors or one linear and one irreducible quadratic factor. In characteristic three, Jordan columns are n-r,c2,c3; c2+c3=r and balancing them is feasible precisely when ceil(r/2)≤n-r. Invertible centralizer weights give the three strata including r=0 and the smallest dimensions. In all regimes the uniform bounded product factors and summable Gaussian imbalance factor yield H(r) comparable to q^(S_n-3(r-r_n)^2/2), including near the characteristic-three rank ceiling. An admissible rank within one of r_n gives the matching normalization lower bound. On |r-r_n|≥t one can factor out q^(-t²) and retain a summable q^(-(r-r_n)^2/2). Completing the square for the extra weight q^(-r) gives the mean order q^(-2n/3), at fixed q. A separate bounded replay matched 13 exhaustive matrix-stratum cases over q=2,3,4,5,7,9, and directly tested every allowed translation and ordered input pair in seven small cases. The replay is finite; the general proof uses the centralizer formula and estimates above.

## originality

PASS

Credit is limited to the commuting-rank distribution of uniformly sampled labelled affine semisymmetric operations and its fixed-field mean and concentration across all three regimes. The semisymmetric linear coefficient identity and matrix-class counts are prior tools. The inspected quasigroup and affine Lie-algebra results do not give this conditioned distribution or the two-thirds law.

## value

PASS

The labelled distribution answers a different question from which commuting counts are possible. Identity constraints and the translation weights give distinct finite-dimensional strata across the three field regimes, yet the mean and typical rank obey the same exponent law, even where characteristic three truncates the upper tail. This is a quantitative description of a natural structured ensemble rather than an unweighted list of matrix classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
