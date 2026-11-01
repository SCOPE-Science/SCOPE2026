---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The graph components are directed paths and directed cycles; stable semantics forces a single alternating phase on each path, two phases on each even cycle, none on odd cycles. Thus stable extensions are binary r-vectors, and a pairwise symmetric difference is a weighted Hamming distance with weight ell_i. For any three codewords, a constant column can be changed into a nonconstant column without reducing any distance. Every nonconstant binary triple has exactly one agreeing pair, so assigning each cycle to its agreeing pair gives the pairwise distances W-w_1,W-w_2,W-w_3. Every three-bin assignment is realized by such columns. With r>=2 positive cycles, an optimal partition has max bin weight <W, guaranteeing three distinct codewords. Reachable weighted bin pairs (a,b) give O(rW^2) exact DP. Our independent direct triple-codeword check matched ten multicyclic cases, but the column partition argument is the infinite proof.

## originality

PASS

Compared precise theorems against their implication directions and alternate formulations using inspected primary literature and Resultary; no covering statement identified; residual priority risks remain and absence of a match is not a novelty proof.

## value

PASS

The simultaneous three-extension diversity objective is natural for selecting genuinely different explanations in argumentation semantics. The theorem gives an exact all-instance answer and polynomial-time algorithm for a structural graph fragment that can have exponentially many extensions, with a sharp balance criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
