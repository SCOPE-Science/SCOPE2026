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

The two markers 0000 at offset zero of a 0-block and 11 at offset one of a 1-block do not cross image boundaries, and each length-8 factor reveals a unique block phase. Long bispecial factors must start at offset 3 and end at offset 0, hence have Phi(u)=01 beta(u) 0 with complete preservation of bilateral-extension pairs; no other long bispecials. Enumerating all seven permitted source triples yields only nonzero short orders: empty +1, 0 +1, 000 -1, 010 +1, 101 -1. The identity Delta^2 p(m)=sum_{|u|=m} bilateral_order(u) gives the stated alternating 2/3 slopes. The excess increment count at s_k and t_k+1 yields the two limiting ratios. Independent reconstruction of all seven triple contexts reproduced all short seeds; independent sliding-window enumeration of a 78125-symbol prefix agreed with p(n) for n=1..120. Finite checks do not establish infinite desubstitution, which is proved by marker uniqueness.

## originality

PASS

Andrade--Mol constructs this exact 5-uniform binary fixed point to exhibit richness and avoid additive fifth powers, without giving the exact word-specific factor complexity or two accumulation slopes in its inspected theorems. General automatic-word complexity algorithms do not imply the explicit interval-structured closed formula. Resultary and targeted searches found no same-morphism explicit sequence.

## value

PASS

Ordinary factor complexity is a canonical invariant of a named combinatorial-avoidance witness. Exact alternation between two linear slopes (rather than a single asymptotic slope) reflects its self-similar bispecial structure and may matter for future comparisons of rich and power-free constructions; it is not a random finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
