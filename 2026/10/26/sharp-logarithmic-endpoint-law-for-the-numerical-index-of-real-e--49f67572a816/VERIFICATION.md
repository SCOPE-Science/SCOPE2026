---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Import explicitly Chiclana’s exact identity n(ell_p^2(R))=M_p=max_{0<t<1}(t-t^{p-1})/(1+t^p) for p>2. With epsilon=2/p, eta=1-epsilon, t=e^{-2z/p}, the scalar objective becomes sinh(eta z)/cosh z; the stationarity equation tanh(eta z)tanh(z)=eta has a unique solution since the left side increases from 0 to 1, and objective vanishes at either endpoint. In y=t^p the equation epsilon(1+y^{2-epsilon})=(2-epsilon)(y+y^{1-epsilon}) gives y=Theta(epsilon), and expanding y^{1-epsilon}=y exp(-epsilon log y) yields y=epsilon/4+epsilon^2[1+log(epsilon/4)]/8+O(epsilon^3 log^2(1/epsilon)). Substitution with careful cancellation of mixed epsilon*y*log y terms gives n=1-[log(2p)+1]/p+[log^2(2p)+1]/(2p^2)+O(log^3(p)/p^3), and y=1/(2p)+[1-log(2p)]/(2p^2)+O(log^2(p)/p^3). Finite-dimensional duality transfers n to conjugate exponent p/(p-1). Independently evaluated the stationary root at p=100,1000,10000,100000,1000000 using high-precision root finding, tracking normalized remainders; source verify.py uses a separate optimization cross-check but finite numerics are not a proof of the big-O theorem.

## originality

PASS

Chiclana’s primary 2026 result already establishes BOTH the exact scalar numerical-index formula and its hyperbolic optimizer equation. The assigned claim properly imports these, with novelty narrowly confined to the quantitatively sharp logarithmic two-term p-infinity expansion and singular optimizer boundary layer. Merí–Quero and Martín–Merí handle finite-exponent bounds/problems, not the stated endpoint coefficients. This is mathematically a deduction from a known exact identity, but extracting the singular scale and second-order cancellations takes controlled asymptotic analysis not already stated or mechanically immediate without calculation. Historical earlier asymptotics remain a priority risk.

## value

PASS

The numerical index near the non-smooth endpoint of real planar ell_p is a standard operator-theoretic invariant. Explicit logarithmic correction, next-order constant and unique extremizer boundary scale quantify a singular endpoint not described by a generic continuity statement. This is useful precision on a natural parameter limit even without a new finite-p formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
