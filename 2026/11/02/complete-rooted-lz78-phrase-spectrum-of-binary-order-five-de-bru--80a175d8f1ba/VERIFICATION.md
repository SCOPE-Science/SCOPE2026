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

The five-bit successor permutations have exactly 2^16 admissible feedback functions g(t); a feedback function produces one circular de Bruijn word iff state 00000 lies in a full 32-state orbit. This bijection exhausts cycles up to rotation without bit complement/reversal quotient. Independent fresh feedback enumeration generated 2048 distinct cycles and parsed all 32 roots of each by a set-based shortest unseen prefix parser, giving c=11:80, 12:7586, 13:55690, 14:2180 and joint (L,H) counts (11,13):6,(11,14):44,(12,13):746,(12,14):1172,(13,13):30,(13,14):50. Source verifier additionally implements distinct Euler tours and trie parsing; both inspected line by line. The finite proof is exhaustive because 2^16 is the complete parametrization.

## originality

PASS

Classical de Bruijn cycle count 2048 and incremental LZ78 algorithm are prior art. Cohn–Helfgott study asymptotic reversal asymmetry using de Bruijn-based constructions, and Dutta et al random-access parsing, neither materially inspected statement supplies this exact rooted order-five spectrum. Published record semantic search returned related string attractors not the same statistic. Best-of-knowledge novelty of the complete finite joint table with parsing-convention specificity.

## value

PASS

Root sensitivity of incremental LZ78 on canonical maximally factor-rich cyclic binary words is a natural compression invariant; the complete first nontrivial exact distribution, extremizers and 30 root-invariant cycles give a reusable baseline rather than an arbitrary unmotivated checksum. Restriction to order five is explicit and all 2048 cycles are enumerated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
