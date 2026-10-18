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

The difference set criterion proves injectivity of (a,b)↦a+b iff no nonzero codeword difference of A equals an opposite difference of B. Fix 0∈A by translating both codebooks by the same XOR mask, equivalently complementing selected coordinates in both (output coordinate flips z↦2−z). Independent newly written C++17 exhaustive algorithm enumerated all 32768 odd A masks, computed 16-vertex conflict graphs and exact MIS recurrence to verify max |A|alpha(G_A)=36. A separate cardinality-constrained full B enumeration found 966 rooted maximum pairs: 192 of (4,9),342 of (6,6),432 of (9,4); XOR translates deduplicated to 2448 ordered labeled pairs with size groups 768,912,768. Enumerating 24 coordinate permutations×16 simultaneous XORs×two user orders partitioned them into 11 orbits of sizes 48 (1),96 (3),192 (3),384 (4). This is exhaustive on the finite 4-bit universe; output was reproduced independently and agrees with actual code, not just logs.

## originality

PASS

Published binary adder-channel work already supplies optimum 36 and asymptotic bounds. This result instead classifies all optimum 4-use code pairs, including the 2448 labeled census and 11 prescribed symmetry orbits. The very relevant Queseth 2024 KTH thesis discusses length-four short optimal constructions, so priority overlap remains a substantial material risk; thesis full text was inaccessible through lawful open routes and institutional Oxford route reported vpn_disconnected. The accessible abstract does not state the whole 2448/11 equality classification, hence a qualified best-of-knowledge acceptance, not novelty certification.

## value

PASS

An all-codebook classification of a known extremal four-use binary adder channel gives useful design diversity beyond merely knowing maximum product 36. The exact 2448 ordered solutions and 11 coordinate/complement/user-exchange orbits provide a complete natural isomorphism-invariant of this finite coding problem, including unequal-size and balanced optima. A finite result is warranted by the coding-theoretic optimum question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
