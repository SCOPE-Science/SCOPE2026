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

Put T=X+1, so the cyclic module is R=F2[T]/(T^n). The block update has determinant one. For even augmentation M-I=cD with D=[[0,1],[1,c]] invertible; in characteristic two M^(2^j)-I=c^(2^j)D^(2^j). For odd augmentation the reduction has order three, and M^d-I is invertible whenever 3 does not divide d. Cayley–Hamilton gives M^3-I=(c+1)^2 M(M+I), with M and M+I units, so the corresponding scalar valuation doubles before the successive squarings. A scalar T^h has kernel dimension min(n,h) on each of the two copies of R. This proves Q_j, and first saturation determines the 2-part of the order; reduction forces the odd part to be three in the odd case. Subtraction along the divisor chains gives exactly the primitive counts, with the zero orbit separate in the odd case. This covers c=0 and c=1 with the stipulated truncated valuation. The n=16 example has v=2 at both graph degrees: the second-step summand starts at valuation four. Its first fixed counts are 16, 256, and 65536, giving the stated counts. Independently walked all states of the eight n=4 symmetric circulants using two binary shears, corroborating, for example, cycle counts (16 fixed,120 length-two) at c=X+X^3 and (1 fixed,85 length-three) when a loop is added. The frozen verifier was inspected, not run; its small-state walks test admissible lengths, and its rank tests yield the corresponding cycle counts by subtraction. The universal proof, not the diagnostics, establishes the result.

## originality

PASS

The construction and matrix recurrence are prior, and exact binary nearest-neighbor spectra are materially covered by other indexed records. The surviving distinct claim is the uniform exact all-state spectrum for every symmetric binary circulant at dyadic size and its dependence on only augmentation and one valuation, including both parity classes. No retrieved comparison gave or mechanically determined that uniform valuation reduction to the best of current knowledge.

## value

PASS

The result computes the complete temporal spectrum of a natural family of linear dynamical systems from a local invariant, not just the matrix's period or a single small census. It identifies graph couplings of different degrees with provably indistinguishable binary dynamics at the level of cycle counts and separates the even and odd period classes. The use of standard local algebra and divisor-chain subtraction does not remove the benefit of a uniform all-coupling classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
