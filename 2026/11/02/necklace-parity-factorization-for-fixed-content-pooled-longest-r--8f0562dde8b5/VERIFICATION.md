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

Using exact common content c with ≥2 symbols, every n−1 read has a uniquely determined missing symbol and exactly two possible full words (left/right addition). Consequently full-word edges and read vertices form disjoint cyclic rotation orbits. For an odd cycle incidence is injective, while an even cycle d=2r has 1-dimensional integer alternating kernel; its nonnegative fiber has min-even+min-odd+1 points. Choosing a canonical even-min-zero representative gives local image Hilbert factor (1−z^r)/(1−z)^d; requiring also an odd zero gives singleton factor (1−z^r)^2/(1−z)^d. Multiplying independent cycles yields both all-content generating functions; primitive-orbit exponents follow from exact Möbius inversion. Earliest collision requires r strands and occurs only at the smallest allowed even period d*, with ν_c(d*) two-preimage profiles. Independent literal prefix/suffix multiset enumeration gave c=(1,1,2),k2: 75 profiles/72 singleton/3 double; c=(2,2,2),k3: 125566/125552/14 double; c=(1,1),k1: 1 double profile. Full all-k statements follow from incidence argument, not finite tests.

## originality

PASS

Fixed-content necklace cycles, de Bruijn shorthand, and general multistrand substring-model code-rate theorems are prior ingredients, as is the specific single-marker c=(n−1,1) parity case. The claim additionally gives arbitrary-content multicycle product formulas for exact image and singleton counts and first ambiguity. Composition-profile reconstruction observes different data and cannot imply these raw-string count formulas by title similarity. A general graph semigroup/flow theorem might imply the identity under another name.

## value

PASS

An exact image cardinality equals optimal zero-error reconstruction code size for a sharply specified practical combinatorial measurement. The joint singleton generating function and first ambiguous pool size are natural nontrivial invariants of the same read channel; multiple simultaneous necklace orbits make this more than a single-marker substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
