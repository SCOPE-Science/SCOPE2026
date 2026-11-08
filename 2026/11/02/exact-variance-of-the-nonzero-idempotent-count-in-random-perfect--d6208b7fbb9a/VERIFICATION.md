---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For uniform A in GL_n(F_q), each fixed nonzero x has P(A x^[2]=x)=1/(q^n-1), so EN=1. Distinct nonzero idempotents cannot be scalar multiples. For linearly independent x,y, their prescribed images occur with probability 1/[(q^n-1)(q^n-q)] exactly when x^[2],y^[2] are independent. In even characteristic Frobenius is a field automorphism and all independent pairs qualify, giving Var N=1. For odd q, a vector with s nonzero coordinates has (q-1)2^{s-1} projectively square-colliding y, including q-1 scalar copies; support summation removes B=(q-1)((2q-1)^n-2q^n+1)/2 pairs and yields Var N=1-B/[(q^n-1)(q^n-q)]. n=1 separately has zero variance. Strict 0<Var<1 and deficit asymptotic (2^{n-1}-1)q^{1-n} at fixed n follow. Inspected finite-field arithmetic and matrix-exhaustion verifier verify_moments.py, including extension-field model; independent small q,n enumerations corroborate without replacing proof.

## originality

PASS

Prior same-model 2026 survey explicitly covers the first moment EN=1; the new statement is a second factorial moment with characteristic-sensitive square-collision defect for every n>=2 and prime-power q. Wei–Zou count algebra isomorphism classes with nonuniform orbit weighting, not the fixed-basis uniform-GL idempotent variance. Full text of same-model survey remained inaccessible, so do not claim whole-document noncoverage.

## value

PASS

Determines an exact second-order fluctuation invariant for a natural finite-field distribution beyond the established mean, including a sharp even-versus-odd characteristic distinction and correct large-field deficit; a plausible target for further factorial moments and distributional questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
