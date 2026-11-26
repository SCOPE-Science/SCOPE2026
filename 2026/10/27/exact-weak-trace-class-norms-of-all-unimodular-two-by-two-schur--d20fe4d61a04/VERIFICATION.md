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

Row/column unitary factors and conjugation reduce the symbol to the stated angle with no change of ratio. With F the squared Frobenius norm and u,v the absolute normalized input/output determinants, the identities in (1) follow from the sum and product of the squared singular values. Solving for the two normalized products gives the sum-of-distances constraint with foci uc±iuh (c=cos(δ/2), h=sin(δ/2)); AM–GM ensures every matrix satisfies the constraint. The boundary modulus squared is a concave quadratic in cos φ. Its vertex is feasible exactly for u≥c (apart from the harmless degenerate endpoints), giving v_max=1 there and v_max=uc+h√(1−u²) below. Substitution into the 2s₂ branch yields a nondecreasing bound below c (the derivative numerator is c(1+u)/√(1−u²)+h−1≥0) and the decreasing square bound 2/(1+u) above. The s₁ branch is at most one by Frobenius invariance. The witness has F=4, u=c and v=1, so it gives exactly sec(δ/4), including δ=π where c=0. The δ=0 map preserves singular values and rank one gives equality. Cross-ratio one is exactly row-times-column phase factorization; Taylor expansion gives 1+δ²/32+O(δ⁴).

## originality

PASS

The supported distinct claim is the exact weak-target law on unimodular 2×2 symbols with a sharp witness, not the gauge reduction, boundedness or a strong Schatten norm. The strongest identified nearby indexed theorem is for S₄, and the cited broad weak-type theorem does not give exact weak norms. An uncited mention of a weak phase formula is a material priority risk, but does not identify a separate exact result or establish coverage.

## value

PASS

The smallest dimension with a nonfactorable phase symbol is a natural complete endpoint test. A sharp functional law and explicit witnesses distinguish quadratic weak-endpoint sensitivity from the linear strong-norm behavior, which cannot be read from a boundedness theorem or a single sign example. This gives a concrete benchmark for proposed sharp endpoint or amplified estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
