# Self-review

## Correctness — PASS

The finite proof reduces uniqueness of a perfect matching to an explicit hitting condition against every alternative perfect matching. Complete enumeration of all perfect matchings, all 120 automorphisms, and all deletion subsets below the claimed minima and at the minima establishes the exact orbit-resolved certificate profile. A separately designed bitmask verifier uses an LCF presentation and independently tests every perfect matching without assuming the automorphism orbits. Both executable programs and their recorded outputs are present. The graph isomorphism between the two presentations is checked explicitly.

## Originality — PASS, with named residual risks

Lei, Yeh and Zhang's 2014 work establishes the object and general theory. The 2015 fullerene theorem supplies the graph-level anti-forcing minimum 4 and forbids disjoint witnesses of size 4; Han, Zhou and Wang's 2023 work establishes the **already-known spectrum \([4,5]\)**. The new result is therefore explicitly confined to the exact 30/6 symmetry multiplicities, the 8/22 and 4/5 minimum-witness multiplicities, and the shared sharp disjoint-deletion threshold of eight. A targeted record search returned matching-complex results for the dodecahedron, whose homological claims do not entail this edge-deletion census. A full-text comparison of the relevant primary articles supports the distinction. A later paper could contain a fine-grained table, and the 2023 authors may have unpublished matching-by-matching computational data; searches cannot eliminate these residual priority risks.

## Value — PASS

The twenty-vertex dodecahedron is the smallest fullerene and a canonical molecular matching graph. An anti-forcing certificate selects bonds whose deletion rigidifies a chosen Kekulé structure; restricting these deletions to independent bonds is a natural locality constraint. The previously-known optimum 4 and the structural theorem that four deletions cannot be independent do not determine the actual restricted optimum. The exact jump to eight for every one of the 36 structures, the symmetry distinction between ordinary and constrained witness counts, and the closed polynomials give a complete and reproducible benchmark rather than an arbitrary slice or rephrasing.

## Limits

Only the single named graph is covered. No blanket claim of global priority is justified by negative searches. Exhaustive computation is valid here because the state space is explicitly finite and completely traversed. The two implementations are independent computations performed within the same review process, not external validation.

Self-review: passed. Independent audit: not yet performed.
