---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For each bit of positive d and n, carries c_j for n+jd (j=1..4), previous bits of the five samples and four relative Rudin–Shapiro parity differences form a finite exact binary-addition transducer. The next relative bit is updated by xor of adjacent-one products; n bits may be chosen nondeterministically. After d bits finish, all remaining input-difference bits are zero: the least fixed point over zero-digit transitions correctly characterizes every possible terminated relative signature, including arbitrary finite higher starting digits. Independently implemented transducer from these digit equations, enumerated precisely 864 NFA states, computed terminal masks by monotone closure, then exhaustive subset construction to exactly 1302 reachable deterministic states. Verified all 2604 transitions, class counts 2/13/1287 by truncated popcount of d, and terminal masks 0x0001 / 0xff96 / 0xffff for zero/one/two-plus set bits. This is a finite inductive proof for ALL finite positive binary differences. Four missing relative signatures for popcount1 double to eight excluded length-five words; adding separated high binary block 11 complements every absolute bit without affecting offsets or relative mask. Thus exactly 24 patterns for powers of two and all 32 for other d. The direct d=1..128 sample in source is not used to establish universal quantifiers.

## originality

PASS

Konieczny–Müllner arXiv:2309.03180 defines arithmetical word complexity using existential quantification over a choice of common difference, so maximal length-five global support does not imply support for EVERY fixed d. Sobolewski arXiv:2204.05287 studies maximal monochromatic progressions, not all nonconstant words. Jugé–Marcovici correlation paper establishes frequency/correlation properties at offsets, not the exact zero/nonzero status of the 32 ordered words at every specified arithmetic difference. Resultary queries under fixed-step 5-term Rudin–Shapiro and dyadic missing pattern support revealed no equivalent publication. Strongest risk is unindexed implicit calculation, not prior title similarity.

## value

PASS

This is a complete sharp exact support classification for a canonical automatic sequence at every fixed arithmetic step, with a genuine and surprising dyadic versus nondyadic dichotomy and eight exceptional words. It answers a natural order-five pattern-realizability question, stronger than the existential quantifier in arithmetic subword complexity, and includes an auditable finite-state certificate for all differences. No general theorem about longer patterns, pattern frequencies or all automatic sequences is required for its independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
