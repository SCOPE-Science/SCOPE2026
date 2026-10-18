---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For smooth lattice polygon P, smooth toric jet-bundle/discriminant formula gives dual degree c(P)=3A-2B+V for hypersurface dual, primal degree A (A normalized area), and Pick+adjunction gives A=2g+B-2. Subtract yields 4g+V-4. Every smooth lattice triangle is unimodularly equivalent to d Delta: at its two other vertices primitive-edge determinants force a=b=gcd(a,b) after normalizing the first vertex. Interior count is (d-1)(d-2)/2 and d>=2 ensures nondefect, hence exactly triangular g permit excess 4g-1 uniquely. All other g have V>=4; rectangle [0,2]x[0,g+1] has genus g, four vertices, is smooth and for g>=1 nondefective, attaining 4g. Genus 0 nondefective quadratic Veronese d=2 attains -1; unimodular d=1 defective is explicitly excluded. Independent exact tests covered d2..39 and g0..99; they support but are not the proof.

## originality

PASS

The standard smooth toric discriminant face-volume formula, Pick and adjunction are prior, while the fixed sectional-genus lower-envelope problem and sharp triangular-genus equality classification constitute a distinct explicit extremal theorem. Relevant full DNV paper provides c(P) but does not state this min_g result. This is an elementary but nontrivial synthesis of smooth triangle rigidity, existence at all remaining genera and discriminant identities.

## value

PASS

At fixed sectional genus, sharp excess of dual versus primal degree is a natural projective-geometric extremal invariant. The result classifies its all-genus envelope and unique three-vertex equality cases, with explicit four-vertex realizations elsewhere; the one-unit dips distinguish Veronese genera. The exact boundary is motivated by smooth lattice polygon geometry, not an arbitrary finite search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
