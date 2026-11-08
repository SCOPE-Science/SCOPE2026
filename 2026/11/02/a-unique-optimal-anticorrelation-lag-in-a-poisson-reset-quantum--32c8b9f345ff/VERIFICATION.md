---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For N>=2 independent identical bosons initially in the +a oscillator ground state and reset jointly at rate r after a center quench to -a, conditional position mean is m(t)=a(2cos(omega t)-1). The stationary reset age A is Exp(r). The trace-preserving reset channel T_h(B)=e^{-rh}U_h B U_h†+r Tr(B)∫_0^h e^{-rt} U_t rho0 U_t† dt gives exact distinct-factor ordered quantum-regression covariance C(h)=e^{-rh}Cov(m(A),m(A+h)); it is not two independent stationary samples or a same-particle measurement result. Four exponential-age trigonometric transforms produce C(h)=4a²e^{-rh}[(5q²+2)cos(omega h)+q(2q²-1)sin(omega h)]/[(q²+1)²(q²+4)] with q=r/omega. C(0)>0; the zeros alternate at omega h_k=pi/2+atan(eta(q))+k pi, eta=q(2q²-1)/(5q²+2). The exact derivative eta_prime=(10q⁴+17q²-2)/(5q²+2)² has one positive zero q*=sqrt((3sqrt41-17)/20), distinct from the maximum of C(0) at sqrt((3sqrt21-13)/10). Checked sample first zeros from direct formula and inspected independent integration Monte Carlo checker source, but universal q statement rests on derivative algebra.

## originality

PASS

Qualified PASS. Kulkarni–Majumdar–Sabhapandit (2024/2025) treat the same center-quench Bose gas and stationary equal-time correlations/counting statistics, but not the lagged ordered distinct-factor regression observable with a globally earliest sign-change rate. Frequency-quench bosons, spin reset correlations, and nonreset trapped Bose gas treat different models or time observables. General quantum-reset channel algebra is prior technique, so a general regression identity is not misrepresented as original.

## value

PASS

The model shows strong positive equal-time cross-particle correlation yet a predictable negative lag signal, and identifies the unique reset frequency minimizing the first anticorrelation time. Its optimal q differs quantitatively from the rate maximizing instantaneous covariance; a natural temporal-vs-static design tradeoff and fully specified observable, not a numerical curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
