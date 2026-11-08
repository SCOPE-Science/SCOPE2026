---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For the specified five-step BDFL coefficients and exactly 4 backward-Euler starts q(r)^j, the characteristic polynomial F_r(z) obeys the exact factorization F_r(q(r))=r^2(sqrt5−3)(7−sqrt5)(r−sqrt5)(r^2+(5+3sqrt5)/2)/[176(1+r)^5]. It vanishes for positive r only at sqrt5, making y_n=t0^n >0 at resonance. An independently checked quartic factor at r0 has simple conjugate pairs of moduli approximately 0.4985061885 and 0.3490165002, both >t0=(sqrt5−1)/4. Rational Rouché disk certificates establish separation and first-pair argument close to pi/2; Vandermonde modal coefficients have dominant complex amplitude proportional to (r−r0), yielding infinitely many positive/negative terms and N_negative=log(1/|r−r0|)/log(rho0/t0)+O(1). Independent SymPy factored F_r(q) and located roots; finite numeric recurrence supports but does not prove infinite signs.

## originality

PASS

Jensen–Ketcheson–Lóczi introduce this five-step L-stable method and study accuracy, L-stability, and TR-BDF2 starts, not proven by accessible abstract to cover the present backward-Euler-starter positivity resonance. Related exact delayed-sign-loss BDF2 Resultary finding concerns a different two-step recurrence and square-root rather than logarithmic detuning delay. Best-of-knowledge O PASS with explicit substantial risk because source arXiv full PDF and OA inaccessible and authorized Oxford download blocked (vpn_disconnected); no whole-document noncoverage inference.

## value

PASS

An exact isolated all-time positive orbit embedded inside a stable method with nearby eventually oscillating trajectories, and sharp logarithmic sign onset, is a meaningful rare resonance/boundary for numerical positivity diagnostics, beyond a routine stability root computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
