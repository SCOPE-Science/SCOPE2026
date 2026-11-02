---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For the odd-order splitting field, the character basis satisfies F_chi F_psi=N*1_{psi=chi^(-2)} F_(chi^(-1)). Its multiplier permutation T:chi↦chi^(-2) has fixed exactly chi^3=1 and no nontrivial 2-cycles (T²chi=chi entails chi³=1). Thus each nonfixed orbit is a cycle of length>=3, and commutator coefficients along it are arbitrary neighboring 2×2 determinants. The explicit cycle lemma covers even lengths by alternating independently chosen even vertices, odd lengths>=5 by a path of independent even vertices, and length3 separately; works even in characteristic2 and with zeros. Hence every vector in the known commutator span is a SINGLE bracket; dimension N-|A[3]|; width0 iff 3A=0, else1. Fresh exhaustive cycle-image checks covered every determinant target over F2 at lengths3–8 and over F3 at lengths3–5, not all groups.

## originality

PASS

Zhang Theorem 2.3 determines the linear span/nonunital commutator algebra (and hence its dimension), but membership in span does not imply representation as ONE bilinear commutator. Bardakov–Passi–Singh and Sangare–Ta supply earlier finite widths/general bounds and an explicit modular width-two example, not an all-odd-order split-field width-one theorem in the inspected material.

## value

PASS

An entire infinite family of explicitly posed commutator-width problems is solved by a nontrivial prescribed-minor surjectivity lemma and constructive Fourier witnesses. The distinction between spanning commutators and single commutators is meaningful, as the known modular counterexample demonstrates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
