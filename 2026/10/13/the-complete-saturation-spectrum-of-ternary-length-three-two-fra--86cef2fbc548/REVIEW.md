# Scientific review

## Correctness — PASS

Two-frameproofness is exactly avoidance of 972 forbidden triples on the complete set of 27 ternary three-coordinate words. Every feasible code has one increasing-index enumeration path. Direct maximality checking against all excluded words yields the stated 1,092 maximal codes. A second implementation uses base-three bitmask incompatibilities and produces the identical full catalogue. Direct orbit closure under generating alphabet/coordinate permutations yields nine disjoint orbits; enumeration of the one-word deletions of the 12 nine-word codes gives exactly 108 distinct size-eight codes, equal to the total feasible count at size eight. Both verifiers assert the nonzero cardinality profile, finite coverage and all symmetry sizes.

## Originality — PASS, with limitations

The closest primary literature covers frameproof code bounds and constructions (Chee–Zhang and Blackburn) and, separately, stronger identifiable-parent variants (Tô–Safavi-Naini). It does not state a classification of all inclusion-maximal ternary length-three two-frameproof codes. Maximum-cardinality classifications, including the known nine-word case, cover only 12 of the 1,092 terminal codes; they cannot imply the other 1,080 maximal codes or the nonoccurrence of maximal size eight. An earlier unindexed table remains a genuine risk. Relevant inaccessible primary papers were not declared noncovering on snippets alone.

## Value — PASS

The saturation spectrum measures how badly a greedy process of adding fingerprint users until no further addition is possible can underperform an optimal design. The minimum terminal size three versus optimum nine quantifies that gap. The complete list of nine isometry classes and the unique extension of every size-eight code give a structural account of the terminal landscape, not merely a witness, renaming or routine re-enumeration of maximum-size designs.

## Boundaries and nearest literature

Chee–Zhang (arXiv:1206.5863) was inspected in full; the Guo thesis was inspected in relevant theoretical sections. Blackburn (DOI:10.1137/S0895480101384633) could not be inspected in full. Tô–Safavi-Naini (DOI:10.1137/S0895480102400424) was inspected through all 23 pages; its Theorem 34 establishes the much smaller ternary two-IPP maximum of four words, and its section 7 optimizes IPP code size, rather than enumerating inclusion-maximal two-frameproof codes. Classification is finite and exact only at the stated parameters. The accompanying code is a reproducible exhaustive computational proof, not an independent external audit.

Self-review: passed. Independent audit: not yet performed.
