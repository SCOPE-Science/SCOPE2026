---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

PASS: Original 2026 full-text Theorem 4 (constant climate, nonnegative rates d>0, R0>1, interior endemic equilibrium) and unweighted four-variable Volterra W with asserted equation (13) were read, including original PDF page images. Exact admissible Λ=d=1,gamma=2,omega=1,beta=10,Vbar=1,epsilon=4/5,beta0=0,alpha0=1/10,alpha=5,eta=1 gives B0=1/11,R0=34/11>1 and equilibrium x*=(27/50,23/100,23/100,5/9). At interior x=(3/4,1/100,1/20,19/20), independent Fraction substitution gives Wdot=2019503/13851000>0 while eq.(13) RHS=−30854209/1923750<0. Hence (13) fails and *this particular Lyapunov proof* does not prove global stability. It does not demonstrate endemic instability or rule out another global-stability proof.

## originality

PASS

PASS best-of-knowledge: Target source original 31-page full PDF explicitly asserts Wdot<=strictly negative quadratics; no inspected portion or targeted correction/result search acknowledges a positive derivative. General SIR/SEIR Lyapunov and Dulac results treat different equations and do not supply this behavioral counterexample. Resultary exact paper, correction, endemic, Volterra aliases found no same counterexample. Priority remains subject to possible unindexed author notice.

## value

PASS

PASS: A published theorem's sign-definite Volterra bound is essential to a LaSalle global-stability proof and is contradicted by an exact rational point meeting every stated assumption. This reveals an actionable structural gap (behavior-transmission cross terms), not a mere numerical optimization or unsupported assertion that a published conclusion itself is false.

The dated certificate retains the supplied scientific assessment, sources and limitations.
