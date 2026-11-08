---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

From slicing Fubini transform F(u), product (1-e^-z)^n R(z), R(z)=product(z+2pi i k_j)^-1, relies essentially on integer frequencies. Simple poles have sum of residues zero (R(z)=O(z^-n)), so inverse Laplace values h(m) vanish at positive integers, giving zero coefficient for distinct entries. Precisely one double pole at common r contributes A m, where A=product_{j not a,b}(2pi i(k_j-r))^-1, while simple contributions sum to zero; finite binomial convolution gives (-1)^(s-1) binom(n-2,s-1) A, nonzero. Collision hyperplanes k_a=k_b, including those with k_n=0, have (2N+1)^(n-2) integer points each, pairwise intersections O_n(N^(n-3)), yielding leading binom(n,2)(2N)^(n-2) and the uniform-in-s ratio. Independent integer checks of binomial identity and hyperplane counts (n=5,N=2: 240 exactly-one-pair frequencies, n=5,N=3: 1200); inspected check_hypersimplex.py, with direct low-dimensional integration. Higher collisions and uniform joint n,N are deliberately unproved.

## originality

PASS

Xu’s multivariate spline theory and Diaz–Le–Robins general polytope Fourier formulas provide frameworks capable of deriving specialized slice coefficients, but inspected primary statements do not expressly give integer collision-order cancellation with sharp cross-slice support count; this requires a confluent double pole and arrangement combinatorics. Li concerns hypersimplex volume/Ehrhart quantities. Generality is treated as a serious priority caveat, not novelty by unmatched keywords.

## value

PASS

Hypersimplices are natural matroid polytopes and integer cube sections. Across every nontrivial level the generic nonzero integer Fourier modes share codimension-one arrangement support and explicit binomial coefficient rescaling, giving a sharp resonance density with an infinite family of n,s and not just a finite sample. Higher-multiplicity collisions remain unresolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
