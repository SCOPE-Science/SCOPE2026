---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For the five printed decimal rational coefficients treated exactly, Schur inequalities hold for every s>0. When s<=s0=c/d both A,B>=0; when s>=s1=a/b the second iterate is negative. On s0<s<s1, roots p>0 and -q<0 have q>p, and exact starting solution has coefficients (u+q)/(p+q), (p-u)/(p+q), u=e^-s. Every iterate is positive iff u=p, otherwise the dominant alternating mode eventually gives negative parity. Exact matching is F(s)=0. The derivative analysis of H=e^sF’’ with H’’>0 and explicit endpoint/interior signs bounds F to two simple zeros. Independent high-precision root calculations locate 3.70146585514664567398 and 46.340425531914893290594485997229844; the second is ~3.26e-16 below s1 and direct finite iteration there is ill-conditioned, so it was NOT used as a proof. Log ratio of amplitudes proves inverse-linear first-negative index near s0 and logarithmic delay near simple resonance. Bounded numerical checks support but do not replace the derivative sign proof.

## originality

PASS

Li–Lin–Zhang–Zhou Section 3.5 equation (3.20) supplies the exact printed O2CP rational functions and optimizes parareal convergence. Its stated analysis concerns convergence/stability, not all-time scalar positivity with exponential starter or the two matching roots. Hundsdorfer–Ruuth–Spiteri provides general linear multistep monotonicity theory, and the public BDF2 sign-loss record is a different oscillatory-root regime. The particular coefficient-driven two-resonance classification appears distinct, with substantial methodological overlap credited.

## value

PASS

Positivity of uncorrected coarse trajectories is a natural qualitative stability question even for an A-stable optimized propagator. The exact two isolated eigenmode-cancellation parameters and inverse-linear/logarithmic delay laws are sharply motivated information about that published numerical method, with explicit limitation to a scalar exact-start test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
