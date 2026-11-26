---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Forcing chains cover the tree, with one initially blue endpoint per chain. A chain contains at most two pendant leaves; the cover by adjacent pairs of teeth, with a one-tooth path in odd order, attains the ceiling lower bound using the tree endpoint theorem. With even n every path must contain two leaves; a chain skipping an index would strand its internal pendant leaf as a singleton, so only the adjacent perfect pairing is possible. With odd n just one path has one leaf. If it has a spine endpoint, no two-leaf path can skip a tooth, so the sole unmatched tooth has odd index and gives the one spine choice. Otherwise either all paired paths are adjacent or exactly one pair skips one tooth and leaves its middle leaf as a singleton. That latter pattern is represented in the stated union by moving the unmatched choice to the selected outer endpoint. For counting distinct odd all-leaf choices, 00 cannot start a valid word. For prefix 10 or 01 the initial two entries can be deleted and prepended bijectively (when q=1 and the word starts 10, entry 3 is selected and can serve as the new singleton). For 11 one needs q=1 and entry 3 zero; there are 2^(m−1) remaining choices. With A₁=3 this yields the stated all-leaf, spine and total counts. The n=2 boundary gives the two endpoints of P₄.

## originality

PASS

The tree path-cover theorem supplies the scalar result and any chosen cover's endpoint construction, not the explicit parity-dependent census of distinct endpoint sets across the standard comb's minimum covers. The closest indexed spider result overlaps at n=3 only, the broader comb literature studies a different forcing game, and graph-operation work inspected does not provide this exact enumeration.

## value

PASS

For the natural path-corona tree family this describes exactly which minimum seed sets can contain a spine vertex and counts the distinct minimum sets, not the representations by path covers. The nonunique odd all-leaf parametrization and parity distinction are genuine structure beyond the known scalar zero forcing number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
