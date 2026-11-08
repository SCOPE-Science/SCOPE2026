---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The intended notation is A=1+r (multiplicity m), S=1−r−2r² (multiplicity m−1), r=1/(q−1). Conditioning on the hub, petal colors are independent ordered distinct draws from q−1 remaining colors. Direct character orthogonality yields hub-petal and same-triangle correlation −r, different-triangle r², separating antisymmetric petal, zero-sum symmetric petal, and 2D hub/global-petal sectors. The 2D block [[1,−sqrt(2m)r],[−sqrt(2m)r,1−r+2(m−1)r²]] has determinant S, proving μ± and all multiplicities. q=3 gives S=μ−=0, one relation per triangle and frequency; for q>=4 positivity and extreme eigenvalues μ± imply μ+²/S~4m²r^4/S. The independent color enumeration and Gram Fourier spectra agree for 14 frequency bands.

## originality

PASS

The chromatic polynomial q((q−1)(q−2))^m and windmill graph structure are known, and a conditional Potts correlation calculation is elementary. The complete Gram eigenspectrum, exact q=3 rank boundary and q>=4 condition numbers are not provided in inspected chromatic polynomial extremal works. Risk: older Potts-model covariance eigenvalue results could give an implicit specialization.

## value

PASS

Exact first-order Fourier information and its sharp conditioning for a canonical graph family has natural sampling/theory significance: at minimal q=3 the one-site features become dependent, whereas q>=4 are independent with quadratic squared conditioning. The complete parameter spectrum is a motivated exact finite-invariant family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
