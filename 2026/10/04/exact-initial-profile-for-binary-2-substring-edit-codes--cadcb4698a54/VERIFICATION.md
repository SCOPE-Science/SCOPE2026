---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

An at-most-one 2-substring edit is exactly replacement of a contiguous removed block of size 0..2 by inserted binary block of size 0..2, including unchanged output. Reconstructed finite output balls independently and took compatibility edges iff balls are disjoint. Coloring bound produces independent classes, hence any clique extending a branch uses ≤ number of classes; all other candidates branch, establishing exhaustive upper bounds. An independent bitmask clique search over all 2^n vertices gave maxima 1,1,1,1,2,3,5,8 for n=1..8 (largest n=8 256 vertices, 24,196 visited recursion nodes), and witness size 8. The package verify.py directly enumerates two ball constructions and exhaustively uses the same valid color bound; its full source was inspected.

## originality

PASS

Best-of-knowledge PASS on finite exact profile: accessible full Li et al. source gives asymptotic constructions and the original Tang paper is a channel/long-length construction; none actually read establishes optimality for n=1..8. Two plausible papers (Tang full text and Oct 2026 Ye/Ge) were not fully accessible and remain explicit risk. A temporarily unavailable semantic index is not evidence of novelty.

## value

PASS

A natural exact code-capacity invariant under the well-studied one-2-substring-edit channel: first nontrivial short-block transitions at n=5..8 and a sharp optimum at n=8. Exact finite optima distinguish constructions whose asymptotic redundancy results alone cannot answer short-block design. Finite exhaustive search is motivated, not inherently a landmark theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
