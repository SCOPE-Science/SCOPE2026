---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The forbidden local Watson–Crick motif ab̅b̅a on a four-letter alphabet excludes exactly 16 length-four words. Reading cyclic n-periodic words, including repeated-letter wraps n=1,2,3, as closed n-step walks in the explicitly constructed 64 triple-state de Bruijn graph is a bijection. Independent direct matrix construction recovered exact characteristic polynomial x^36(x-1)^3(x+1)^3(x²+1)^2(x³-3x²-2x-3)(x^5-x^4+x^3-4x²+2x-3)^2(x^5+x^4+x^3+4x²+2x+3), with integer symbolic determinant independent of stored proof coefficients. Exact trace computations gave C1..C7=(4,12,64,228,744,2904,10420). The inspected verifier computes all 64 traces, checks the entire 64-degree det(I-zM) via Newton identities, and separately brute-checks small circular words; that is a complete finite determinant identity, not an infinite sequence extrapolation. Formal -log det(I-zM)=sum C_n z^n/n proves the displayed rational dynamical zeta for every n, and Mobius inversion proves primitive oriented necklace counts. Strong connectivity with a loop and Perron–Frobenius, plus polynomial root isolation on (3,4), give capacity log2(3.7473465403...) ≈1.9058694. Scope is only local cyclic length-four avoidance, not global hairpin or DNA secondary-structure constraints.

## originality

PASS

Compared the exact claim and implications with the named primary mathematics and published Resultary records. The actual semantic query was 'Resultary: Watson Crick reverse complement palindrome length four cyclic DNA words zeta transfer matrix necklace'. No materially inspected source supplies or logically dominates the stated instance; inaccessible/unindexed source risks remain.

## value

PASS

The exact all-period periodic-point zeta, primitive-orbit counts and entropy of a natural four-base reverse-complement local forbidden-motif shift are useful constrained-coding invariants. Although transfer matrices are textbook methods, the evaluated nontrivial 64x64 determinant, quintic factors, short-period wraparound and capacity are a substantive exact classification, not a mere name substitution or tiny case check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
