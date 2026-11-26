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

Composing d/(|d|+delta) with the fourth-power soft-sign kernel and clearing the positive normalization denominator gives the frozen F exactly. L is strictly increasing from epsilon*delta to infinity, so |F(x)|<|x| for x nonzero and C<=2*epsilon*delta; continuity rules out a positive limit. At the matched step the one-sided radial expansion of L gives (lambda/delta)*x*|x| to leading order. At the critical step the magnitude satisfies r_next=r-(2*lambda/delta)*r^2+O(r^3), so the reciprocal increments tend to 2*lambda/delta and give the asserted limit except for orbits hitting zero. Beyond the frontier, zero has derivative below -1 and the strict radial increase gives a unique symmetric cycle L(a)=C/2. The elasticity q=a*L'(a)/L(a) lies strictly between zero and one: its denominator minus numerator is epsilon^4*delta*(lambda*a+delta)^3. Thus the two-step multiplier is (-1+2*q)^2<1, and inversion of L at zero gives the linear onset coefficient. As delta goes to zero the limiting L is linear off the origin, giving a=t/2 in the limit and q tending to 1; the limiting sign-step map has F_0^2=u on (0,t). This is a local symmetric-cycle statement and a singular branch limit, not a global supercritical basin or an interchangeable time/floor limit. Frozen finite diagnostics were inspected, not executed or used as the proof.

## originality

PASS

The preconditioner, the scalar substitution, and the sign-step limit viewed alone are not the advance. The supported distinct claim is the exact two-floor phase boundary, critical and matched rates, onset and locally attracting cycle with a singular midpoint limit. The strongest apparent earlier scalar flip record drops the normalization floor before applying the soft sign and has different crossing, matched-step and amplitude exponents; neither that relation nor the inspected primary optimization results cover this classification.

## value

PASS

Shows why a modeling floor that might look cosmetic in a normalized optimizer changes the actual critical exponents and long-time dynamics in its simplest deterministic mode. The exact frontier and singular-cycle result provide a benchmark beyond the derivative-at-zero test. This does not establish the behavior of the matrix, stochastic or momentum optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
