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

PASS: For k=2m the target set is exactly 2^m complement-reversal-fixed edges of the binary order-(k−1) de Bruijn graph. Every cyclic host can be rotated to start at P_m=0^m1^m. BFS states (suffix-of-length k−1, bitmask of witnessed target edges) with its forced first edge have a bijection with such rooted indexed cycles; BFS distance and layerwise shortest-path counts give C_m,R_m. The distinct Held–Karp shortest overlap-route recurrence gives matching minimum cyclic cover lengths: distinct required occurrences along any cycle have gaps ≥k−longest proper suffix-prefix overlap, while an overlap tour spells a cycle with those factors. I independently compiled a different C++ BFS and checked exhaustive values m=1: (2,1), m=2:(9,2), m=3:(26,14), m=4:(67,1232); m=4 first optimum discovered after 4,190,096 BFS states. A separate Python subset-DP returned minima 2,9,26,67 and directly tested the 67-symbol witness contains all 16 targets. Enumerative result is finite m≤4, not an infinite theorem.

## originality

PASS

PASS best of knowledge: earlier RC-complete sequence constructions require covering one representative for EACH reverse-complement pair of ALL k-mers; the RC-fixed-point antipalindromes are compulsory but are only a tiny target subset, so the optimum and the number of rooted optimal cycles are not determined by those designs. Constrained-language de Bruijn Euler circuits aim at once-each admissible-edge coverage; general cyclic cover and reversal-superstring problems use different target sets/allowed orientations. No exact finite table (2,9,26,67) or rooted multiplicities located in inspected sources; a directly related publisher study could not be examined completely and remains a residual risk.

## value

PASS

PASS: the fixed-point antipalindrome family is a natural reverse-complement invariant DNA-word subset with nontrivial overlap constraints; a certified exact length-eight optimum and counted rooted optima are concrete reproducible combinatorial invariants beyond trivial tiny cases, even though no uniform formula for all m is claimed. Both independent finite-state methods certify minimum, and rooted counts distinguish genuine solution multiplicity from just one witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
