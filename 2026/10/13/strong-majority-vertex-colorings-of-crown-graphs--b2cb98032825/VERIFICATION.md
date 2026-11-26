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

For n≥3 the integer neighborhood bound is h=floor((n−1)/2) and the count of a color on B seen by a_i is its side count minus the indicator for b_i. If the count is between h+1 and n−1, a vertex omitting a different color sees all of it; if it is n, every count is n−1>h. A side count at most h is always sufficient, and the other side is symmetric. Properness is not required. The same palette of ceil(n/h) colors can fill both sides and fewer colors have insufficient capacity. To increase the used-color count, split off one vertex from a class of size at least two into a fresh color; such a class exists until all 2n colors are used. For named palettes sum multinomials on one side and square by independence, then use inclusion–exclusion on absent names. An independent direct check reproduces both kinds of counts and the structural predicate on 672,856 assignments, yielding optimal named counts 36, 576, 8100, 8100 at n=3,4,5,6.

## originality

PASS

The inspected results cover the scalar C6 case but not the general crown capacity criterion, spectrum, or exact named and surjective counts. The closest indexed crown result uses a different majority rule; the closest static same-invariant result uses a different graph family. Pass is for the combined crown result, not the known C6 number.

## value

PASS

Crowns are a natural near-complete regular bipartite test for a neighborhood coloring invariant. A full classification captures when missing edges affect the constraint; the spectrum and named and onto counts specify all valid colorings, and the order-four exception is not apparent from general bounds. The usable exact profile goes beyond recomputing a known cycle value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
