---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

After translating the support and dividing out g=gcd(N,a,b), Fourier zeros lift with multiplicity g from the primitive quotient and q can only increase. If 3 divides N, product uncertainty is sharp. If 4 divides N but 3 does not, splitting the trinomial into even/odd exponent parts shows P(z) and P(−z) cannot both vanish, so at most N/2 roots vanish. If q=p≥5 and N is odd, Meshulam gives the claimed lower bound. If N=2m with m odd, the primitive support meets both parity fibers; under Z_N≅Z_2×Z_m, each of the two frequency parities is the Fourier transform of a nonzero ≤3-sparse function on Z_m, giving at most 2m/p zeros each. The support {0,N/q,2N/q} with a quadratic having two prescribed distinct q-th roots realizes exactly 2N/q zeros. Every branch and boundary is therefore proved analytically.

## originality

PASS

Meshulam's interpolation theorem directly supplies some branches of the claimed lower bound but is weaker in the key even regimes; Bonami–Ghobber give equality-case results for restricted group families rather than arbitrary cyclic order. The audited proof adds parity pairing for the q=4 regime and a Z2×Z_m fiber argument for the even q≥5 regime, then supplies a uniform sharp construction. No prior all-N support-three formula or equivalent trinomial-zero theorem was located.

## value

PASS

Exact support three is the first genuinely nontrivial sparse Fourier uncertainty profile beyond one/two-point cases. A sharp formula for every cyclic order, including composite even orders where the generic divisor interpolation is not sharp, is a natural reusable invariant in finite harmonic analysis and sparse-polynomial zero theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
