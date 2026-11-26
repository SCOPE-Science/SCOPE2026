---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Left translating the support preserves rank. Independently, on two cyclic cosets one can pair the Fourier mode j on the rotation coset with mode −j on the other; a acts by opposite phases and b switches cosets, with the return phase (−1)^j. This yields the stated 2×2 symbol, paired again at −j, with fixed modes 0 and n giving the four scalar characters. For even j the determinant condition is the union of congruences n divides (j/2)(r±u), nested because n is dyadic, yielding max(A/2−1,0) eligible singular blocks when A is even and zero when A=1. Both terms of the symbol vanish together exactly when j times each difference is congruent to n mod 2n; common difference valuation t in [1,k−1] gives 2^(t−1) zero blocks. When j is odd, a sum of squared cosines can vanish only for r=u=n, so every odd block then adds its full nullity. The four scalar tests contribute 1, 2, or 3 according to mixed, even/even, or odd/odd parities. For the mean, odd/odd congruence union tails are 2^(2−j) for powers 2^j with j≥2; for halved even differences the union tail is 2^(1−j)−2^(1−2j), before removing both zero axes. Removing those axes and adding the zero-block corrections gives the stated moment. Ordered anchors have exactly four presentations per unordered support. An independent exact characteristic-zero rank calculation checked 617 supports (every normalized r,u,w at n=4 and every r,u at one deterministic offset at n=8), including the two full difference-pair sums 148 and 856.

## originality

PASS

The precise all-support dyadic valuation strata, populations and closed first moment survive the comparison. General Fourier blocks and the extremal rank bound in isolation are standard or elementary. Dicyclic graph singularity is the closest external overlap risk, but the available statement is for finite simple graphs, and its full text was not successfully opened. Neither that scope nor the checked integrality papers gives the complete directed or looped coefficient-one census and its first moment. Closest indexed complete analogues use odd cyclic index or the different generalized-dihedral group law; they do not extend by substitution.

## value

PASS

This is an exact all-scale sparse convolution rank classification, not a repeated singularity test. Every support is singular but asymptotically half lose just one dimension, while a log-growing mean reflects a range of much larger kernels and extremizers have an explicit subgroup geometry. Such distinctions are useful for rank-sensitive filtering and not apparent from the common first scalar zero or integrality criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
