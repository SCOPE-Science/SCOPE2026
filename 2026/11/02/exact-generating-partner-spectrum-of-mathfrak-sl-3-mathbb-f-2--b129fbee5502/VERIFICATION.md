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

The result concerns precisely 256 traceless 3x3 matrices over F2. Rational canonical forms give seven complete similarity classes with orbit sizes 1,21,84,42,28,56,24. Bracket closure via exact row reduction gives generated Lie subalgebra because each iteration adds all brackets and terminates by dimension eight. The pinned source has two distinct all-65536-pair enumerators plus an orbit-reduced all-partner enumerator. Independently constructed a nine-bit matrix-product/bracket and exhaustive subalgebra-closure implementation: full dimension multiplicities (0:1,1:765,2:3618,3:7392,4:20160,5:20160,6:0,7:0,8:13440) and partner spectrum (0:50,56:24,64:126,72:56) exactly reproduced. Hence probability 13440/65536=105/512; nonzero 49 without partners comprise 21 rank-one square-zero plus 28 rank-two idempotents. Unlike sampling, enumeration is exhaustive finite proof once independently checked.

## originality

PASS

The complete fixed binary small-case partner and generated-dimension census is not logically implied by the inspected asymptotic and 2-generator-existence results, or by a nilpotent-restricted obstruction. The expanded journal full text and historical small-algebra tables remain priority risks, but no decisive covering formula was identified.

## value

PASS

Conditional generation probabilities and obstructions are natural quantitative refinements of Lie-algebra two-generation. The seven-class enumeration isolates the exact binary smallest rank-three spectrum and a substantive failure of one-and-a-half generation, not an arbitrary single example or a recomputation of mere generator existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
