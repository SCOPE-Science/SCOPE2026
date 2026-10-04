---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

Run `python3 verify.py`. A successful replay prints `VERIFY_OK` and the rational thresholds used in the proof.

The verifier performs decision arithmetic with `fractions.Fraction`. Square-root enclosures are dyadic and checked by integer squaring. Base-two logarithms are reduced to \([1,2]\) and enclosed using
\[
\ln x=2\sum_{k\ge0}\frac{z^{2k+1}}{2k+1},\qquad z=\frac{x-1}{x+1},
\]
with a positive explicit remainder bound. It verifies: both endpoint purified distances are below \(178/10^6\); the resulting dimension-eight entropy-continuity penalty is below \(297363/10^8\); the regularized upper interpolation at the left endpoint is below \(966531/10^6\); the interpolation derivative is below \(-8\) throughout the interval; and the resulting uniform gap exceeds \(49537/10^8\) bit.

The verifier does not reproduce the primary source's global purification certificate. The external theorem \(E_P(W(1/200))>97/100\) and its endpoint witness are literature premises inspected in the cited primary source and its public reproduction note. The new proof establishes how those certified margins propagate across the stated interval.
