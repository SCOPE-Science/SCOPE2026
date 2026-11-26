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

For a fixed final type the t−1 prefix is an onto word on m=q−1 labels and its singleton count is S−1. Counting it by the exponential series z for a singleton and F=e^z−1−z for a nonsingleton gives the displayed kernel; the full mass multiplies each row by q^(1−t). The consecutive coefficients of F are log-concave, preserved by convolution because the Toeplitz order-two nonnegative minors are preserved by Cauchy–Binet on finite truncations. For the adjacent column pair, a term u_(ℓ−a)/u_(ℓ−1) is zero until the numerator support begins and afterwards is a product of inverse successive ratios, increasing weakly with ℓ. Its weighted reciprocal is therefore decreasing weakly. To pass from adjacent columns to any minor, if the left product is positive then neither row is the singleton-support row ℓ=m; the support for ℓ>m is [max(0,2m−ℓ),m−1] and expands to the left, so both rows are positive across the full compared interval. Multiply the adjacent-column inequalities. When the left product is zero there is nothing to show; in particular q=2 is handled. For the credited covariance identity, deleting a specified singleton that is not final gives an onto word on q−2 labels with length plus one possible insertions. Differentiating its generating function and the usual waiting-time PGF yields the stated moments, including the empty-word case q=2. The repaired result rechecks the discrete all-times theorem, not a fixed-time or continuous-time analogue.

## originality

PASS

PASS only the repaired distinct claim, the discrete reverse-TP2 ordering. Myers–Wilf already give the exact joint mass and Resultary 095ece1fb7b6 explicitly gives the same covariance under the same uniform parameters, so the covariance is now credited and retained only as context. The closest stronger-looking conditional result uses a different, Poissonized conditioning variable and does not give the discrete minors.

## value

PASS

The repair supplies uniform likelihood-ratio comparisons of the entire stopped singleton distribution for arbitrary discrete completion times, including support changes. This is stronger than a covariance sign or mean monotonicity and is a natural comparison for what singleton counts say about when a coupon collection completed. The useful contribution survives without the already recorded moment identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
