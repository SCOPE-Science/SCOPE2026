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

For any finite poset P and downsets A,B the Heyting implication is A→B={p: downarrow(p)∩A⊆B}. Every minimal excluded p has all strict predecessors in A, so p belongs to C=A→B precisely if these predecessors lie in B. The equation (C→A)=A is therefore equivalent to S(A)⊆B, where S(A) is their predecessor boundary; other excluded points lie above a minimal one. The number of successful consequents is |J(P\S(A))|, giving the universal sum of failures. If P has a least element, each nonempty proper A has a failure B=empty; a strict length-three chain makes an additional failure, forcing rooted star for equality. If P has a greatest point, the coatom A=P\{g} has h−2 failures and comparable elements below g create an additional one, yielding dual star. Two-antichain-level formula follows by counting distinct proper-upper antecedents times proper-lower consequents. Independent direct Heyting pair evaluation checked a 3-chain (h,F)=(4,3), a rooted 4-element star (9,7), its dual (9,7), and the 2+2 two-level poset (7,9); all checked against the boundary failure criterion.

## originality

PASS

Bumpus–Kocsis (2021 arXiv, 2025 journal) explicitly study this same two-variable Peirce equation; Corollary 3.11 shows no uniform satisfiability gap, a qualitative result rather than exact finite-rooted failure counts or equality cases. Birkhoff duality supplies representation not the extremal count. The claim’s quantitative refinement is not implied by their corollary alone.

## value

PASS

Quantifying how close finite non-Boolean Heyting algebras can be to satisfying Peirce law is the expressly studied degree-of-satisfiability problem. The exact boundary formula for arbitrary finite P plus sharp rooted/co-rooted carrier-dependent lower bound and rigid equality cases measure how qualitative near-classicality behaves; this is a motivated natural classification, not a trivial restatement of no-gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
