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

In the incidence algebra, inversion on the nonzero diagonal block B preserves comparable-pair support (diagonal inverse and finite nilpotent expansion). Each elimination coefficient DB⁻¹ or B⁻¹C is supported by a comparable chain, so both eliminating matrices are units in the original algebra. The residual S=E−DB⁻¹C is supported on strict Z-to-Z comparable pairs; a regular such residual satisfies S=S(YS)^h for all h and hence vanishes by radical nilpotence. Conversely, on the reduced matrix diag(B,0), diag(B⁻¹,I) is an invertible witness and transports back. This includes empty blocks. DB⁻¹C has zero diagonal and no forbidden positions, so each strict Z-to-Z entry is uniquely prescribed, with no additional constraints. In the square-zero algebra, a Z-to-Z entry of axa is zero; with all those entries zero, matching the diagonal inverses, assigning diagonal 1 on Z, and cancelling the off-diagonal terms between two nonzero diagonal sites gives the stated unit witness. The count and the uniform chain probabilities follow by multiplying unconstrained coordinates and summing over Z. For the limit the weight ratio factors into q^(κ−k) times F(k)=(n−k)(κ+1)/[(n−κ)(k+1)]. F decreases through 1 at κ. In each outward telescoping product from m, every residual factor is at most 1 except the single factor F(m)=1+O(1/m) on the positive side. Thus exact weights have a phase-uniform Gaussian tail bound, including zero weights off their support. For |t|≤m/2 the sum of log residuals is O((t²+|t|)/m) by the denominator bounds there; multiplying by the theta envelope and absorbing exp(O(t²/m)) in the discrete Gaussian gives summable O(1/m) total error. The complement has exponentially small tails. The denominator is at least the t=0 term, so both the normalized TV estimate and the relative normalization follow. Taking logs in the center equation gives m∼log_q n and the claimed expansion; the inverse center has increments tending to zero and diverges, so all interior phases occur as subsequential limits, with distinct adjacent weight ratios. Inspected frozen scripts and recorded output, not rerun: incidence witnesses are checked by direct finite linear algebra, square-zero witness brute force is limited to 99 elements, and the theta checks are finite numerical diagnostics. The square-zero script uses some nonunit witnesses, so the universal unit assertion is established by the proof, not those tests.

## originality

PASS

Credit the known incidence-algebra factorization and unit regularity, the exact height-at-most-two stratum formula in a distinct indexed record, and the binary summed chain count. The supported distinct contribution is the paired-algebra all-poset law and, most substantially, the fixed-field phase-dependent chain law in TV with a sharp relative normalization. No inspected source supplies this last claim; this is not a priority ruling on the overlap.

## value

PASS

Support-stratum equivalence identifies an invariant that survives changing the radical products, even for chains whose radical nilpotency lengths differ. The quantitative local law then explains why a logarithmically increasing zero count is not accompanied by Gaussian broadening and why a phase-dependent factor remains in the rare-event regularity probability. The combination supplies both a structural comparison and a precise probabilistic consequence, rather than merely recounting binary triangular matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
