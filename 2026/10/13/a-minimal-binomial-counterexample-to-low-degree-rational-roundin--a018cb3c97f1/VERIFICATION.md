---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The pushforward of Bin(3,p) under 0,1,2,3→0,1,3,4 gives PGF a0+a1 z+a3 z^3+a4 z^4 with a2=0, all other coefficients positive. If any factor has degree 2 with positive leading coefficient, its positive constant gives a forbidden z^2 term. Exactly one nontrivial factor has a positive linear coefficient, and any other cannot have z or z^2 support; total degree 4 with every factor degree<=3 forces factors C(1+uz)(1+vz^3). Such factors give a0 a4=a1 a3. Actual binomial coefficients give a1 a3=9 a0 a4 for all 0<p<1. Independently calculated exact p=1/3: a0a4=8/729, a1a3=8/81, ratio9. n<=2 trivially one bounded variable. Correct original exact coefficient proof is valid, not a numerical-root heuristic.

## originality

PASS

Conjecture 4.8 is explicitly printed by Tang--Tang following a positive j=2 result and general P_3/Q_3 incomparability. That ambient incomparability does not establish a counterexample within the restricted rounded strongly-Rayleigh class. The present minimal binomial example tests exactly the conjecture, with a uniform-in-p obstruction. Earlier unpublished Liggett material cited by Tang--Tang remains unavailable and a residual priority risk.

## value

PASS

An explicit unconditional counterexample to a published universal probability-factorization conjecture at the first new numerator j=3 with the smallest possible binomial trial size is mathematically decisive, even though the proof is short. It distinguishes ambient nonnegative-PGF factorization failures from the conjecture's rounded-strongly-Rayleigh subclass and maps the sharp earliest failure boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
