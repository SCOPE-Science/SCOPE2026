---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. Reconstructed independence and maximality in the difference Cayley graph with forbidden residues ±1,±3,±4. Necessity: successive gaps cannot be 1,3,4 or >=10 (the vertex five inside an oversized gap is undominated), two adjacent 2 gaps produce forbidden distance four, and any 7/8/9 gap requires 2 on both sides to dominate its offset-two interior vertices. Sufficiency: all nonconsecutive selected vertices have shortest forward gap sum at least 7; endpoint distance steps ±1,±3,±4 and flanking 2 gaps cover all interior sites. Verified base sizes with direct graph enumeration and independently constructed cyclic gap words for n=5..17, including n=12 both size 2 and 3 and n=13 only size 3. Base pairs at n=14..18 and recurring insertion of a gap of 5 between two <=6 gaps give consecutive sizes at all n>=14. Double count ordered rooted gap words to obtain nW/k, with k=1 and 2 cyclic conventions checked. Finite tests are corroboration, not a proof of the infinite extension; the local dominance argument and induction supply that proof.

## originality

PASS

PASS (best knowledge). Hooshmand formulates three-element index stability and develops two-element cases; Brown–Hoshino provides the general well-covered circulant difference framework and other explicit graph-family classifications. A general difference sequence lemma alone does not enumerate all independent dominating sets of the noninterval connection set {1,3,4} or force the exceptional n=13. No source inspected gives the six-gap rules and infinite cutoff as an implied corollary. Older unindexed well-covered circulant calculations or independent domination tables remain a concrete priority risk.

## value

PASS

PASS. Maximal packings of translates of the smallest noninterval normalized triple A={0,1,4} are a natural next instance of the published three-subset index-stability problem. The result is a complete all-order classification with exceptional stable n=13 and exact independent dominating set cardinality distribution, not an arbitrary single graph or routine renaming; both symbolic gap descriptions and constructive infinite witness families are reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
