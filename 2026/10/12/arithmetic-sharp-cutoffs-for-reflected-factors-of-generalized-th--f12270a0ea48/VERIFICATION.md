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

The adjacent digit-sum jump is 1−(b−1)ν_b(n+1), so the exact difference coset is D=1−(b−1)Z_m. Long-block digit additivity realizes every alphabet translation, yielding all length-two factors F2={(a,a+d):d∈D}, cardinal m²/g. Reversal of an edge requires D∩(−D), and as D is one coset, D=−D iff g|2; for g≥3 no two-letter reversals. For m≥3, any length-four difference triple for b≥3 has ≥2 occurrences +1 and any reversal would force ≥2 occurrences −1, impossible. For b=2, exhaustive even/odd start types (1,x,1) and (x,1,y) with at least one outer 0 also preclude reversed length-four patterns. Reversible length-three words must be palindromes; when g|2 a carry with j(b−1)≡2(mod m), together with alphabet translations, constructs both (a,a±1,a) for every a, exactly 2m. For m≤2 the constant/alternating/morphism palindrome arguments give full closure. Independent digit-sum prefix computations across seven (b,m) cases corroborated but do not establish the infinite result.

## originality

PASS

The all-base gcd-dependent cutoff is not supplied by the known reflection-complexity source question, generalized Thue–Morse factor-complexity theorems, or Starosta’s dihedral letter-changing antimorphisms; the binary-base modular case is a known special case and explicitly credited.

## value

PASS

This supplies an exact arithmetic trichotomy and all reversal-complexity corrections for a canonical automatic sequence family, closing the specific generalized-language question rather than merely reporting sparse finite experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
