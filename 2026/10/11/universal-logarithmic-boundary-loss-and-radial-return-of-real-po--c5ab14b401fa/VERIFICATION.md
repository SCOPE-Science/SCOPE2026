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

# Verification of the real Poisson boundary-loss theorem

The proof's essential nonstandard input is the real sharp-norm identity in Kovalev's Proposition 2.1. This identity is checked by reconstructing its conformal-strip subordination argument, rather than treating numerical maximization as proof. The remaining asymptotic is proved directly: the region \(0<x<a\) contributes \(O(a)\), Taylor's remainder is bounded by the exact integral \(a\sqrt{1-a^2}\), and the main kernel integral is \(\log((1+\sqrt{1-a^2})/a)\). These facts give the \(4/\pi^2\) coefficient after taking the \(p\)-th root, then dividing by \(r\).

Execute `python3 verify_poisson_boundary.py` using Python 3 (standard library only). The packaged script was run successfully and printed `OK: 12 finite consistency checks; proof needed for all-r/all-p theorem`. The checks compare direct angular quadrature with a distinct Fourier-Parseval formula for \(p=2\), confirm opposite small- and large-radius regimes at two supercritical finite exponents, and compare finite-scale normalized deficits against the analytically predicted \(4p/\pi^2\) angular-moment coefficient.

The finite tests do not certify the infinite limiting claim, exclude intermediate additional crossing radii, establish a sharp finite threshold, or replace a complete primary-literature comparison. The proof covers each finite \(p\ge1\) but is not uniform over unbounded \(p\). No independent audit has been performed.
