---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: On the 120 permutations in S5, the exact Chebyshev d_infty>=3 adjacency graph has 5,340 edges; a complete independent Bron–Kerbosch bitset algorithm enumerated all 4,694,132 maximal cliques and found maximum size 10 with exactly 192 labeled maximum cliques. Applying the exact coordinate-permutation S5 action times global value reversal (240 maps) partitions maxima into 3 orbits of sizes 24,48,120, stabilizers 10,5,2 and pair-distance spectra (30,15),(25,20),(28,17) at distances 3 and 4. Independent code reconstructed everything from metric, not from certificate.json; 15-second run; no random heuristic or unsound partial enumeration.

## originality

PASS

PASS (qualified): The exact optimum P(5,3)=10 is already published by Bereg et al (2023 preprint/2024 article) as the case n=5 of P(n,n−2)=10. Originality is only the complete 192 labeled-extremizer census and three natural 240-group orbits with distinguishing pair spectra. The primary initial Chebyshev-paper small table and later 2025 bounds discussion do not determine these extremizer orbit types. Resultary related (5,3) Ulam metric census is a different metric, not dominating coverage.

## value

PASS

PASS: n=5 is the first nontrivial extremal case for the known P(n,n−2)=10 sequence. Exact counts and natural isometry orbit structure are motivated structural invariants of optimum packing codes; an exhaustive finite classification is independently worthwhile here and can support later larger-n investigations. Value does not rest on the already known P(5,3) scalar maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
