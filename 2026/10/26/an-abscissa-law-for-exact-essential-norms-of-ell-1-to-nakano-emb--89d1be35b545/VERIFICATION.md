---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Coordinate unit vectors prove ||J||=1. For every finite partition of the coordinates, the positive-series convergence abscissa is the maximum of its pieces, and finite deletions do not change it. If the basis has a finite cover by balls of radius b<1, some center covers an infinite piece at maximum abscissa; coordinates of the center on that set have modulus >1-b, forcing b>exp(s*)/(1+exp(s*)) (or b>=1 if s*=∞). Compact K maps {e_n} into a precompact subset, giving the same essential-norm lower bound. For s*<∞, necessarily p_n→∞, and the finite-rank map K_N x=head(x)+c(sum_tail x_n)1_tail, c=1/(1+exp(s*)), is well defined in the FULL space; for every λ>r*, its column errors have modular at most Σ_{j>N}(c/λ)^{p_j}+sup_{j>N}((1-c)/λ)^{p_j}→0. Since ||T:ℓ1→Y||=sup ||Te_n||, get ||J-K_N||<=λ, giving essential norm, limiting approximation numbers and noncompactness cover radius all exactly r*. For monotone p_n, upper/lower exponential-series comparisons yield s*=limsup(log n)/p_n. Independently checked finite tail estimate for p_n=2n and λ=3/4, but proof is analytic for all sequences (C3_OK).

## originality

PASS

PASS, qualified: Sanchiz 2512.16633 proves qualitative failure of compactness of Nakano inclusions. Kiwerski–Tomaszewski 2212.06723 develops precise multiplier essential norms but the stated general case relies on reflexive source or order-continuous target; ℓ1 is not reflexive and unbounded-p_n full Nakano need not be order continuous. Vuillermot 2610.19745 treats related modular embeddings, but its newly posted full 30-page manuscript was inaccessible; the abstract gives qualitative embedding/compactness, not this exact formula. Stronger full-space noncompactness-radius results remain a concrete risk.

## value

PASS

PASS: This exact invariant answers how far the natural canonical inclusion lies from compact maps, sharply distinguishing the full non-order-continuous Nakano space from its heart. The three independent-looking quantities agree with a quantitative threshold in exponent-series growth. Logarithmic exponent families interpolate between exact values 1 and 1/2. Not a routine restatement of noncompactness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
