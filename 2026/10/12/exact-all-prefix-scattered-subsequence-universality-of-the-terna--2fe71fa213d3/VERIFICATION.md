---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The standard greedy-arch theorem identifies subsequence universality U with the number of complete-alphabet greedy arches. Binary Thue–Morse t(8j+i)=t(j) xor t(i) and the explicit difference coding yield exactly four aligned length-16 templates according to (t(j),t(j+1)). Independently reconstructed these four templates; exhaustive scan of all four against all eight input masks finds exactly five completed arches, and every incoming singleton mask exits as the singleton of the last symbol. Thue–Morse cannot contain 000 or 111 (via even/odd recurrences); the remaining six adjacent triples and all first 0≤r<16 positions give floor(r/3) plus the single correction for k≥1,r=2,t(k−1)≠t(k). Thus U(16k+r)=5k+floor(r/3)+correction for every k, not only tested k. Independent direct difference-word scan confirmed the formula on 160001 prefixes; the finite-table reduction itself is the infinite argument. Remainder check gives -10≤16U(N)-5N≤6, sharp at r=2 for equal/unequal adjacent t; both occur infinitely using t(4j+1)=t(4j+2) and t(4j)≠t(4j+1).

## originality

PASS

The fundamental Barker et al. arch characterization and general algorithms, Schnoebelen–Veron compressed-word arch operations and Adamson et al. absent-subsequence extremal bounds are acknowledged. They do not state the closed all-prefix 16-residue formula for the specific ternary Thue difference word or its sharp discrepancy. The new four-template/six-context analysis is required to specialize the general invariant. Semantic Resultary query and published primary full text found no stronger word-specific theorem. A poorly indexed older computation of the same squarefree word remains possible.

## value

PASS

Every-prefix coverage by arbitrary scattered subsequences is an established natural word-combinatorics invariant. The exact formula for a canonical ternary squarefree infinite word, global 5/16 density, sharp bounded discrepancy and a nontrivial single-residue correction form a motivated closed classification, not merely an arbitrary numerical prefix census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
