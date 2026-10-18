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

Every 32-cycle has 32 distinct length-5 factors, each occurs exactly once in length-36 unfolded word; a chosen letter position hits <=5 such windows, so size >=ceil(32/5)=7. A 7-subset hits every length-5 window iff its first mark<=4, last>=31, consecutive mark gaps<=5; exact enumeration gives 120 candidates. Every longer substring contains a length-5 window, so only all 2+4+8+16=30 distinct shorter factors must be checked by occurrence-union masks. Exhaustive Euler recursion on the order-four binary de Bruijn digraph, anchoring its uniquely occurring 00000 edge, enumerates every one of 2048 cycles and 32 cuts each, 65536 unfolded words, without quotienting cuts. The inspected C++ source checks all 120 masks for every cut and directly checks every distinct nonempty factor for one successful witness per cut. Independent alternate Python exhaustive re-enumeration confirmed 2048 circuits, 65536 cuts, 120 candidates, min/max multiplicities 30/120, extrema attained at respectively 4/22 cuts, with 699 distinct independently full-factor-checked cached witnesses; not a general-order proof.

## originality

PASS

Mantaci et al 2021 Proposition 41 gives bounds for de Bruijn attractors but not the exact all-cycle/all-cut binary order-five enumeration. Whittington 2024 Theorem 29 proves optimum for a specified Lyndon-constructed prime-order unfolding and identifies an open general de Bruijn issue; cannot imply all cuts of all 2048 order-five cycles. Béal et al 2025 give algorithms and one-family experiments, not exhaustive rooted-cycle classifications. Unindexed earlier order-five census remains a genuine possibility; qualified best-of-knowledge PASS.

## value

PASS

Full exact invariant for all rooted unfoldings of a canonical extremal factor-complexity family at the first binary order where the length-five window lower bound ceil(32/5) is not integral. Establishes universality at seven marks across all cuts and nontrivial sharp range/frequencies of the count of optimal attractors, resolving a natural finite case of questions in primary literature. Complete finite proof rather than arbitrary sample; not a claim for all orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
