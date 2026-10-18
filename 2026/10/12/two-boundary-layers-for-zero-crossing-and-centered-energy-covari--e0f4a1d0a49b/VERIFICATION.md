---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Gaussian integration-by-parts for sign-crossing versus squared linear form yields the exact σ²F_n/(π√(1−ρ²)) projector identity, with P=I−11ᵀ/n. The square-completion formula and geometric sum show F_n(0)=2(n−1)/n>0, F_n(1/2)<0 for n≥7 and F_n(1−ε)>0 to second order. Exact Q_n=2(n²−1)/3 and S_n=(n²−1)(3n²−5n+8)/30 give n²F_n(1−c/n²)→2c²/3−c³/10; bulk and small-correlation asymptotics yield other claims. Sign-bracketing and intermediate value establish root sequences, without asserting uniqueness. Independently recalculated exact n=7,8,9 negative fractions, and numerical convergence checks for n=60,120,240 support but do not prove asymptotics.

## originality

PASS

The Gaussian moment identity and exact finite mixed covariance can already be obtained by combining pre-existing sign/raw-energy and sign/squared-sample-sum moments, hence cannot be claimed new. The specific two-zero sign theorem, sample-length threshold, and two nonuniform asymptotic layers are not in the inspected prior statements. Price–Gaussian integration-by-parts is also standard. Lindgren 1974 full text could not be accessed; this is an explicit residual bibliographic risk, not an automatic originality failure.

## value

PASS

Crossing frequency and mean-centered amplitude dispersion are complementary standard time-series statistics. The proof uncovers competing 1/n and 1/n² dependence boundary layers with distinct constants and a finite threshold n=7, a precise behavior that ordinary covariance identities conceal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
