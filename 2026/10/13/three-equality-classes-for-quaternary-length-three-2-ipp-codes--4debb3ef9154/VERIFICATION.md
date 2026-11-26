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

Independently reconstructed the forbidden-subset test. At a descendant with no common parent, either two parent coalitions are disjoint or a pairwise-intersecting family of pairs contains the three edges of a triangle. A disjoint singleton and pair also witnesses that triangle; two distinct singletons cannot yield a common descendant. The triangle test is coordinatewise failure of three distinct symbols in every coordinate, and the disjoint-pair test is coordinatewise intersection of the symbol sets of the pairs. Exhaustion using these obstructions finds 4320 codes of size five through 000 and no size-six code through 000; transitivity and heredity show this proves optimality. Applying all 82944 group elements directly to each listed representative gives disjoint orbits of sizes 20736, 13824, 20736, with 1620, 1080, 1620 through 000 and stabilizers 4, 6, 4. These cover the normalized census, yielding all 55296 labeled unordered maxima. The three asserted agreement graphs follow directly from coordinate equality; the middle uses 12 symbols summed across coordinates versus 11 for the first, so it is not alphabet-usage minimal among maxima. Independent replay: python3 /workspace/checks/2ipp.py. The historical type numbers could not be rechecked in the inaccessible article; the graph descriptions themselves are verified.

## originality

PASS

Pass for the full quaternary equality census and its orbit and stabilizer refinement, not the known scalar optimum, known local obstructions or general agreement-graph method. Positive prior evidence does not imply the whole census, with an explicit remaining primary-access caveat.

## value

PASS

The equality layer at the established small quaternary optimum is a natural classification target, not an arbitrary sample. It resolves whether the selected minimal graphs account for every maximum in this parameter and gives a concrete nonminimal extremal shape plus exact orbit sizes useful for comparing small-optimum constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
