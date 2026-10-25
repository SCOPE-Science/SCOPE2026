---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The actual RESULT.md proves the Strehl-summand valuation identity ν₂(T)=s₂(n)+c₁+c₂, where c₁ and c₂ are binary carry counts for a+k=n and 2a+b=n. Simultaneous carry-free addition corresponds bijectively to subsets of positions with two adjacent 1 bits, giving 2^t(n) minimal summands. Their normalized sum is odd exactly if t(n)=0. Fibonacci no-adjacent-ones count and density-one divisibility then follow. Independently re-evaluated exact integers for n=0..71; this is corroboration, not a proof of all n.

## originality

PASS

The published Strehl identity and standard binary carry formula are prior methods. No matched published sharp all-index adjacency equivalence or its Fibonacci census emerged in the consulted primary sources and Resultary search; this remains a best-of-knowledge finding, not global novelty certification.

## value

PASS

Franel valuations are a motivated classical arithmetic problem; the all-index exact sharpness boundary and Fibonacci census give a nontrivial, reusable classification beyond the existing lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
