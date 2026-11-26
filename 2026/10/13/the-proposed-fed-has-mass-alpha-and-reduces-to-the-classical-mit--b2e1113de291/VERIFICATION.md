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

Publisher Eqs. (6.17) and (6.20) print the same extra α in the density and in the tail integrand, but (6.20) equates its tail to E_α(−λx^α). For x>0, differentiating the entire Mittag–Leffler series after composition and cancelling αk using Γ(αk+1)=αkΓ(αk) gives f_pub=−α(d/dx)E_α(−λx^α). The boundary values at zero and infinity are 1 and 0 for 0<α≤1, so the total mass is α and the printed density's tail integral is αE_α(−λx^α). Removing α is the unique multiplicative normalization, and rescaling y=λ^(1/α)x identifies the nonnegative classical density. Equation (6.19) really does use the upper endpoint α; it is not the raw moment stated there. With the positive power-law tail in (6.22), the tail-integral formula for r>0 converges at zero and converges at infinity exactly for r<α when 0<α<1; equality diverges logarithmically. No positive integer moment is finite there. Finite lower-order fractional moments are possible and should not be confused with integer moments. At α=1 the density is correctly exponential and has all positive moments, although the finite endpoint in (6.19) would still be inappropriate. Removing the erroneous factor in (6.25) subtracts n log α, not a parameter-independent constant. VERIFICATION.md and verify_fed.py were inspected, not executed; the latter uses a finite-precision test of truncated series at a point, not an exact coefficient-wise proof, and its tail tolerance is tested on the last loop value. The analytic derivation does not depend on those checks.

## originality

PASS

The repaired law and its standard analytic properties are classical. The supported distinct result is the diagnosis of inconsistent printed formulas and inferential consequences in DOI 10.3934/math.2026395, not the introduction of a distribution.

## value

PASS

Although normalization is elementary here, it changes the status of a proposed law, exposes the classical identity of the repair, distinguishes finite fractional moments from infinite integer moments, and changes the likelihood objective in an estimated parameter. These are substantive consequences for applying the paper's statistical model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
