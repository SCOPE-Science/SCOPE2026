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

Character orthogonality gives J=S/[q(sum |f|²)³], so at 1 the denominator is q⁴. Translation by s/3 reduces the fiber to a binary form of discriminant square class −3, giving N=q−κ+qκ·1_{t=s²/3} and S(1)=q²(q²+q−1). For any real mean-zero h, fixing one coordinate gives L=3Σ_a h(a)χ(D_a); the character Gram matrix has diagonal q(q−1) and vanishing off-diagonal because D_a−D_b runs through the entire field as s varies for a≠b. Thus ΣL²=9q(q−1)Σh². Fixing an ordered pair gives the N-summed curve weights q² on the diagonal and q(q+1) off it, since the residual conic equation has 1 and 1+κ roots, respectively. Hence ΣNQ=−3qΣh². In the real and imaginary directions the numerator's quadratic terms are ΣL²±2ΣNQ; the energy normalization additionally subtracts 3S(1)Σh²/q. Dividing by q⁴ and converting to normalized L² yields the two stated deficit half-Hessian bands. The first variation vanishes at the extremum; conjugation eliminates mixed terms and scaling eliminates the complex constants. A fixed-field uniform Taylor remainder on the slice with mean one gives the sharp local limit, attained asymptotically in imaginary mean-zero directions. Theorem 1.3 and its two cases in §6 verify the imported global bound. At RESULT.md:18 'quadratic-character' denotes the additive chirps defined at line 81, not a multiplicative quadratic character. RESULT.md:23–81 is the all-field replay; the supplied script tests exact counts in five fields but does not implement the separately reported Fourier diagnostics, and it was inspected rather than executed here.

## originality

PASS

The global constant and extremizing symmetries are prior. The supported distinction is the exact normalized second variation and optimal transverse coefficient for all characteristic greater than three. The closest exact formula has a disjoint characteristic hypothesis and a different counting argument; none of the compared sources gives broader coverage or a specialization yielding these bands.

## value

PASS

Sharp global control does not quantify near-equality. For the full characteristic-greater-than-three family, this gives the optimal local quadratic coefficient, identifies precisely the weakest directions, and resolves the small but exact 12/q² separation of phase and amplitude curvatures. It is useful fixed-field information independent of any global or uniform-neighborhood stability assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
