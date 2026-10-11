---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Fixed-point equality is enough to reconstruct the law. Because X^e has a Lebesgue density, a fixed X is absolutely continuous. With a=E|X|, density equality gives F'=F/a a.e. on (-infinity,0) and F'=(1-F)/a a.e. on (0,infinity). Integrating factors yield F(x)=p e^{x/a} on the negative side and 1-F(x)=(1-p)e^{-x/a} on the positive side; absolute continuity removes a zero atom and enforces the common boundary mass. Conversely the displayed signed-exponential law has E|X|=a and substitution reproduces the same density. Endpoints p=0,1 and p=1/2 are correctly handled.

## originality

PASS

PASS. Capaldo--Di Crescenzo--Navarro's open-access primary article was inspected at the exact generalized-equilibrium definition and surrounding structural results; it defines the same absolute-mean two-sided density but does not state a fixed-point classification. The classical nonnegative equilibrium transform has the exponential as its fixed point, and other arbitrary-support/fractional transforms use different operators. Resultary returned no independent same-transform fixed-point theorem. The submitted common-scale signed-exponential family is therefore not implication-wise covered by the checked prior statements.

## value

PASS

This is a natural complete fixed-point classification for a recently introduced probability transform. It identifies the precise structural freedom created by two-sided support: exponential memorylessness remains in magnitude while an arbitrary independent sign bias survives. Complete fixed-point sets are useful baselines for transform iteration and approximation theory, so the result is more than a cosmetic ODE exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
