---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: Maximal ternary order-four Kautz cycles correspond bijectively to Euler circuits in the overlap digraph of 12 proper length-three vertices and 24 proper length-four edges. Anchoring the unique edge 0101 removes rotation. Every complete Euler circuit determines one of 2^12 local binary in/out transition matchings; independently re-enumerated all 4096 systems using source-independent code, retained precisely 384 single-24-edge tours, checked all cyclic windows, and applied exact canonical rotation, reversal and six-symbol-permutation orbit computations: 24 reversal-fixed; 204 bracelets; 64 relabeling classes; 34 with reversal; 4 reflective relabeling classes. The general obstruction uses at most two fixed window positions of a cycle reflection: for odd k>=3 there are at least six proper palindromes of length k, contradiction; for even k>=4 and even q>=4, each of at least four length-(k-1) proper palindromes occurs q-1 odd times, forcing too many fixed positions. The finite census covers only q=3,k=4, while the parity necessity covers all q>=3,k>=3.

## originality

PASS

PASS best-of-knowledge: Rosenfeld Theorem 9 already counts 384 rotation classes, correctly credited, but the inspected 2002 text distinguishes enumeration with orientation from reversal class identification. Burris et al. 2016 study an unoriented de Bruijn coverage requirement, not reversal-fixed complete Kautz sequences; orthogonal de Bruijn constructions likewise do not count these group-action orbits. No Resultary exact Kautz orbit census/obstruction was located; residual risk of unindexed bracelet-Kautz enumeration remains.

## value

PASS

PASS: Enumeration of symmetry classes, rather than the already-known total cycle count, is the natural next isomorphism-level question for universal Kautz cycles. The exact chiral/achiral quotient profile and four canonical reflective types give a complete meaningful small-parameter classification, and the general parity obstruction explains structural possibilities beyond the finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
